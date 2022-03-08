#!/usr/bin/python

import os
import subprocess

# local
from unix_socket import UnixSocket
from logger import logger

try:
    os.unlink("/tmp/launcher.sock")
except OSError:
    if os.path.exists("/tmp/launcher.sock"):
        raise

sock_launcher = UnixSocket("/tmp/launcher.sock", 100)
sock_launcher.listen()

while True:
    logger.info("Wait for a connection")
    sock_launcher.accept()
    logger.info("Connected. Listening for commands ...")
    try:
        while True:
            command = sock_launcher.receive()
            # very basic security
            command = command[1:]
            logger.info(command)
            subprocess.Popen(
                command,
                shell=True,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

    except RuntimeError as err:
        logger.error(err)

    finally:
        logger.info("Clean up the connection")
        sock_launcher.close_connection()

exit()
