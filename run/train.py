#!/usr/bin/python

import subprocess

subprocess.run('sphinxtrain run', shell=True, cwd='../sphinx/own').check_returncode()
