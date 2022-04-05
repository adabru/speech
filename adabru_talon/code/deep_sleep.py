from talon import (
    Module,
    Context,
)

mod = Module()
mod.tag("deep_sleep", desc="Enable deep sleep")

ctx = Context()


@mod.action_class
class Actions:
    def enable_deep_sleep():
        """???"""
        ctx.tags = ["user.deep_sleep"]

    def disable_deep_sleep():
        """???"""
        ctx.tags = []
