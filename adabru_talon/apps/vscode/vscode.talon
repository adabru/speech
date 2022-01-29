#custom vscode commands go here
app: vscode
-

tag(): user.snippets
window reload: user.vscode("workbench.action.reloadWindow")
window close: user.vscode("workbench.action.closeWindow")
#multiple_cursor.py support end

please [<user.text>]:
    user.vscode("workbench.action.showCommands")
    insert(user.text or "")

# Sidebar
bar explore: user.vscode("workbench.view.explorer")
bar extensions: user.vscode("workbench.view.extensions")
bar outline: user.vscode("outline.focus")
bar run: user.vscode("workbench.view.debug")
bar search: user.vscode("workbench.view.search")
bar source: user.vscode("workbench.view.scm")
bar switch: user.vscode("workbench.action.toggleSidebarVisibility")

symbol hunt [<user.text>]:
    user.vscode("workbench.action.gotoSymbol")
    sleep(50ms)
    insert(text or "")

# Panels
panel control: user.vscode("workbench.panel.repl.view.focus")
panel output: user.vscode("workbench.panel.output.focus")
panel problems: user.vscode("workbench.panel.markers.view.focus")
panel switch: user.vscode("workbench.action.togglePanel")
panel terminal: user.vscode("workbench.action.terminal.focus")
focus editor: user.vscode("workbench.action.focusActiveEditorGroup")

# Settings
show settings: user.vscode("workbench.action.openGlobalSettings")
show shortcuts: user.vscode("workbench.action.openGlobalKeybindings")
show snippets: user.vscode("workbench.action.openSnippets")

# Display
centered switch: user.vscode("workbench.action.toggleCenteredLayout")
fullscreen switch: user.vscode("workbench.action.toggleFullScreen")
theme switch: user.vscode("workbench.action.selectTheme")
wrap switch: user.vscode("editor.action.toggleWordWrap")
zen switch: user.vscode("workbench.action.toggleZenMode")

# File Commands
file hunt [<user.text>]:
    user.vscode("workbench.action.quickOpen")
    sleep(50ms)
    insert(text or "")
file copy path: user.vscode("copyFilePath")
file create sibling: user.vscode_and_wait("explorer.newFile")
file create: user.vscode("workbench.action.files.newUntitledFile")
file rename:
    user.vscode("fileutils.renameFile")
    sleep(150ms)
file move:
    user.vscode("fileutils.moveFile")
    sleep(150ms)
file open folder: user.vscode("revealFileInOS")
file reveal: user.vscode("workbench.files.action.showActiveFileInExplorer")
save ugly: user.vscode("workbench.action.files.saveWithoutFormatting")

# Language Features
suggest show: user.vscode("editor.action.triggerSuggest")
hint show: user.vscode("editor.action.triggerParameterHints")
definition show: user.vscode("editor.action.revealDefinition")
definition peek: user.vscode("editor.action.peekDefinition")
definition side: user.vscode("editor.action.revealDefinitionAside")
references show: user.vscode("editor.action.goToReferences")
references find: user.vscode("references-view.find")
format that: user.vscode("editor.action.formatDocument")
format selection: user.vscode("editor.action.formatSelection")
imports fix: user.vscode("editor.action.organizeImports")
problem next: user.vscode("editor.action.marker.nextInFiles")
problem last: user.vscode("editor.action.marker.prevInFiles")
problem fix: user.vscode("problems.action.showQuickFixes")
rename that: user.vscode("editor.action.rename")
refactor that: user.vscode("editor.action.refactor")
whitespace trim: user.vscode("editor.action.trimTrailingWhitespace")
language switch: user.vscode("workbench.action.editor.changeLanguageMode")
refactor rename: user.vscode("editor.action.rename")
refactor this: user.vscode("editor.action.refactor")

#code navigation
(go declaration | follow): user.vscode("editor.action.revealDefinition")
go back: user.vscode("workbench.action.navigateBack")
go forward: user.vscode("workbench.action.navigateForward")
go implementation: user.vscode("editor.action.goToImplementation")
go type: user.vscode("editor.action.goToTypeDefinition")
go usage: user.vscode("references-view.find")
go recent [<user.text>]:
    user.vscode("workbench.action.openRecent")
    sleep(50ms)
    insert(text or "")
    sleep(250ms)

