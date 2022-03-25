#!/usr/bin/python

import os
import sys
import re
import numpy as np
from pocketsphinx import AudioFile
from scipy.io import wavfile

import util

folderPath = "/home/adabru/repo/speech_commands/sphinx/own"
dictionaryDataFilePath = f"{folderPath}/etc//own.dic.sh"
audioRecordingsFolder = f"{folderPath}/wav/train"

dictionary = {}


def findSegments(audioFilePath):
    rate, data = wavfile.read(audioFilePath)

    segments = []
    threshold = np.int16(1000)
    in_word = False
    sil_length = 0

    data = np.abs(data)
    for f, value in enumerate(data):
        if value > threshold:
            sil_length = 0
            if not in_word:
                in_word = True
                segment = {"startFrame": f, "endFrame": f}
                segments += [segment]
        else:
            sil_length += 1

        # find next word
        if in_word and sil_length > 0.2 * rate:
            in_word = False
            segment["endFrame"] = f - int(0.2 * rate)

    for segment in segments:
        # print(f"start: {segment['startFrame']/rate}s end: {segment['endFrame']/rate}s")
        # print(f"duration: {(segment['endFrame'] - segment['startFrame'])/rate}s end: {segment['endFrame']/rate}s")
        segment["startTime"] = segment["startFrame"] / rate
        segment["endTime"] = segment["endFrame"] / rate

    return segments


def checkRecording(key, audioFilePath):
    config = {
        "verbose": False,
        "audio_file": audioFilePath,
        "buffer_size": 2048,
        "no_search": False,
        "full_utt": False,
        "hmm": os.path.join(folderPath, "model_parameters/own.ci_cont"),
        "lm": os.path.join(folderPath, "etc/own.lm"),
        "dic": os.path.join(folderPath, "etc/own.dic"),
    }

    speech = AudioFile(**config)

    segments = []
    for phrase in speech:
        segments += phrase.seg()
    segments = [s for s in segments if s.word not in ["<sil>", "<s>", "</s>"]]

    print(f"\n{key}")
    if all(s.word == key for s in segments):
        print("✓")
    else:
        recognizedWords = [s.word for s in segments]
        print(f"{' '.join(recognizedWords)}")

    oracle = findSegments(audioFilePath)

    count = len(oracle)
    expected_count = int(re.findall(r"\d+", audioFilePath)[-1])
    if count != expected_count:
        print(
            f"WARNING: oracle found {count} segments, but file name says {expected_count}"
        )

    for i in range(count):
        tolerance = 0.15
        if (
            abs(segments[i].start_frame / 100 - oracle[i]["startTime"]) > tolerance
            or abs(segments[i].end_frame / 100 - oracle[i]["endTime"]) > tolerance
        ):
            print(
                "WARNING: times differ, segment[%.3f, %.3f], oracle[%.3f, %.3f]"
                % (
                    segments[i].start_frame / 100,
                    segments[i].end_frame / 100,
                    oracle[i]["startTime"],
                    oracle[i]["endTime"],
                )
            )
            break


with open(dictionaryDataFilePath, newline="") as dictionaryDataFile:
    Lines = dictionaryDataFile.readlines()
    for line in Lines:
        if line[0] == "#":
            continue

        parts = line.strip().split()
        key = parts[0]

        dictionary[key] = parts[1:]

if len(sys.argv) > 1:
    key = sys.argv[1]
    parts = dictionary[sys.argv[1]]
    checkRecording(key, util.getAudioFile(parts))

else:
    for key, parts in dictionary.items():
        checkRecording(key, util.getAudioFile(parts))
