#defines the commands that sleep/wake Talon
mode: all
not tag: user.deep_sleep
-
^sleep [<phrase>]$:
    speech.disable()
    user.mouse_sleep()
^wake$:
    speech.enable()
    user.mouse_toggle_control_mouse()
