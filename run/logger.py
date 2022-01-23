import sys, logging

# create logger for : journalctl -u -b speech.keyboard
# https://stackoverflow.com/questions/34588421/how-to-log-to-journald-systemd-via-python
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # maximal logging level e.g. [DEBUG|INFO]

formatter = logging.Formatter(fmt="%(message)s (%(filename)s:%(lineno)d)")
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(formatter)
logger.addHandler(handler)
