# local
from unix_socket import UnixSocket 

# create socket client with dragonfly handling
import logging

import dragonfly
from dragonfly import *

sock_keyboard = UnixSocket('/tmp/evdev_keypress.sock', 100)
sock_keyboard.connect()

sock_gui = UnixSocket('/tmp/speech_gui.sock', 100)

modifiers = set()
hold_modifiers = False

if False:
    logging.basicConfig(level=10)
    logging.getLogger('grammar.decode').setLevel(20)
    logging.getLogger('compound').setLevel(20)
    # logging.getLogger('kaldi').setLevel(30)
    logging.getLogger('engine').setLevel(10)
    logging.getLogger('kaldi').setLevel(10)
else:
    # logging.basicConfig(level=20)
    from dragonfly.log import setup_log
    setup_log()


class ExampleCustomRule(dragonfly.CompoundRule):

    spec = "I want to eat <food>"
    extras = [
        dragonfly.Choice(
            "food", {"(an | a juicy) apple": "good",
                     "a [greasy] hamburger": "bad"}
        )
    ]

    def _process_recognition(self, node, extras):
        good_or_bad = extras["food"]
        print("That is a %s idea!" % good_or_bad)


def sendGuiState(key):
    msg = "%s%s%s%s%s%s" % (
        "1" if hold_modifiers else "0",
        "1" if "shift" in modifiers else "0",
        "1" if "ctrl" in modifiers else "0",
        "1" if "alt" in modifiers else "0",
        "1" if "win" in modifiers else "0",
        key
    )
    sock_gui.try_send(msg)

def sendKeyCode(keyboardCode):
    global hold_modifiers
    mods = ""
    for mod in modifiers:
        mods += f"{mod}+"

    sock_keyboard.send(f"{mods}{keyboardCode}")
    
    print(f"{mods}{keyboardCode}")

    print(f"hold_modifiers: {hold_modifiers}")
    if not hold_modifiers:
        releaseModifiers(False)
    sendGuiState(keyboardCode)

def activateModifier(modifier):
    modifiers.add(modifier)
    print(f"mods: {'+'.join(modifiers)}")
    sendGuiState(modifier)

def holdModifiers():
    global hold_modifiers
    hold_modifiers = True
    print(f"hold modifiers - mods: {'+'.join(modifiers)}")
    sendGuiState("hold")

def releaseModifiers(send = True):
    global hold_modifiers
    modifiers.clear()
    hold_modifiers = False
    if send:
        sendGuiState("release")

class ExampleDictationRule(dragonfly.MappingRule):
        
    keyCodes = {
        # "dictate <text>": dragonfly.Function(lambda keyValue=keyValue: print("I heard %r!" % str(text))),
        # "duplicate <n>":                    release + Key("c-c, c-v"),
        
        "escape":                     "escape",
        "up":                         "up",
        "down":                       "down",
        "left":                       "left",
        "right":                      "right",
        "page up":                    "pgup",
        "page down":                  "pgdown",
        "start":                      "home",
        "end":                        "end",

        "space":                      "space",
        "enter":                      "enter",
        "tab":                        "tab",
        "delete":                     "del",
        "back space":                 "backspace",
        # "say <text>":                Text("%(text)s",

        "_a": "a",
        "b": "b",
        "c": "c",
        "d": "d",
        "e": "e",
        "f": "f",
        "g": "g",
        "j": "j",
        "ha": "h",
        "i": "i",
        "k": "k",
        "la": "l",
        "om": "m",
        "nay": "n",
        "_o": "o",
        "p": "p",
        "q": "q",
        "r": "r",
        "s": "s",
        "t": "t",
        "u": "u",
        "_v": "v",
        "_w": "w",
        "x": "x",
        "y": "y",
        "z": "z",

        # "F one": "f1",
        # "F two": "f2",
        # "F three": "f3",
        # "F four": "f4",
        # "F five": "f5",
        # "F six": "f6",
        # "F seven": "f7",
        # "F eight": "f8",
        # "F nine": "f9",
        # "F ten": "f10",
        # "F eleven": "f11",
        # "F twelve": "f12",
        # "degree": "°",

        "circus": "^",
        "curly left": "{",
        "curly right": "}",
        "question": "?",
        "exclamation": "!",
        "back tick": "`",
        "(vertical bar|pipe)": "|",
        "(dash|minus|hyphen)": "minus",
        "(dot|period)": ".",
        "comma": "comma",
        "backslash": "\\",
        "underscore": "_",
        "(star|asterisk)": "*",
        "colon": "colon",
        "semicolon": ";",
        "at": "@",
        "[double] quote": "\"",
        "single quote": "'",
        "hash": "hash",
        "dollar": "$",
        "euro": "euro",
        "percent": "percent",
        "slash": "slash",
        "ampersand": "&",
        "equal": "=",
        "plus": "+",

        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",

        "para left": "(",
        "para right": ")",
        "tag left": "<",
        "tag right": ">",
        "square left": "[",
        "square right": "]",
    }

    mapping = {}
    for (key, keyValue) in keyCodes.items():
        mapping[key] = dragonfly.Function(lambda keyValue=keyValue: sendKeyCode(keyValue))
 
    mapping[f"win"] = dragonfly.Function(lambda: activateModifier(f"win"))
    mapping[f"alter"] = dragonfly.Function(lambda: activateModifier(f"alt"))
    mapping[f"control"] = dragonfly.Function(lambda: activateModifier(f"ctrl"))
    mapping[f"shift"] = dragonfly.Function(lambda: activateModifier(f"shift"))

    mapping[f"hold"] = dragonfly.Function(lambda: holdModifiers())
    mapping[f"release"] = dragonfly.Function(lambda: releaseModifiers())

    # extras = [dragonfly.Dictation("text")]



# Load engine before instantiating rules/grammars!
# Set any configuration options here as keyw
# ord arguments.
engine = dragonfly.get_engine("kaldi",
    model_dir='kaldi_model',
    # tmp_dir='kaldi_tmp',  # default for temporary directory
    # vad_aggressiveness=3,  # default aggressiveness of VAD
    vad_padding_start_ms=5,  # default ms of required silence surrounding VAD
    vad_padding_end_ms=5,
    # input_device_index=None,  # set to an int to choose a non-default microphone
    # cloud_dictation=None,  # set to 'gcloud' to use cloud dictation
    )
# Call connect() now that the engine configuration is set.
engine.connect()

grammar = dragonfly.Grammar(name="mygrammar")
# rule = ExampleCustomRule()
# grammar.add_rule(rule)
grammar.add_rule(ExampleDictationRule())
grammar.load()

engine.do_recognition()
