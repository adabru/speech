#!/usr/bin/python

# local
from unix_socket import UnixSocket
from logger import logger

sock_keyboard = UnixSocket("/tmp/evdev_keypress.sock", 100)
sock_gui = UnixSocket("/tmp/speech_gui.sock", 100)

modifiers = set()
hold_modifiers = False
pause_engine = False
confirm_function = None


# direct communicators
def sendGuiState(key):
    msg = "%s%s%s%s%s%s%s" % (
        "1" if pause_engine else "0",
        "1" if hold_modifiers else "0",
        "1" if "shift" in modifiers else "0",
        "1" if "ctrl" in modifiers else "0",
        "1" if "alt" in modifiers else "0",
        "1" if "win" in modifiers else "0",
        key,
    )
    sock_gui.try_send(msg)


# keys and modifiers
def sendKeyCode(keyboardCode):
    global hold_modifiers
    mods = ""
    for mod in modifiers:
        mods += f"{mod}+"

    # sock_keyboard.try_send(f"{mods}{keyboardCode}")

    # logger.info(f"hold_modifiers: {hold_modifiers}")
    if not hold_modifiers:
        releaseModifiers(False)
    sendGuiState(keyboardCode)


def activateModifier(modifier):
    modifiers.add(modifier)
    logger.info(f"mods: {'+'.join(modifiers)}")
    sendGuiState(modifier)


def holdModifiers():
    global hold_modifiers
    hold_modifiers = True
    logger.info(f"hold modifiers - mods: {'+'.join(modifiers)}")
    sendGuiState("hold")


def releaseModifiers(send=True):
    global hold_modifiers
    modifiers.clear()
    hold_modifiers = False
    if send:
        sendGuiState("release")


#
def pauseEngine():
    global pause_engine
    pause_engine = True
    logger.info("pause engine")
    sendGuiState("pause")


def continueEngine():
    global pause_engine
    pause_engine = False
    logger.info("continue engine")
    sendGuiState("continue")


#
def noop(phone="noop"):
    ()


def getPermissionFor(f, infoText):
    global confirm_function
    confirm_function = f
    sendGuiState(infoText)

    switchLm("confirmation")


#
def poweroff():
    noop()
    # cmdCommand = "shutdown -h now"
    # process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)


keyCodes = {
    "A": "a",
    "B": "b",
    "C": "c",
    "D": "d",
    "E": "e",
    "F": "f",
    "G": "g",
    "J": "j",
    "H": "h",
    "I": "i",
    "K": "k",
    "L": "l",
    "M": "m",
    "N": "n",
    "O": "o",
    "P": "p",
    "Q": "q",
    "R": "r",
    "S": "s",
    "T": "t",
    "U": "u",
    "V": "v",
    "W": "w",
    "X": "x",
    "Y": "y",
    "Z": "z",
    "ZERO": "0",
    "NULL": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "ROUND_LEFT": "(",
    "ROUND_RIGHT": ")",
    "TAG_LEFT": "<",
    "TAG_RIGHT": ">",
    "SQUARE_LEFT": "[",
    "SQUARE_RIGHT": "]",
    "ESCAPE": "escape",
    "UP": "up",
    "DOWN": "down",
    "LEFT": "left",
    "RIGHT": "right",
    "PAGE_UP": "pgup",
    "PAGE_DOWN": "pgdown",
    "START": "home",
    "END": "end",
    "SPACE": "space",
    "ENTER": "enter",
    "TAB": "tab",
    "DELETE": "del",
    "BACKSPACE": "backspace",
    # "SAY <TEXT>":                Text("%(text)s",
    # "F ONE": "f1",
    # "F TWO": "f2",
    # "F THREE": "f3",
    # "F FOUR": "f4",
    # "F FIVE": "f5",
    # "F SIX": "f6",
    # "F SEVEN": "f7",
    # "F EIGHT": "f8",
    # "F NINE": "f9",
    # "F TEN": "f10",
    # "F ELEVEN": "f11",
    # "F TWELVE": "f12",
    # "DEGREE": "°",
    "CARET": "^",
    "CURLY_LEFT": "{",
    "CURLY_RIGHT": "}",
    "QUESTION": "?",
    "EXCLAMATION": "!",
    "BACK_TICK": "`",
    "PIPE": "|",
    "MINUS": "minus",
    "DOT": ".",
    "COMMA": "comma",
    "BACKSLASH": "\\",
    "UNDERSCORE": "_",
    "STAR": "*",
    "COLON": "colon",
    "SEMICOLON": ";",
    "AT": "@",
    "DOUBLE_QUOTE": '"',
    "SINGLE_QUOTE": "'",
    "HASH": "hash",
    "DOLLAR": "$",
    "EURO": "euro",
    "PERCENT": "percent",
    "SLASH": "slash",
    "AMPERSAND": "&",
    "EQUAL": "=",
    "PLUS": "+",
    "COMPOSE": "menu",
}

