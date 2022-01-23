#!/usr/bin/python

import os
import numpy as np
import sounddevice as sd
from scipy.io import wavfile
import util

dictionaryFilePath = f'{util.folderPath}/etc/own.dic'
recordingFolder = f'{util.folderPath}/wav/train'

COUNT = 99
FS = 16000  # Sample rate
DEFAULTSEGMENTDURATION = 0.8
sd.default.device = 'Razer Seiren Mini'
sd.default.samplerate = FS
sd.default.channels = 1
sd.default.dtype = 'int16'
sd.default.blocksize = 2048


def is_float(value):
    try:
        float(value)
        return True
    except:
        return False


print('================= settings =================')
print(f"  destination path      : {recordingFolder}")
print(f"  number of repetitions : {COUNT}")
print('=================  record  =================\n')

transcriptions = {}

# get all transcriptions from dictionary
# with open(dictionaryFilePath, newline='') as dictionaryFile:
#     Lines = dictionaryFile.readlines()
#     for line in Lines:
#         if line[0] == '#':
#             continue

#         # define file name
#         parts = line.strip().split()
#         key = parts[0]
#         recordFileName = "{}_{:02}.wav".format('_'.join(parts[1:]), COUNT)

#         transcriptions[recordFileName] = [' '.join(parts[1:])] * COUNT

# generate transcriptions for consonants
for phone in util.consonant_phones:
    for word in util.getConsonantWords(phone):
        transcriptions['_'.join(word) + ".wav"] = [' '.join(word)]

# run records
i = 0
items = list(transcriptions.items())
last_index = 0
while i < len(items):
    file_name = items[i][0]
    transcription = items[i][1]
    i += 1

    recordFilePath = f"{recordingFolder}/{file_name}"

    if os.path.exists(recordFilePath):
        print(f"recording for '{file_name}' -> '{file_name}' already exists")
    else:
        recordDuration = DEFAULTSEGMENTDURATION

        # wait for user to be ready
        B = '\033[1m'
        R = '\033[22m'
        rerecord = f'|{B}r{R}erecord' if last_index != -1 else ''
        recordingText = f"Start recording for '{file_name}' -> '{file_name}' [{B}Y{R}es|<duration>|{B}s{R}kip|{B}q{R}uit{rerecord}]"
        userInput = input(recordingText)
        if userInput in ['skip', 's']:
            # print ('\033[2A')
            print(
                f"skipped recording for '{file_name}' -> '{file_name}'                 ")
            continue

        elif userInput in ['quit', 'q']:
            break

        elif userInput in ['rerecord', 'r']:
            last_file_name = items[last_index][0]
            os.remove(f"{recordingFolder}/{last_file_name}")
            os.remove(f"{recordingFolder}/headset/{last_file_name}")
            i = last_index
            last_index = -1
            continue
            
        elif is_float(userInput):
            recordDuration = float(userInput)

        # start recording
        i = 0
        recordings = []
        recordings2 = []
        skip_frames = 0
        in_noise = True

        with sd.InputStream() as stream, sd.InputStream(device="default") as stream2:
            sil_length = 0
            in_word = False

            while i < len(transcription):
                frames, overflowed = stream.read(stream.blocksize)
                frames2, overflowed2 = stream2.read(stream2.blocksize)
                recordings += [frames]
                recordings2 += [frames2]

                overflowed = overflowed or overflowed2
                if overflowed:
                    print('WARNING: stream has overflowed')

                for f in range(len(frames)):
                    if abs(frames[f]) >= 1000:
                        sil_length = 0
                        if not in_noise and not in_word:
                            in_word = True
                    else:
                        sil_length += 1

                    if sil_length > .2 * FS:
                        if in_noise:
                            in_noise = False
                            print(
                                f'left: {len(transcription) - i}, next words: {transcription[i:i+2]}')

                        elif in_word:
                            in_word = False
                            i += 1
                            print('\033[2A')
                            print(
                                f'left: {len(transcription) - i}, next words: {transcription[i:i+2]}')

                    elif in_noise:
                        skip_frames += 1

        # cut the noise at the beginning
        recording = np.concatenate(recordings)
        recording = recording[skip_frames:]
        wavfile.write(recordFilePath, FS, recording)

        recording2 = np.concatenate(recordings2)
        recording2 = recording2[skip_frames:]
        wavfile.write(f"{recordingFolder}/headset/{file_name}", FS, recording2)

        last_index = i-1

        print('\033[2A')
        print('\033[1A')
        print(
            f"Finished recording for '{file_name}' -> '{file_name}'          ")
