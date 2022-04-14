# adapted from https://github.com/mqnc/talon_german

import time
import pickle
import os.path
import re

from talon import (
    Module,
    Context,
    actions,
    registry,
)
from talon.grammar import Phrase
from talon import speech_system, Context
from talon.engines.vosk import VoskEngine

vosk_de = VoskEngine(model="vosk-model-small-de-0.15", language="de_DE")
vosk_de.set_vocab(["finish", "bapfel", "hückelhoven"])
speech_system.add_engine(vosk_de)

capitalized_words = set()


def load_dictionary():
    global capitalized_words
    dictionary_path = os.path.realpath(
        os.path.join(os.path.abspath(__file__), "../../dictionary/german.dic")
    )
    dictionary_cache_path = os.path.realpath(
        os.path.join(os.path.abspath(__file__), "../../dictionary/german.pickle")
    )
    # load dictionary
    if not os.path.exists(dictionary_cache_path) or os.path.getmtime(
        dictionary_cache_path
    ) < os.path.getmtime(dictionary_path):
        # recreate cache
        with open(dictionary_path, encoding="ISO-8859-1") as file:
            for word in file:
                if word[0].isupper():
                    capitalized_words.add(word.lower().strip())
        with open(dictionary_cache_path, "wb") as file:
            # Pickle the 'data' dictionary using the highest protocol available.
            pickle.dump(capitalized_words, file, pickle.HIGHEST_PROTOCOL)
    else:
        # read from cache
        with open(dictionary_cache_path, "rb") as file:
            capitalized_words = pickle.load(file)


load_dictionary()

mod = Module()
mod.tag("german", desc="Start german dictation")

ctx__activate = Context()
ctx__activate.matches = "tag: user.german"
ctx__activate.settings = {
    "speech.engine": "vosk",
    # 	'speech.language': 'de_DE',
    "speech.timeout": 0.2,
}

ctx = Context()


formatter = None
end_after_speak = False


class State:
    start_of_sentence = True
    latent_space = False


dictation_state = State()

punctuation_words = {
    "punkt": ".",
    "strich": ",",
    "ausrufezeichen": "!",
    "fragezeichen": "?",
    "doppelpunkt": ":",
}

end_of_sentence_words = {
    "!",
    "?",
    ".",
}


@mod.action_class
class Actions:
    def activate_german():
        """???"""
        ctx.tags = ["user.german"]

    def deactivate_german():
        """???"""
        ctx.tags = []

    def german_sentence():
        """???"""
        global formatter, end_after_speak
        formatter = "sentence"
        end_after_speak = True
        actions.user.activate_german()

    def german_dictation():
        """???"""
        global formatter, end_after_speak
        formatter = "dictation"
        end_after_speak = False
        dictation_state.start_of_sentence = True
        dictation_state.latent_space = False
        actions.user.activate_german()

    def german_words():
        """???"""
        global formatter, end_after_speak
        formatter = "words"
        end_after_speak = True
        actions.user.activate_german()

    def german_process(phrase: Phrase):
        """???"""
        global formatter, end_after_speak
        if formatter == "sentence":
            text = phrase[0].upper() + phrase[1:] + "."
        elif formatter == "dictation":
            text = ""
            for word in phrase:
                # avoid space before following symbols
                if word == "eingabe" or word in punctuation_words:
                    dictation_state.latent_space = False
                # insert space after last word
                if dictation_state.latent_space:
                    text = text + " "
                    dictation_state.latent_space = False
                if word in punctuation_words:
                    # replace punctuation words
                    text = text + punctuation_words[word]
                    if punctuation_words[word] in end_of_sentence_words:
                        dictation_state.start_of_sentence = True
                    dictation_state.latent_space = True
                elif word == "eingabe":
                    text = text + "\n"
                elif dictation_state.start_of_sentence or word in capitalized_words:
                    # capitalize first word in sentence
                    text = text + word[0].upper() + word[1:]
                    dictation_state.start_of_sentence = False
                    dictation_state.latent_space = True
                else:
                    text = text + word
                    dictation_state.latent_space = True
        else:
            text = phrase
        actions.insert(text)
        if end_after_speak:
            ctx.tags = []

    def german_dictation_add():
        """???"""
        print("to do")
