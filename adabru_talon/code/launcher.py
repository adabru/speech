# wmctrl -lx
# https://github.com/Conservatory/wmctrl/blob/master/main.c#L1261
# https://github.com/Conservatory/wmctrl/blob/master/main.c#L1278
# https://stackoverflow.com/questions/1201179/how-to-identify-top-level-x11-windows-using-xlib
from ewmh import EWMH

from talon import (
    Module,
    actions,
)

ewmh = EWMH()

mod = Module()
mod.tag("launcher", desc="Launch and focus apps")


@mod.action_class
class Actions:
    def print_debug():
        """..."""
        for window in ewmh.getClientList():
            wm_class = window.get_wm_class()
            wm_name = window.get_wm_name()
            print(f"instance:'{wm_class[0]}', class:'{wm_class[1]}', name:'{wm_name}'")

    def focus_window(label: str):
        """..."""
        for window in ewmh.getClientList():
            wm_class = window.get_wm_class()
            wm_name = window.get_wm_name()
            if label == wm_name or label == wm_class[0] or label == wm_class[1]:
                ewmh.setActiveWindow(window)
                ewmh.display.flush()
                return True
        return False

    def switch_app(label: str, command: str):
        """..."""
        if not actions.user.focus_window(label):
            actions.user.system_launch(command)
