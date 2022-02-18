# see https://github.com/knausj85/knausj_talon/blob/master/mouse_grid/mouse_grid.py
from talon import (
    Module,
    Context,
    actions,
    app,
    canvas,
    screen,
    settings,
    ui,
    ctrl,
    cron,
)

mod = Module()
mod.tag("fast_mode", desc="Shorten speech timeout")

ctx = Context()


@mod.action_class
class Actions:
    def make_fast():
        """Reduce speech timeout"""
        ctx.tags = ["user.fast_mode"]

    def make_slow():
        """Default speech timeout"""
        ctx.tags = []


# from slack chat:
#
# from talon import Context, Module
# mod = Module()
# mod.mode("low_latency", help="low speech latency mode")

# from talon import Context
# ctx = Context()
# ctx.matches = "mode: user.low_latency"
# ctx.settings["speech.timeout"] = 0.120
#
# talon fast: mode.enable("user.low_latency")
