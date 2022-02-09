# keyboard keys = low level
<user.arrow_keys>: key(arrow_keys)
bottom:key("ctrl-end")
shif bottom:key("shift-ctrl-end")
top:key("ctrl-home")
shif top:key("shift-ctrl-home")

<user.letter>: key(letter)
(ship | uppercase) <user.letters> [(lowercase | sunk)]:
    user.insert_formatted(letters, "ALL_CAPS")
<user.symbol_key>: key(symbol_key)
<user.function_key>: key(function_key)
<user.special_key>: key(special_key)
<user.modifiers> <user.unmodified_key>: key("{modifiers}-{unmodified_key}")
press <user.modifiers>: key(modifiers)

# universal shortcuts
zoom in: key(ctrl-+)
zoom out: key(ctrl--)
zoom reset: key(ctrl-0)
copy: key(ctrl-c)
copy all: key(ctrl-a ctrl-c)
cut: key(ctrl-x)
cut all: key(ctrl-a ctrl-x)
paste: key(ctrl-v)
wipe up: key(shift-up delete)
wipe down: key(shift-down delete)
wipe all: key(ctrl-a delete)
undo: key(ctrl-z)
redo: key(ctrl-y)
paste match: edit.paste_match_style()
[file] save: key(ctrl-s)
find$: key(ctrl-f)
find <user.text>$:
    key(ctrl-f)
    sleep(.15)
    insert(text)
line wipe: key(home shift-down delete)
line copy: key(home shift-down ctrl-c)
line cut: key(home shift-down ctrl-x)
word select: key(right ctrl-left shift-ctrl-right)
word copy: key(right ctrl-left shift-ctrl-right ctrl-c)
word cut: key(right ctrl-left shift-ctrl-right ctrl-x)
word left: key(ctrl-left)
word right: key(ctrl-right)
shif word left: key(shift-ctrl-left)
shif word right: key(shift-ctrl-right)
word wipe: key(ctrl-backspace)
word race: key(ctrl-delete)
word wipe race: key(ctrl-backspace ctrl-delete)


# repeat commands
<user.ordinals>: core.repeat_command(ordinals-1)
<number_small> times: core.repeat_command(number_small-1)
twice | again: core.repeat_command(1)

#  window management
window (new|open): app.window_open()
window next: app.window_next()
window last: app.window_previous()
window close: app.window_close()
focus <user.running_applications>: user.switcher_focus(running_applications)
running list: user.switcher_toggle_running()
running close: user.switcher_hide_running()
launch <user.launch_applications>: user.switcher_launch(launch_applications)
snap <user.window_snap_position>: user.snap_window(window_snap_position)
snap next [screen]: user.move_window_next_screen()
snap last [screen]: user.move_window_previous_screen()
snap screen <number>: user.move_window_to_screen(number)
snap <user.running_applications> <user.window_snap_position>:
    user.snap_app(running_applications, window_snap_position)
snap <user.running_applications> [screen] <number>:
    user.move_app_to_screen(running_applications, number)

# virtual desktops
desk next: key(ctrl-alt-right)
desk left: key(ctrl-alt-left)

# media keys
volume up: user.system_command("pactl set-sink-volume 0 +10%")
volume down: user.system_command("pactl set-sink-volume 0 -10%")
volume <number>: user.system_command("pactl set-sink-volume 0 {number}%")
volume mute: user.system_command("pactl set-sink-mute @DEFAULT_SINK@ toggle")
[media] play next: key(next)
[media] play previous: key(prev)
media (play | pause): key(play)

# brightness
brightness up: user.system_command("brillo -A 10")
brightness down: user.system_command("brillo -U 10")
brightness <number>: user.system_command("brillo -S {number}")
brightnessp dot <number>: user.system_command("brillo -S .{number}")

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
(abbreviate|abreviate|brief) {user.abbreviation}: "{abbreviation}"
#(jay son | jason ): "json"
#(http | htp): "http"
#M D five: "md5"
#word (regex | rejex): "regex"

talon fast: user.make_fast()
talon slow: user.make_slow()
