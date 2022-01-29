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
    def tab_open():
        actions.user.vscode("workbench.action.files.newUntitledFile")

    def tab_close():
        actions.user.vscode("workbench.action.closeActiveEditor")

    def tab_next():
        actions.user.vscode("workbench.action.nextEditorInGroup")

    def tab_previous():
        actions.user.vscode("workbench.action.previousEditorInGroup")

    def tab_reopen():
        actions.user.vscode("workbench.action.reopenClosedEditor")

    def window_close():
        actions.user.vscode("workbench.action.closeWindow")

    def window_open():
        actions.user.vscode("workbench.action.newWindow")


@ctx.action_class("code")
class CodeActions:
    # talon code actions
    def toggle_comment():
        actions.user.vscode("editor.action.commentLine")


@ctx.action_class("edit")
class EditActions:
    # talon edit actions
    def indent_more():
        actions.user.vscode("editor.action.indentLines")

    def indent_less():
        actions.user.vscode("editor.action.outdentLines")

    def save_all():
        actions.user.vscode("workbench.action.files.saveAll")

    def find(text=None):
        if is_mac:
            actions.key("cmd-f")
        else:
            actions.key("ctrl-f")
        if text is not None:
            actions.insert(text)

    def line_swap_up():
        actions.key("alt-up")

    def line_swap_down():
        actions.key("alt-down")

    def line_clone():
        actions.key("shift-alt-down")

    def jump_line(n: int):
        actions.user.vscode("workbench.action.gotoLine")
        actions.insert(str(n))
        actions.key("enter")


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
    def vscode_terminal(number: int):
        """Activate a terminal by number"""
        actions.user.vscode(f"workbench.action.terminal.focusAtIndex{number}")

    def command_palette():
        """Show command palette"""
        actions.key("alt-space")

    def select_range(line_start: int, line_end: int):
        """Selects lines from line_start to line line_end"""
        actions.edit.jump_line(line_start)

        number_of_lines = line_end - line_start + 1
        for i in range(0, number_of_lines):
            actions.edit.extend_line_down()

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

    def find(text: str):
        """Triggers find in current editor"""
        actions.key("ctrl-f")
        actions.insert(text)

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
