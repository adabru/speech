#defines the commands that sleep/wake Talon
mode: all
-
^deep sleep [<phrase>]$:
    user.enable_deep_sleep()
    speech.disable()
    # user.engine_sleep()
    user.set_tag("follow", false)
^wakeup wakeup$:
    user.disable_deep_sleep()
    speech.enable()
    user.toggle_tag("follow")
