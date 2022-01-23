#!/usr/bin/python

# the choosen one: https://github.com/boppreh/keyboard
# https://github.com/gvalkov/python-evdev
# https://gitlab.com/interception/linux/tools/
# https://github.com/dictation-toolbox/aenea/tree/master/server
#
# bad:
#  https://git.sr.ht/~brocellous/wlrctl
#  simulate input events: https://github.com/swaywm/sway/issues/1779
#  https://github.com/moses-palmer/pynput/issues/184
#  https://github.com/atx/wtype/issues

import os
import time
import keyboard

# local
from unix_socket import UnixSocket
from logger import logger

try:
    os.unlink('/tmp/evdev_keypress.sock')
except OSError:
    if os.path.exists('/tmp/evdev_keypress.sock'):
        raise

keyboard.press_and_release('5')

sock_keyboard = UnixSocket('/tmp/evdev_keypress.sock', 100)
sock_keyboard.listen()

while True:
    logger.info('Wait for a connection')
    sock_keyboard.accept()
    logger.info('Connected. Listening for keys ...')
    try:
        # Receive the data in small chunks and retransmit it
        while True:
            keyboardCode = sock_keyboard.receive()

            keyboard.press_and_release('shift')
            time.sleep(0.02)
            keyboard.press_and_release(keyboardCode)
    
    except RuntimeError as err:
        logger.error(err)

    finally:
        logger.info('Clean up the connection')
        sock_keyboard.close_connection()

exit()
