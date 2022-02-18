# see https://github.com/knausj85/knausj_talon/blob/master/mouse_grid/mouse_grid.py
import time
from talon import (
    Module,
    Context,
    actions,
    app,
    canvas,
    screen,
    settings,
    ui,
    noise,
    ctrl,
    cron,
    registry,
)
from talon_plugins.eye_mouse import config, toggle_control

mod = Module()
mod.tag("wheel_pop", desc="Enable pop scrolling")

ctx = Context()

scroll_job = None
was_controlling = False


@mod.action_class
class Actions:
    def enable_wheel_pop():
        """???"""
        global scroll_amount, was_controlling
        ctx.tags = ["user.wheel_pop"]
        scroll_amount = abs(scroll_amount)
        was_controlling = config.control_mouse
        toggle_control(False)

    def disable_wheel_pop():
        """???"""
        global was_controlling
        ctx.tags = []
        toggle_control(was_controlling)


def on_pop(active):
    if not "user.wheel_pop" in registry.tags:
        return
    global scroll_job, scroll_amount, last_pop
    t = time.time()
    # double pop
    if scroll_job is None:
        start_scroll()
    elif t - last_pop < 0.3:
        scroll_amount = scroll_amount * -1
    else:
        stop_scroll()
    last_pop = t


noise.register("pop", on_pop)


scroll_amount = 40
last_pop = 0


def scroll_continuous_helper():
    global scroll_amount
    actions.mouse_scroll(by_lines=False, y=int(scroll_amount))


def start_scroll():
    global scroll_job
    if scroll_job is None:
        scroll_job = cron.interval("40ms", scroll_continuous_helper)


def stop_scroll():
    global scroll_job
    if scroll_job != None:
        cron.cancel(scroll_job)
        scroll_job = None
