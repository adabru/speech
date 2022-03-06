# keyboard keys = low level
<user.arrow_keys>: key(arrow_keys)
<user.function_key>: key(function_key)
<user.special_key>: key(special_key)
<user.modifiers> <user.unmodified_key>: key("{modifiers}-{unmodified_key}")
press <user.modifiers>: key(modifiers)

let$: skip()
let <user.letter>+$: user.insert_many(letter_list)
ship <user.letters>: user.insert_formatted(letters, "ALL_CAPS")
sym$: skip()
sym <user.symbol_key>*$: user.insert_many(symbol_key_list)
num <user.number_string>: "{number_string}"

# repeat commands
# <user.number_string>: skip()
<number>: core.repeat_command(number)
ho: core.repeat_command(1)

bottom:key("ctrl-end")
shottom:key("shift-ctrl-end")
top:key("ctrl-home")
shop:key("shift-ctrl-home")
sheft: key("shift-left")
shight: key("shift-right")
shart: key("shift-home")
shend: key("shift-end")
shown: key("shift-down")
shup: key("shift-up")

# shortened punctuation
spamma: ", "
spoint: ". "
spest: "? "
spang: "! "
spolon: ": "
sym new line: "\\n"
sym carriage return: "\\r"
sym line feed: "\\r\\n"

# universal shortcuts
zoom in: key(ctrl-+)
zoom out: key(ctrl--)
zoom reset: key(ctrl-0)
copy: key(ctrl-c)
copy all: key(ctrl-a ctrl-c)
cut: key(ctrl-x)
cut all: key(ctrl-a ctrl-x)
paste: key(ctrl-v)
ipe all: key(ctrl-a delete)
undo: key(ctrl-z)
redo: key(ctrl-y)
paste match: edit.paste_match_style()
[file] ok: key(ctrl-s)
find$: key(ctrl-f)
find <user.text>$:
    key(ctrl-f)
    sleep(.15)
    insert(text)
lipe: key(home shift-down delete)
lopy: key(home shift-down ctrl-c)
line cut: key(home shift-down ctrl-x)
con sheft: key(shift-ctrl-left)
con shite: key(shift-ctrl-right)

#  window management
window close: key('alt-f4')
fogy <user.running_applications>: user.switcher_focus(running_applications)
running list: user.switcher_toggle_running()
running close: user.switcher_hide_running()
# launch <user.launch_applications>: user.switcher_launch(launch_applications)
snap <user.window_snap_position>: user.snap_window(window_snap_position)
snap next [screen]: user.move_window_next_screen()
snap last [screen]: user.move_window_previous_screen()
snap screen <number>: user.move_window_to_screen(number)
snap <user.running_applications> <user.window_snap_position>:
    user.snap_app(running_applications, window_snap_position)
snap <user.running_applications> [screen] <number>:
    user.move_app_to_screen(running_applications, number)

launch web: user.systems_start("vivaldi-stable")
launch term: user.systems_start("alacritty -e tmux")
launch code: user.systems_start("code-insiders /home/adabru/.cache/vscode-default/default.code-workspace")
launch steps: user.systems_start('sh -c "featherpad -w /home/adabru/👣/*"')
launch mail: user.systems_start('thunderbird')
launch$: user.systems_start("albert toggle")

# virtual desktops
desk right: key(ctrl-alt-right)
desk move right: key(ctrl-alt-end)
desk left: key(ctrl-alt-left)
desk move left: key(ctrl-alt-home)

screen rotate left: user.system_exec("xrandr -o left")
screen rotate right: user.system_exec("xrandr -o right")
screen rotate inverted: user.system_exec("xrandr -o inverted")
screen rotate normal: user.system_exec("xrandr -o normal")

# media keys
volume up: user.system_exec("pactl set-sink-volume 0 +10%")
volume down: user.system_exec("pactl set-sink-volume 0 -10%")
volume <number>: user.system_exec("pactl set-sink-volume 0 {number}%")
volume mute: user.system_exec("pactl set-sink-mute @DEFAULT_SINK@ toggle")
[media] play next: key(next)
[media] play previous: key(prev)
media (play | pause): key(play)