mapping = {}
for (key, keyValue) in keyCodes.items():
    mapping[key] = lambda keyValue=keyValue: sendKeyCode(keyValue)

mapping["WIN"] = lambda: activateModifier("win")
mapping["ALT"] = lambda: activateModifier("alt")
mapping["CONTROL"] = lambda: activateModifier("ctrl")
mapping["SHIFT"] = lambda: activateModifier("shift")

mapping["CUT"] = lambda: ()
mapping["COPY"] = lambda: ()
mapping["PASTE"] = lambda: ()

mapping["HOLD"] = lambda: holdModifiers()
mapping["RELEASE"] = lambda: releaseModifiers()

mapping["PAUSE"] = lambda: pauseEngine()
mapping["CONTINUE"] = lambda: continueEngine()

#
mapping["POWEROFF"] = lambda: getPermissionFor(poweroff, "poweroff system? [Yes|No]")

# noop
mapping["YES"] = lambda: noop()
mapping["NO"] = lambda: noop()


import os, sys

# https://github.com/bambocher/pocketsphinx-python
from pocketsphinx import LiveSpeech

# modelName = 'cmusphinx-voxforge-de-5.2'
# modelName = 'an4_sphere/an4'
modelName = "own"
# modelName = 'confirmation'
modelPath = f"/home/adabru/repo/speech_commands/sphinx/{modelName}"

current_lm = "own"

global speech
if len(sys.argv) > 1:
    import os
    from pocketsphinx import AudioFile

    config = {
        "verbose": False,
        "audio_file": sys.argv[1],
        "buffer_size": 2048,
        "no_search": False,
        "full_utt": False,
        "hmm": os.path.join(modelPath, f"model_parameters/{modelName}.ci_cont"),
        "lm": os.path.join(modelPath, f"etc/{modelName}.lm"),
        "dic": os.path.join(modelPath, f"etc/{modelName}.dic"),
    }

    speech = AudioFile(**config)


def getSpeech(lm_name):
    # https://github.com/cmusphinx/pocketsphinx/blob/master/include/cmdln_macro.h
    # https://github.com/cmusphinx/sphinxbase/blob/master/include/sphinxbase/fe.h
    return LiveSpeech(
        verbose=False,
        sampling_rate=16000,
        buffer_size=2048,
        no_search=False,
        full_utt=False,
        pip=1000.0,  # Phone insertion penalty
        wip=1000.0,  # Word insertion penalty
        nwpen=1000.0,  # New word transition penalty
        # pbeam=1e-10, # Beam width applied to phone transitions
        # fwdtree=False, # Run forward lexicon-tree search (1st pass)
        # fwdflat=False, # Run forward flat-lexicon search over word lattice (2nd pass)
        # logfn="/home/adabru/repo/speech_commands/sphinx/own/logdir/test.txt",
        # senlogdir="/home/adabru/repo/speech_commands/sphinx/own/logdir",
        # backtrace=True,
        hmm=os.path.join(modelPath, f"model_parameters/{modelName}.ci_cont"),
        lm=os.path.join(modelPath, f"etc/{lm_name}.lm"),
        dic=os.path.join(modelPath, f"etc/{modelName}.dic"),
    )


def switchLm(lm_name):
    global current_lm
    current_lm = lm_name


def getSegment():
    while True:
        last_lm = current_lm
        for phrase in getSpeech(current_lm):
            segments = phrase.seg()
            findings = ""

            for s in segments:
                findings += f"{s.word} {s.prob} "
            logger.debug(findings)

            for s in segments:
                yield s

            if last_lm != current_lm:
                break


logger.debug("entering loop")
for s in getSegment():
    if s.word == "<s>" or s.word == "</s>" or s.word == "<sil>":
        continue

    if not pause_engine or s.word == "CONTINUE":
        if confirm_function:
            if s.word == "YES":
                confirm_function()
                confirm_function = None
                switchLm("keyboard")
                sendGuiState(s.word)
            elif s.word == "NO":
                confirm_function = None
                switchLm("keyboard")
                sendGuiState(s.word)
        # else:
        # mapping[s.word]()
