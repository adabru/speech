#defines the commands that sleep/wake Talon
mode: all
-
^deep sleep [<phrase>]$:
    user.enable_deep_sleep()
    speech.disable()
    user.mouse_sleep()
^wakeup wakeup$:
    user.disable_deep_sleep()
    speech.enable()
    user.mouse_toggle_control_mouse()
