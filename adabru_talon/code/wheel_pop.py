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
mod.tag("wheel_pop", desc="Enable pop scrolling")

ctx = Context()


@mod.action_class
class Actions:
    def enable_wheel_pop():
        """???"""
        ctx.tags = ["user.wheel_pop"]

    def disable_wheel_pop():
        """???"""
        ctx.tags = []
