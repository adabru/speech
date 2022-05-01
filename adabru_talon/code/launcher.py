# https://python-xlib.github.io
import Xlib.display
import Xlib.X

from talon import (
    Module,
    Context,
    actions,
    registry,
)

display = Xlib.display.Display()
root = display.screen().root
print(root.list_properties())

mod = Module()
mod.tag("launcher", desc="Launch and focus apps")


class Window:
    def __init__(self, window, main_window):
        """..."""
        self.window = window
        self.main_window = main_window
        self.wm_class = window.get_wm_class()
        self.wm_name = window.get_wm_name()

    def get_children(self):
        """..."""

        def decorate_window(_window):
            """..."""
            if self.window == root:
                return Window(_window, _window)
            else:
                return Window(_window, self.main_window)

        return [decorate_window(child) for child in self.window.query_tree().children]

    def is_valid(self):
        """..."""
        return self.wm_class != None and self.window != root

    def focus(self):
        """..."""
        window = self.window
        root = window.query_tree().root
        while window != root:
            print(window)
            window.raise_window(print)
            window = window.query_tree().parent
        # self.window.raise_window(print)
        # self.main_window.raise_window(print)
        # self.window.set_input_focus(Xlib.X.RevertToPointerRoot, Xlib.X.CurrentTime)


def get_all_windows():
    """..."""
    # window = disp.get_input_focus().focus

    valid_windows = []
    queue = [Window(root, None)]
    # breadth search
    while len(queue) > 0:
        window = queue.pop(0)
        if window.is_valid():
            valid_windows.append(window)
        else:
            queue += window.get_children()
    return valid_windows


@mod.action_class
class Actions:
    def print_debug():
        """..."""
        for window in get_all_windows():
            print(
                f"instance:'{window.wm_class[0]}', class:'{window.wm_class[1]}', name:'{window.wm_name}'"
            )

    def focus_window(label: str):
        """..."""
        for window in get_all_windows():
            if (
                label == window.wm_name
                or label == window.wm_class[0]
                or label == window.wm_class[1]
            ):
                window.focus()
                return
