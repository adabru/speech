#defines the commands that sleep/wake Talon
mode: all
not tag: user.deep_sleep
-
^sleep [<phrase>]$:
    speech.disable()
    user.toggle_mouse(0)
^wake$:
    speech.enable()
    user.toggle_mouse()