# Bookmarks. Requires Bookmarks plugin
go marks: user.vscode("workbench.view.extension.bookmarks")
toggle mark: user.vscode("bookmarks.toggle")
go next mark: user.vscode("bookmarks.jumpToNext")
go last mark: user.vscode("bookmarks.jumpToPrevious")

# Folding
fold that: user.vscode("editor.fold")
unfold that: user.vscode("editor.unfold")
fold those: user.vscode("editor.foldAllMarkerRegions")
unfold those: user.vscode("editor.unfoldRecursively")
fold all: user.vscode("editor.foldAll")
unfold all: user.vscode("editor.unfoldAll")
fold comments: user.vscode("editor.foldAllBlockComments")

# Git / Github (not using verb-noun-adjective pattern, mirroring terminal commands.)
git branch: user.vscode("git.branchFrom")
git branch this: user.vscode("git.branch")
git checkout [<user.text>]:
    user.vscode("git.checkout")
    sleep(50ms)
    insert(text or "")
git commit [<user.text>]:
    user.vscode("git.commitStaged")
    sleep(100ms)
    user.insert_formatted(text or "", "CAPITALIZE_FIRST_WORD")
git commit undo: user.vscode("git.undoCommit")
git commit ammend: user.vscode("git.commitStagedAmend")
git diff: user.vscode("git.openChange")
git ignore: user.vscode("git.ignore")
git merge: user.vscode("git.merge")
git output: user.vscode("git.showOutput")
git pull: user.vscode("git.pullRebase")
git push: user.vscode("git.push")
git push focus: user.vscode("git.pushForce")
git rebase abort: user.vscode("git.rebaseAbort")
git reveal: user.vscode("git.revealInExplorer")
git revert: user.vscode("git.revertChange")
git stash: user.vscode("git.stash")
git stash pop: user.vscode("git.stashPop")
git status: user.vscode("workbench.scm.focus")
git stage: user.vscode("git.stage")
git stage all: user.vscode("git.stageAll")
git unstage: user.vscode("git.unstage")
git unstage all: user.vscode("git.unstageAll")
pull request: user.vscode("pr.create")
change next: key(alt-f5)
change last: key(shift-alt-f5)

#Debugging
break point: user.vscode("editor.debug.action.toggleBreakpoint")
step over: user.vscode("workbench.action.debug.stepOver")
debug step into: user.vscode("workbench.action.debug.stepInto")
debug step out [of]: user.vscode("workbench.action.debug.stepOut")
debug start: user.vscode("workbench.action.debug.start")
debug pause: user.vscode("workbench.action.debug.pause")
debug stopper: user.vscode("workbench.action.debug.stop")
debug continue: user.vscode("workbench.action.debug.continue")
debug restart: user.vscode("workbench.action.debug.restart")
debug console: user.vscode("workbench.debug.action.toggleRepl")

# Terminal
terminal external: user.vscode("workbench.action.terminal.openNativeConsole")
terminal new: user.vscode("workbench.action.terminal.new")
terminal next: user.vscode("workbench.action.terminal.focusNext")
terminal last: user.vscode("workbench.action.terminal.focusPrevious")
terminal split: user.vscode("workbench.action.terminal.split")
terminal zoom: user.vscode("workbench.action.toggleMaximizedPanel")
terminal trash: user.vscode("workbench.action.terminal.kill")
terminal toggle: user.vscode_and_wait("workbench.action.terminal.toggleTerminal")
terminal scroll up: user.vscode("workbench.action.terminal.scrollUp")
terminal scroll down: user.vscode("workbench.action.terminal.scrollDown")
terminal <number_small>: user.vscode_terminal(number_small)

#Expand/Shrink AST Selection
select less: user.vscode("editor.action.smartSelect.shrink")
select (more|this): user.vscode("editor.action.smartSelect.expand")

