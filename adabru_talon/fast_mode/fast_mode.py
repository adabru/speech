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
from talon.skia import Shader, Color, Paint, Rect
from talon.types.point import Point2d
from talon_plugins import eye_mouse, eye_zoom_mouse
from typing import Union

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
