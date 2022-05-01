# keyboard keys = low level
<user.arrow_keys>: key(arrow_keys)
<user.function_key>: key(function_key)
<user.special_key>: key(special_key)
<user.modifiers> <user.unmodified_key>: key("{modifiers}-{unmodified_key}")
press <user.modifiers>: key(modifiers)

let$: skip()
let <user.letter>+$: user.insert_many(letter_list)
step <user.letters>: user.insert_formatted(letters, "ALL_CAPS")
sym$: skip()
sym <user.symbol_key>*$: user.insert_many(symbol_key_list)
num <user.number_string>: "{number_string}"

# repeat commands
# <number>: core.repeat_command(number)
<user.single_digit> hi: core.repeat_command(single_digit)
hi: core.repeat_command(1)

bottom:key("ctrl-end")
shottom:key("shift-ctrl-end")
tip:key("ctrl-home")
ship:key("shift-ctrl-home")
kace: key("ctrl-del")
kipe: key("ctrl-backspace")
sheft: key("shift-left")
shite: key("shift-right")
shkeft: key("ctrl-shift-left")
shkite: key("ctrl-shift-right")
keft: key("ctrl-left")
kite: key("ctrl-right")
shart: key("shift-home")
shend: key("shift-end")
shunder: key("shift-down")
shup: key("shift-up")

# shortened punctuation
somma: ", "
soint: ". "
sest: "? "
sang: "! "
solon: ": "
sequals: "= "
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

#  window management
window close: key('alt-f4')
full screen: key('f11')
snap <user.window_snap_position>: user.snap_window(window_snap_position)
snap next [screen]: user.move_window_next_screen()
snap last [screen]: user.move_window_previous_screen()
snap screen <number>: user.move_window_to_screen(number)
snap <user.running_applications> <user.window_snap_position>:
    user.snap_app(running_applications, window_snap_position)
snap <user.running_applications> [screen] <number>:
    user.move_app_to_screen(running_applications, number)


# see https://forum.vivaldi.net/topic/30413/password-for-keyring-solved/20
launch web: user.system_launch("vivaldi-stable --password-store=basic")
fogy web: user.focus_window("vivaldi-stable")
launch term: user.system_launch("alacritty --class tmux -e tmux")
fogy term: user.focus_window("tmux")
launch code: user.system_launch("code-insiders /home/adabru/.cache/vscode-default/default.code-workspace")
fogy code: user.focus_window("code - insiders")
launch steps: user.system_launch('sh -c "featherpad -w /home/adabru/👣/*"')
fogy steps: user.focus_window('featherpad')
to dos: user.switch_app('todo', 'sh -c "alacritty -t Todo --class todo -e vim ~/s"')
launch mail: user.system_launch('thunderbird')
fogy mail: user.focus_window('Thunderbird')
launch$: user.system_start("albert toggle")
fogy debug: user.print_debug()

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
brightness max: user.system_exec("brillo -S 100")

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
flag <user.letter>+$:
  "-"
  user.insert_many(letter_list)
word <user.word>: user.insert_formatted(user.word, "NOOP")
recent list: user.toggle_phrase_history()
recent close: user.phrase_history_hide()
recent repeat <number_small>: insert(user.get_recent_phrase(number_small))
recent copy <number_small>: clip.set_text(user.get_recent_phrase(number_small))
select that: user.select_last_phrase()
before that: user.before_last_phrase()
nope that | scratch that: user.clear_last_phrase()
nope that was <user.formatters>: user.formatters_reformat_last(formatters)

dentence: user.german_sentence()
dords: user.german_words()
doytation: user.german_dictation()
dictation up: user.german_dictionary_add()
dictation low: user.german_dictionary_add()

# allows you to prevent a command executing by ending it with "cancel"
ignore$: skip()
# the actual behavior of "cancel" is implemented in code/cancel.py; if you want to use a different phrase you must also change cancel_phrase there.

# allows you to say something (eg to a human) that you don't want talon to hear, eg "ignore hey Jerry"
ignore [<phrase>]$: app.notify("Command ignored")

# web
open {user.website}: user.open_url(website)
{user.search_engine} hunt <user.text>$: user.search_with_search_engine(search_engine, user.text)
{user.search_engine} (that|this):
    text = edit.selected_text()
    user.search_with_search_engine(search_engine, text)

# system
system force poweroff: user.system_exec("poweroff")
system force reboot: user.system_exec("reboot")
system force suspend: user.system_exec("systemctl suspend")

chat ready: "I am ready\n"
chat yes: "Yes 👍\n"
chat ok: "ok\n"

start eye record: user.start_eye_record()
stop eye record: user.end_eye_record()
