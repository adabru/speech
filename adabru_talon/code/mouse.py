# https://github.com/elichad/elichad_talon/blob/main/mouse_drag_on_hiss.py
from talon import Module, actions, ctrl, noise, cron, registry
from time import sleep, time

start = 0
running = False
noise_length_threshold = "200ms"
threshold_passed = False

mod = Module()


def still_running():
    global running
    global threshold_passed
    if running:
        threshold_passed = True
        toggle_mouse_drag(True)
        # print("hiss duration passed threshold, starting gaze drag")


def cursor_drag_on_hiss(is_active):
    global start
    global running
    global threshold_passed
    if is_active:
        start = time()
        running = True
        cron.after(noise_length_threshold, still_running)
    else:
        running = False
        if threshold_passed:
            threshold_passed = False
            toggle_mouse_drag(False)
            # print("end of hiss detected, disabling gaze drag")


def toggle_mouse_drag(active: bool):
    if active:
        ctrl.mouse_click(button=0, down=True)
    else:
        ctrl.mouse_click(button=0, up=True)


noise.register("hiss", cursor_drag_on_hiss)


def on_pop(active):
    if "user.wheel_pop" in registry.tags:
        return
    ctrl.mouse_click(button=0, hold=16000)


noise.register("pop", on_pop)


@mod.action_class
class Actions:
    def toggle_mouse(state: bool = None):
        """???"""
        print(state)
        actions.tracking.control_toggle(state)
