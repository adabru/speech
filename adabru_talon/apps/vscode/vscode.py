from talon import Context, actions, ui, Module, app, clip

is_mac = app.platform == "mac"

ctx = Context()
mod = Module()
mod.apps.vscode = """
app.exe: code-oss
app.exe: code-insiders
"""

ctx.matches = r"""
app: vscode
"""


@ctx.action_class("app")
class AppActions:
    # talon app actions
    def window_close():
        actions.user.vscode("workbench.action.closeWindow")

    def window_open():
        actions.user.vscode("workbench.action.newWindow")


@ctx.action_class("code")
class CodeActions:
    # talon code actions
    def toggle_comment():
        actions.user.vscode("editor.action.commentLine")


@ctx.action_class("win")
class WinActions:
    def filename():
        title = actions.win.title()
        # this doesn't seem to be necessary on VSCode for Mac
        # if title == "":
        #    title = ui.active_window().doc

        if is_mac:
            result = title.split(" — ")[0]
        else:
            result = title.split(" - ")[0]

        if "." in result:
            return result

        return ""


@mod.action_class
class Actions:
    def jump_line(n: int):
        """Go to a specific line in file"""
        actions.user.vscode("workbench.action.gotoLine")
        actions.insert(str(n))
        actions.key("enter")

    def vscode_terminal(number: int):
        """Activate a terminal by number"""
        actions.user.vscode(f"workbench.action.terminal.focusAtIndex{number}")

    def command_palette():
        """Show command palette"""
        actions.key("alt-space")

    def select_range(line_start: int, line_end: int):
        """Selects lines from line_start to line line_end"""
        actions.user.jump_line(line_start)

        number_of_lines = line_end - line_start + 1
        for i in range(0, number_of_lines):
            actions.key("shift-down")

    # snippet.py support begin
    def snippet_insert(text: str):
        """Inserts a snippet"""
        actions.user.vscode("editor.action.insertSnippet")
        actions.insert(text)
        actions.key("enter")

    def snippet_create():
        """Triggers snippet creation"""
        actions.user.vscode("workbench.action.openSnippets")

    # snippet.py support end

    # find_and_replace.py support begin

    def find_everywhere(text: str):
        """Triggers find across project"""
        actions.key("ctrl-shift-f")
        actions.insert(text)

    def find_toggle_match_by_case():
        """Toggles find match by case sensitivity"""
        actions.key("alt-c")

    def find_toggle_match_by_word():
        """Toggles find match by whole words"""
        actions.key("alt-w")

    def find_toggle_match_by_regex():
        """Toggles find match by regex"""
        actions.key("alt-r")

    def replace(text: str):
        """Search and replaces in the active editor"""
        actions.key("ctrl-h")
        if text:
            actions.insert(text)

    def replace_everywhere(text: str):
        """Search and replaces in the entire project"""
        actions.key("ctrl-shift-h")
        if text:
            actions.insert(text)

    def replace_confirm():
        """Confirm replace at current position"""
        actions.key("ctrl-shift-1")

    def replace_confirm_all():
        """Confirm replace all"""
        actions.key("ctrl-alt-enter")
