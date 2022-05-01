from typing import Set

from talon import Module, Context, actions, app
import sys

default_alphabet = "air beach cap dream egg flop gust hunch sit john ka look made near odd pit cu red sun trap urge vest when plex yank zip".split(
    " "
)
letters_string = "abcdefghijklmnopqrstuvwxyz"

default_digits = "zero one two three four five six seven eight nine".split(" ")
numbers = [str(i) for i in range(10)]
default_f_digits = (
    "one two three four five six seven eight nine ten eleven twelve".split(" ")
)

mod = Module()
mod.list("letter", desc="The spoken phonetic alphabet")
mod.list("symbol_key", desc="All symbols from the keyboard")
mod.list("arrow_key", desc="All arrow keys")
mod.list("number_key", desc="All number keys")
mod.list("modifier_key", desc="All modifier keys")
mod.list("function_key", desc="All function keys")
mod.list("special_key", desc="All special keys")
mod.list("punctuation", desc="words for inserting punctuation into text")


@mod.capture(rule="{self.modifier_key}+")
def modifiers(m) -> str:
    "One or more modifier keys"
    return "-".join(m.modifier_key_list)


@mod.capture(rule="{self.arrow_key}")
def arrow_key(m) -> str:
    "One directional arrow key"
    return m.arrow_key


@mod.capture(rule="<self.arrow_key>+")
def arrow_keys(m) -> str:
    "One or more arrow keys separated by a space"
    return str(m)


@mod.capture(rule="{self.number_key}")
def number_key(m) -> str:
    "One number key"
    return m.number_key


@mod.capture(rule="{self.letter}")
def letter(m) -> str:
    "One letter key"
    return m.letter


@mod.capture(rule="{self.special_key}")
def special_key(m) -> str:
    "One special key"
    return m.special_key


@mod.capture(rule="{self.symbol_key}")
def symbol_key(m) -> str:
    "One symbol key"
    return m.symbol_key


@mod.capture(rule="{self.function_key}")
def function_key(m) -> str:
    "One function key"
    return m.function_key


@mod.capture(rule="( <self.letter> | <self.number_key> | <self.symbol_key> )")
def any_alphanumeric_key(m) -> str:
    "any alphanumeric key"
    return str(m)


@mod.capture(
    rule="( <self.letter> | <self.number_key> | <self.symbol_key> "
    "| <self.arrow_key> | <self.function_key> | <self.special_key> )"
)
def unmodified_key(m) -> str:
    "A single key with no modifiers"
    return str(m)


@mod.capture(rule="{self.modifier_key}* <self.unmodified_key>")
def key(m) -> str:
    "A single key with optional modifiers"
    try:
        mods = m.modifier_key_list
    except AttributeError:
        mods = []
    return "-".join(mods + [m.unmodified_key])


@mod.capture(rule="<self.key>+")
def keys(m) -> str:
    "A sequence of one or more keys with optional modifiers"
    return " ".join(m.key_list)


@mod.capture(rule="{self.letter}+")
def letters(m) -> str:
    "Multiple letter keys"
    return "".join(m.letter_list)


ctx = Context()
modifier_keys = {
    # If you find 'alt' is often misrecognized, try using 'alter'.
    "al": "alt",  # 'alter': 'alt',
    "con": "ctrl",  # 'troll':   'ctrl',
    "shif": "shift",  # 'sky':     'shift',
    "super": "super",
}
ctx.lists["self.modifier_key"] = modifier_keys
alphabet = dict(zip(default_alphabet, letters_string))
ctx.lists["self.letter"] = alphabet

# `punctuation_words` is for words you want available BOTH in dictation and as key names in command mode.
# `symbol_key_words` is for key names that should be available in command mode, but NOT during dictation.
punctuation_words = {
    "period": ".",
    "comma": ",",
    "semicolon": ";",
    "colon": ":",
    "forward slash": "/",
    "question mark": "?",
    "exclamation mark": "!",
    "asterisk": "*",
    "hash sign": "#",
    "percent sign": "%",
    "at sign": "@",
    "ampersand": "&",
    "dollar sign": "$",
    "pound sign": "£",
}
symbol_key_words = {
    "point": ".",
    "com": ",",
    "semi": ";",
    "col": ":",
    "quest": "?",
    "bang": "!",
    "star": "*",
    "hash": "#",
    "percent": "%",
    "at sign": "@",
    "amper": "&",
    "dollar": "$",
    "pound": "£",
    "quote": "'",
    "tick": "`",
    "box": "[",
    "right box": "]",
    "slash": "/",
    "backslash": "\\",
    "plus": "+",
    "dash": "-",
    "equals": "=",
    "tilde": "~",
    "down score": "_",
    "round": "(",
    "right round": ")",
    "brace": "{",
    "right brace": "}",
    "angle": "<",
    "left angle": "<",
    "less than": "<",
    "rangle": ">",
    "right angle": ">",
    "greater than": ">",
    "caret": "^",
    "pipe": "|",
    "dote": '"',
}

ctx.lists["self.punctuation"] = punctuation_words
ctx.lists["self.symbol_key"] = symbol_key_words
ctx.lists["self.number_key"] = dict(zip(default_digits, numbers))
ctx.lists["self.arrow_key"] = {
    "down": "down",
    "left": "left",
    "right": "right",
    "up": "up",
}
ctx.lists["self.special_key"] = {
    "end": "end",
    "start": "home",
    "insert": "insert",
    "space": "space",
    "ipe": "backspace",
    "out": "escape",
    "go": "enter",
    "ace": "delete",
    "ta": "tab",
    # 'junk': 'backspace',
    "pay up": "pageup",
    "pay down": "pagedown",
    "menu key": "menu",
    "print screen": "printscr",
}

ctx.lists["self.function_key"] = {
    f"F {default_f_digits[i]}": f"f{i + 1}" for i in range(12)
}
