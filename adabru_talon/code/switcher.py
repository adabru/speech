import os
import re
import time

import talon

from talon import Context, Module, app, imgui, ui, fs, actions
from glob import glob
from itertools import islice
from pathlib import Path
import subprocess

mod = Module()
mod.list("running", desc="all running applications")
mod.list("launch", desc="all launchable applications")
ctx = Context()

# a list of the current overrides
overrides = {"term": "Alacritty"}

# a list of the currently running application names
running_application_dict = {}


words_to_exclude = [
    "zero",
    "one",
    "two",
    "three",
    "for",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "and",
    "dot",
    "exe",
    "help",
    "install",
    "installer",
    "microsoft",
    "nine",
    "readme",
    "studio",
    "terminal",
    "visual",
    "windows",
]


@mod.capture(rule="{self.running}")  # | <user.text>)")
def running_applications(m) -> str:
    "Returns a single application name"
    try:
        return m.running
    except AttributeError:
        return m.text


@mod.capture(rule="{self.launch}")
def launch_applications(m) -> str:
    "Returns a single application name"
    return m.launch


def update_running_list():
    global running_application_dict
    running_application_dict = {}
    running = {}
    for cur_app in ui.apps(background=False):
        running_application_dict[cur_app.name] = True

        if app.platform == "windows":
            # print("hit....")
            # print(cur_app.exe)
            running_application_dict[cur_app.exe.split(os.path.sep)[-1]] = True

    running = actions.user.create_spoken_forms_from_list(
        [curr_app.name for curr_app in ui.apps(background=False)],
        words_to_exclude=words_to_exclude,
        generate_subsequences=True,
    )

    # print(str(running_application_dict))
    # todo: should the overrides remove the other spoken forms for an application?
    for override in overrides:
        if overrides[override] in running_application_dict:
            running[override] = overrides[override]

    lists = {
        "self.running": running,
    }

    # batch update lists
    ctx.lists.update(lists)


@mod.action_class
class Actions:
    def get_running_app(name: str) -> ui.App:
        """Get the first available running app with `name`."""
        # We should use the capture result directly if it's already in the list
        # of running applications. Otherwise, name is from <user.text> and we
        # can be a bit fuzzier
        if name not in running_application_dict:
            if len(name) < 3:
                raise RuntimeError(
                    f'Skipped getting app: "{name}" has less than 3 chars.'
                )
            for running_name, full_application_name in ctx.lists[
                "self.running"
            ].items():
                if running_name == name or running_name.lower().startswith(
                    name.lower()
                ):
                    name = full_application_name
                    break
        for application in ui.apps(background=False):
            if application.name == name or (
                app.platform == "windows"
                and application.exe.split(os.path.sep)[-1] == name
            ):
                return application
        raise RuntimeError(f'App not running: "{name}"')

    def switcher_focus(name: str):
        """Focus a new application by name"""
        app = actions.user.get_running_app(name)
        actions.user.switcher_focus_app(app)

    def switcher_focus_app(app: ui.App):
        """Focus application and wait until switch is made"""
        app.focus()
        t1 = time.monotonic()
        while ui.active_app() != app:
            if time.monotonic() - t1 > 1:
                raise RuntimeError(f"Can't focus app: {app.name}")
            actions.sleep(0.1)

    def switcher_focus_window(window: ui.Window):
        """Focus window and wait until switch is made"""
        window.focus()
        t1 = time.monotonic()
        while ui.active_window() != window:
            if time.monotonic() - t1 > 1:
                raise RuntimeError(f"Can't focus window: {window.title}")
            actions.sleep(0.1)

    def switcher_launch(path: str):
        """Launch a new application by path"""
        ui.launch(path=path)

    def switcher_menu():
        """Open a menu of running apps to switch to"""
        if app.platform == "windows":
            actions.key("alt-ctrl-tab")
        else:
            print("Persistent Switcher Menu not supported on " + app.platform)

    def switcher_toggle_running():
        """Shows/hides all running applications"""
        if gui_running.showing:
            gui_running.hide()
        else:
            gui_running.show()

    def switcher_hide_running():
        """Hides list of running applications"""
        gui_running.hide()


@imgui.open()
def gui_running(gui: imgui.GUI):
    gui.text("Names of running applications")
    gui.line()
    for line in ctx.lists["self.running"]:
        gui.text(line)

    gui.spacer()
    if gui.button("Running close"):
        actions.user.switcher_hide_running()


def ui_event(event, arg):
    if event in ("app_launch", "app_close"):
        update_running_list()


ctx.lists["user.launch"] = {}
ctx.lists["user.running"] = {}

# Talon starts faster if you don't use the `talon.ui` module during launch


def on_ready():
    update_running_list()
    ui.register("", ui_event)


app.register("ready", on_ready)
