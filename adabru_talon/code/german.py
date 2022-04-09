# adapted from https://github.com/mqnc/talon_german

from talon import (
    Module,
    Context,
    actions,
    registry,
)

from talon import speech_system, Context
from talon.engines.vosk import VoskEngine

vosk_de = VoskEngine(model="vosk-model-small-de-0.15", language="de_DE")
speech_system.add_engine(vosk_de)


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


@mod.action_class
class Actions:
    def switch_german():
        """???"""
        ctx.tags = ["user.german"]

    def german_sentence():
        """???"""
        global formatter, end_after_speak
        formatter = "sentence"
        end_after_speak = True
        actions.user.switch_german()

    def german_process(txt: str):
        """???"""
        global formatter, end_after_speak
        if end_after_speak:
            ctx.tags = []


@mod.capture(rule="(.+)")
def german(m) -> str:
    """capture all"""
    return m
