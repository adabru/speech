import os
from re import S
import sys
import subprocess

# local
from .unix_socket import UnixSocket

from talon import Module

mod = Module()

sock_launcher = UnixSocket("/tmp/launcher.sock", 100)


def get_environment():
    env = os.environ.copy()
    # remove talon specific variables
    del env["LC_NUMERIC"]
    del env["QT_PLUGIN_PATH"]
    del env["LD_LIBRARY_PATH"]
    return env


@mod.action_class
class Actions:
    def system_exec(cmd: str):
        """execute a command on the system"""
        subprocess.run(cmd, shell=True, env=get_environment())

    def system_start(cmd: str):
        """execute a command on the system without blocking"""
        subprocess.Popen(
            cmd,
            shell=True,
            env=get_environment(),
        )

    def system_launch(cmd: str):
        """execute a detached command on the system"""
        sock_launcher.try_send(f"x{cmd}")
