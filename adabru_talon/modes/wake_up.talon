#defines the commands that sleep/wake Talon
mode: all
not tag: user.deep_sleep
-
^sleep [<phrase>]$:
    speech.disable()
    user.set_tag("follow", false)
^wake$:
    speech.enable()
    user.toggle_tag("follow")