# brightness
brightness up: user.system_exec("brillo -A 10")
brightness down: user.system_exec("brillo -U 10")
brightness <number>: user.system_exec("brillo -S {number}")
brightness dot <number>: user.system_exec("brillo -S .{number}")

# macro
macro record: user.macro_record()
macro stop: user.macro_stop()
macro play: user.macro_play()

# screenshot
^grab screen$:                       user.screenshot()
^grab screen <number_small>$:        user.screenshot(number_small)
^grab window$:                       user.screenshot_window()
^grab selection$:                    user.screenshot_selection()
^grab screen clip$:                  user.screenshot_clipboard()
^grab screen <number_small> clip$:   user.screenshot_clipboard(number_small)
^grab window clip$:                  user.screenshot_window_clipboard()

# multiple screens
screen numbers:   user.screens_show_numbering()

# microphone selection
^microphone show$: user.microphone_selection_toggle()
^microphone close$: user.microphone_selection_hide()
^microphone pick <number_small>$: user.microphone_select(number_small)

# command history
command history: user.history_toggle()
command history close: user.history_disable()
command history clear: user.history_clear()
command history less: user.history_less()
command history more: user.history_more()

# file extensions
{user.file_extension}: "{file_extension}"

# text insertions
date insert:
    insert(user.time_format("%Y-%m-%d"))
date insert UTC:
    insert(user.time_format_utc("%Y-%m-%d"))
timestamp insert:
    insert(user.time_format("%Y-%m-%d %H:%M:%S"))
timestamp insert high resolution:
    insert(user.time_format("%Y-%m-%d %H:%M:%S.%f"))
timestamp insert UTC:
    insert(user.time_format_utc("%Y-%m-%d %H:%M:%S"))
timestamp insert UTC high resolution:
    insert(user.time_format_utc("%Y-%m-%d %H:%M:%S.%f"))
brief {user.abbreviation}: "{abbreviation}"
#(jay son | jason ): "json"
#(http | htp): "http"
#M D five: "md5"
#word (regex | rejex): "regex"

talon fast: user.make_fast()
talon slow: user.make_slow()
wheel pop: user.enable_wheel_pop()

# dictation
phrase <user.text>$: user.insert_formatted(text, "NOOP")
phrase <user.text> over: user.insert_formatted(text, "NOOP")
say <user.prose>$: user.insert_formatted(prose, "NOOP")
sauce <user.prose>$:
    user.insert_formatted(prose, "NOOP")
    " "
say$: skip()
stay <user.prose>$: user.insert_formatted(prose, "CAPITALIZE_FIRST_WORD")
stay$: skip()
<user.format_text>+$: user.insert_many(format_text_list)
<user.format_text>+ over: user.insert_many(format_text_list)
<user.formatters> that: user.formatters_reformat_selection(user.formatters)
word <user.word>: user.insert_formatted(user.word, "NOOP")
recent list: user.toggle_phrase_history()
recent close: user.phrase_history_hide()
recent repeat <number_small>: insert(user.get_recent_phrase(number_small))
recent copy <number_small>: clip.set_text(user.get_recent_phrase(number_small))
select that: user.select_last_phrase()
before that: user.before_last_phrase()
nope that | scratch that: user.clear_last_phrase()
nope that was <user.formatters>: user.formatters_reformat_last(formatters)

# allows you to prevent a command executing by ending it with "cancel"
cancel$: skip()
# the actual behavior of "cancel" is implemented in code/cancel.py; if you want to use a different phrase you must also change cancel_phrase there.

# allows you to say something (eg to a human) that you don't want talon to hear, eg "ignore hey Jerry"
ignore [<phrase>]$: app.notify("Command ignored")

# web
open {user.website}: user.open_url(website)
{user.search_engine} hunt <user.text>$: user.search_with_search_engine(search_engine, user.text)
{user.search_engine} (that|this):
    text = edit.selected_text()
    user.search_with_search_engine(search_engine, text)
