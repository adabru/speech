#!/usr/bin/python

import subprocess
import util

# default project to build
modelName = "own"
modelFolderPath = f"/home/adabru/repo/speech_commands/sphinx/{modelName}"

dictionaryDataFilePath = f"{modelFolderPath}/etc/{modelName}.dic.sh"
dictionaryFilePath = f"{modelFolderPath}/etc/{modelName}.dic"
phonesFilePath = f"{modelFolderPath}/etc/{modelName}.phone"
fileIdsFilePath = f"{modelFolderPath}/etc/{modelName}_train.fileids"
transcriptionFilePath = f"{modelFolderPath}/etc/{modelName}_train.transcription"
lmFilePath = f"{modelFolderPath}/etc/{modelName}.lm"


print("================= generate =================")
print(f"  model name : {modelName}")
print(f"  path       : {modelFolderPath}")
print("=================  generate  =================\n")

# parse dictionary
dictionary = {}
phones = {"SIL"}

with open(dictionaryDataFilePath, newline="") as dictionaryDataFile:
    Lines = dictionaryDataFile.readlines()
    for line in Lines:
        if line[0] == "#":
            continue

        parts = line.strip().split()
        key = parts[0]
        dictionary[key] = parts[1:]

        phones.update(parts[1:])

# generate dictionary
with open(dictionaryFilePath, "w") as dictionaryFile:
    for key, value in dictionary.items():
        dictionaryFile.write(f"{key}\t{' '.join(value)}\n")


# generate phones
with open(phonesFilePath, "w") as phonesFile:
    phonesFile.write("\n".join(sorted(phones)))
    phonesFile.write("\n")

# generate fileIds
fileIds = {}
error = False
with open(fileIdsFilePath, "w") as fileIdsFile:
    # for key, value in dictionary.items():

    #     try:
    #         audio_file_path = util.getAudioFile(value)

    #         # store path to recording
    #         fileIds[key] = "train" + audio_file_path[len(util.audioRecordingsFolder):-4]
    #         fileIdsFile.write(fileIds[key] + "\n")

    #     except IndexError as e:
    #         print(f'WARNING: could not find recording for {key}: {value}')

    for phone in util.consonant_phones:
        for word in util.getConsonantWords(phone):
            key = "_".join(word)
            fileIds[key] = f"train/{key}"
            fileIdsFile.write(fileIds[key] + "\n")


# generate transcription
with open(transcriptionFilePath, "w") as transcriptionFile:
    # for key, parts in dictionary.items():
    #     if key in fileIds:
    #         audio_file = util.getAudioFile(parts)
    #         count = util.getCount(audio_file)
    #         transcriptionFile.write('<s> ' + key + (f' <sil> {key}' * (count - 1)) + f' </s> ({fileIds[key]})\n')

    for phone in util.consonant_phones:
        for word in util.getConsonantWords(phone):
            key = "_".join(word)
            transcriptionFile.write(
                "<s> " + " ".join(word) + f" </s> ({fileIds[key]})\n"
            )

# generate lm
with open("/tmp/corpus.txt", "w") as corpusFile:
    for key in dictionary.keys():
        corpusFile.write(f"<s> {key} </s>\n")

try:
    subprocess.run(
        f"text2wfreq < /tmp/corpus.txt | wfreq2vocab > /tmp/{modelName}.vocab",
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    ).check_returncode()

    subprocess.run(
        f"text2idngram -vocab /tmp/{modelName}.vocab -idngram /tmp/{modelName}.idngram < /tmp/corpus.txt",
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    ).check_returncode()

    subprocess.run(
        f"idngram2lm -vocab_type 0 -idngram /tmp/{modelName}.idngram -vocab /tmp/{modelName}.vocab -arpa {lmFilePath}",
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    ).check_returncode()

except subprocess.CalledProcessError as e:
    print(e)