minimap: user.vscode("editor.action.toggleMinimap")
maximize: user.vscode("workbench.action.minimizeOtherEditors")
restore: user.vscode("workbench.action.evenEditorWidths")

replace here:
    user.replace("")
    key(cmd-alt-l)

hover show: user.vscode("editor.action.showHover")

join lines: user.vscode("editor.action.joinLines")

full screen: user.vscode("workbench.action.toggleFullScreen")

curse undo: user.vscode("cursorUndo")

select word: user.vscode("editor.action.addSelectionToNextFindMatch")
skip word: user.vscode("editor.action.moveSelectionToNextFindMatch")

# jupyter
cell next: user.vscode("jupyter.gotoNextCellInFile")
cell last: user.vscode("jupyter.gotoPrevCellInFile")
cell run above: user.vscode("jupyter.runallcellsabove.palette")
cell run: user.vscode("jupyter.runcurrentcell")

install local: user.vscode("workbench.extensions.action.installVSIX")


# multi cursor
cursor stop: key("escape")
cursor up: user.vscode("editor.action.insertCursorAbove")
cursor down: user.vscode("editor.action.insertCursorBelow")
cursor less: user.vscode("cursorUndo")
cursor more: user.vscode("editor.action.addSelectionToNextFindMatch")
cursor skip: user.vscode("editor.action.moveSelectionToNextFindMatch")
cursor all: user.vscode("editor.action.selectHighlights")
cursor lines: user.vscode("editor.action.insertCursorAtEndOfEachLineSelected")

# pane splitting
split right: user.vscode("workbench.action.moveEditorToRightGroup")
split left: user.vscode("workbench.action.moveEditorToLeftGroup")
split down: user.vscode("workbench.action.moveEditorToBelowGroup")
split up: user.vscode("workbench.action.moveEditorToAboveGroup")
split (vertically | vertical): user.vscode("workbench.action.splitEditor")
split (horizontally | horizontal): user.vscode("workbench.action.splitEditorOrthogonal")
split flip: user.vscode("workbench.action.toggleEditorGroupLayout")
split window: user.vscode("workbench.action.splitEditor")
split clear: user.vscode("workbench.action.joinTwoGroups")
split clear all: user.vscode("workbench.action.editorLayoutSingle")
split next: user.vscode_and_wait("workbench.action.focusRightGroup")
split last: user.vscode("workbench.action.focusLeftGroup")
go split <number>: key(ctrl-number)

# block commands
block comment <number> through <number>:
    user.select_range(number_1, number_2)
    code.toggle_comment()
block clear <number> through <number>:
    user.select_range(number_1, number_2)
    edit.delete()
block copy <number> through <number>:
    user.select_range(number_1, number_2)
    edit.copy()
block cut <number> through <number>:
    user.select_range(number_1, number_2)
    edit.cut()
block replace <number> through <number>:
    user.select_range(number_1, number_2)
    edit.paste()
block <number> through <number>: user.select_range(number_1, number_2)
block indent <number> through <number>:
    user.select_range(number_1, number_2)
    user.vscode("editor.action.indentLines")
block outdent <number> through <number>:
    user.select_range(number_1, number_2)
    user.vscode("editor.action.outdentLines")
block clone <number> through <number>:
    user.select_range(number_1, number_2)
    user.vscode("editor.action.copyLinesDownAction")


# line commands
line copy down: user.vscode("editor.action.copyLinesDownAction")
line copy up: user.vscode("editor.action.copyLinesUpAction")
line <number>: edit.jump_line(number)
line <number> end:
    edit.jump_line(number)
    edit.line_end()
line comment <number>:
    user.select_range(number, number)
    code.toggle_comment()
line clear <number>:
    edit.jump_line(number)
    user.vscode("editor.action.deleteLines")
line clear:
    user.vscode("editor.action.deleteLines")
line copy <number>:
    user.select_range(number, number)
    edit.copy()
line cut <number>:
    user.select_range(number, number)
    edit.cut()
line select <number>: user.select_range(number, number)
line clone: user.vscode("editor.action.copyLinesDownAction")
line indent: user.vscode("editor.action.indentLines")
line indent <number>:
    edit.jump_line(number)
    user.vscode("editor.action.indentLines")
