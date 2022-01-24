# keyboard keys = low level
go <user.arrow_keys>: key(arrow_keys)
<user.letter>: key(letter)
(ship | uppercase) <user.letters> [(lowercase | sunk)]:
    user.insert_formatted(letters, "ALL_CAPS")
<user.symbol_key>: key(symbol_key)
<user.function_key>: key(function_key)
<user.special_key>: key(special_key)
<user.modifiers> <user.unmodified_key>: key("{modifiers}-{unmodified_key}")
press <user.modifiers>: key(modifiers)

# universal shortcuts
zoom in: edit.zoom_in()
zoom out: edit.zoom_out()
zoom reset: edit.zoom_reset()
scroll up: edit.page_up()
scroll down: edit.page_down()
copy that: edit.copy()
cut that: edit.cut()
paste that: edit.paste()
undo that: edit.undo()
redo that: edit.redo()
paste match: edit.paste_match_style()
file save: edit.save()
slap: edit.line_insert_down()

# repeat commands
<user.ordinals>: core.repeat_command(ordinals-1)
<number_small> times: core.repeat_command(number_small-1)
again: core.repeat_command(1)

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
desk <number_small>: user.desktop(number_small)
desk next: user.desktop_next()
desk last: user.desktop_last()
desk show: user.desktop_show()
window move desk <number>: user.window_move_desktop(number)
window move desk left: user.window_move_desktop_left()
window move desk right: user.window_move_desktop_right()

# media keys
volume up: key(volup)
volume down: key(voldown)
set volume <number>: user.media_set_volume(number)
(volume|media) mute: key(mute)
[media] play next: key(next)
[media] play previous: key(prev)
media (play | pause): key(play)

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
