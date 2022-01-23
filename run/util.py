import os, re
import random

folderPath = '/home/slava/speech_commands/sphinx/own'
audioRecordingsFolder = '/home/slava/speech_commands/sphinx/own/wav/train'

def getAudioFile(parts):
    pattern = '^' + '_'.join(parts) + r'_\d*\.wav$'
    audio_file = [f for f in os.listdir(audioRecordingsFolder) if re.search(pattern, f)][0]
    return os.path.join(audioRecordingsFolder, audio_file)

def getCount(audio_file_path):
    count = int(re.findall(r'\d+', audio_file_path)[-1])
    return count

# add prose
vocal_phones = ['A', 'Ä', 'AI', 'AW', 'E', 'EI', 'ER', 'I', 'IH', 'O', 'OA', 'ÖR', 'OI', 'OW', 'U', 'Ü']
consonant_phones = ['B', 'TSCH', 'D', 'F', 'G', 'H', 'J', 'JH', 'K', 'L', 'M', 'N']#, 'P', 'R', 'S', 'SH', 'T', 'TS', 'V', 'W', 'Z']

def getKey(phone):
    return f'perm_{phone}'

# def getConsonantTranscription(phone):
#     CV = [phone + ' ' + s for s in vocal_phones]
#     CV = CV * 2
#     random.seed(phone)
#     random.shuffle(CV)

#     transcription = []
#     for i in range(0, len(CV), 2):
#         transcription += [CV[i] + ' ' + CV[i+1]]
        
#     return transcription

def getConsonantWords(phone):
    vocals = vocal_phones * 2
    random.seed(phone)
    random.shuffle(vocals)

    words = []
    for i in range(0, len(vocals), 2):
        words += [[phone, vocals[i], phone, vocals[i+1]]]
        
    return words