line outdent: user.vscode("editor.action.outdentLines")
line outdent <number>:
    edit.jump_line(number)
    user.vscode("editor.action.outdentLines")
line down: edit.line_swap_down()
line up: edit.line_swap_up()

# find and replace
find: user.find("")
find <user.text>: user.find(text)
find all: user.find_everywhere("")
find all <user.text>: user.find_everywhere(text)
find case : user.find_toggle_match_by_case()
find word : user.find_toggle_match_by_word()
find expression : user.find_toggle_match_by_regex()
find next: actions.user.vscode("editor.action.nextMatchFindAction")
find previous: actions.user.vscode("editor.action.previousMatchFindAction")
replace this [<user.text>]: user.replace(text or "")
replace all: user.replace_everywhere("")
replace <user.text> all: user.replace_everywhere(text)
replace confirm that: user.replace_confirm()
replace confirm all: user.replace_confirm_all()

#quick replace commands, modeled after jetbrains
clear last <user.text> [over]:
    user.select_previous_occurrence(text)
    sleep(100ms)
    edit.delete()
clear next <user.text> [over]:
    user.select_next_occurrence(text)
    sleep(100ms)
    edit.delete()
clear last clip:
    user.select_previous_occurrence(clip.text())
    edit.delete()
clear next clip:
    user.select_next_occurrence(clip.text())
    sleep(100ms)
    edit.delete()
comment last <user.text> [over]:
    user.select_previous_occurrence(text)
    sleep(100ms)
    code.toggle_comment()
comment last clip:
    user.select_previous_occurrence(clip.text())
    sleep(100ms)
    code.toggle_comment()
comment next <user.text> [over]:
    user.select_next_occurrence(text)
    sleep(100ms)
    code.toggle_comment()
comment next clip:
    user.select_next_occurrence(clip.text())
    sleep(100ms)
    code.toggle_comment()
go last <user.text> [over]:
    user.select_previous_occurrence(text)
    sleep(100ms)
    edit.right()
go last clip:
    user.select_previous_occurrence(clip.text())
    sleep(100ms)
    edit.right()
go next <user.text> [over]:
    user.select_next_occurrence(text)
    edit.right()
go next clip:
    user.select_next_occurrence(clip.text())
    edit.right()
paste last <user.text> [over]:
    user.select_previous_occurrence(text)
    sleep(100ms)
    edit.right()
    edit.paste()
paste next <user.text> [over]:
    user.select_next_occurrence(text)
    sleep(100ms)
    edit.right()
    edit.paste()
replace last <user.text> [over]:
    user.select_previous_occurrence(text)
    sleep(100ms)
    edit.paste()
replace next <user.text> [over]:
    user.select_next_occurrence(text)
    sleep(100ms)
    edit.paste()
select last <user.text> [over]: user.select_previous_occurrence(text)
select next <user.text> [over]: user.select_next_occurrence(text)
select last clip: user.select_previous_occurrence(clip.text())
select next clip: user.select_next_occurrence(clip.text())

# tabs
tab left: user.vscode("workbench.action.previousEditor")
tab right: user.vscode("workbench.action.nextEditor")
tab close: user.vscode("workbench.action.closeActiveEditor")
tab (reopen|restore): user.vscode("workbench.action.reopenClosedEditor")
tab one: user.vscode("workbench.action.openEditorAtIndex1")
tab two: user.vscode("workbench.action.openEditorAtIndex2")
tab three: user.vscode("workbench.action.openEditorAtIndex3")
tab four: user.vscode("workbench.action.openEditorAtIndex4")
tab five: user.vscode("workbench.action.openEditorAtIndex5")
tab six: user.vscode("workbench.action.openEditorAtIndex6")
tab seven: user.vscode("workbench.action.openEditorAtIndex7")
tab eight: user.vscode("workbench.action.openEditorAtIndex8")
tab nine: user.vscode("workbench.action.openEditorAtIndex9")
# user.vscode_with_plugin(f"workbench.action.openEditorAtIndex{number}")
tab final: user.vscode("workbench.action.lastEditorInGroup")
