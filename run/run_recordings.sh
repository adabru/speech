#!/bin/bash

recordFields="/home/adabru/repo/speech_commands/sphinx/own/etc/own_train.fileids"
outputFolder="/home/adabru/repo/speech_commands/sphinx/own/wav/new"

printf '------ start recording\n'

while IFS= read -r line; do
    if [ ! -z "$line" ]; then
        printf 'record: %s\n' "$line"

        fileName="$outputFolder/$line.wav"

        arecord -r 16000 -f S16_LE $fileName

        printf 'save to: %s\n\n' "$fileName"
    fi
done < $recordFields