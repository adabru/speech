#!/usr/bin/python

# minimal imports for faster startup
import os
from logger import logger

def run():
    import time
    import sys
    import signal
    import json

    os.environ["QT_QPA_PLATFORM"] = "xcb" # window oddly resizes when regaining focus

    from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
    from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot, Qt
    from PyQt5.QtGui import QFont

    # local
    from unix_socket import UnixSocket

    SOCKET_PATH = "/tmp/speech_gui.sock"

    class Server(QThread):
        update_signal = pyqtSignal(str)

        def __init__(self):
            super().__init__()
            self._quit = False
            self.state = {
                "pause": False, 
                "hold": False, 
                "shift": False, 
                "ctrl": False, 
                "alt": False, 
                "win": False, 
                "key": ""
            }
  
        def run(self):
            self._update()
            while not self._quit:

                try:
                    os.unlink(SOCKET_PATH)
                except OSError:
                    if os.path.exists(SOCKET_PATH):
                        raise

                sock = UnixSocket(SOCKET_PATH, 100)
                sock.listen()

                while True:
                    logger.info('Wait for a connection')
                    sock.accept()
                    logger.info('Connected. Listening for keys ...')
                    try:
                        # Receive the data in small chunks and retransmit it
                        while True:
                            msg = sock.receive()
                            self.state["pause"] = msg[0] == "1"
                            self.state["hold"] = msg[1] == "1"
                            self.state["shift"] = msg[2] == "1"
                            self.state["ctrl"] = msg[3] == "1"
                            self.state["alt"] = msg[4] == "1"
                            self.state["win"] = msg[5] == "1"
                            self.state["key"] = msg[6:]
                            self._update()
                    
                    except RuntimeError as err:
                        logger.info(err)

                    finally:
                        logger.info('Clean up the connection')
                        sock.close_connection()

                exit()

        def _update(self):
            message = json.dumps(self.state)
            logger.info(message)
            self.update_signal.emit(message)

        def quit(self):
            self._quit = True


    class App(QObject):
        colors = {
            "background": "#B7EBB9",

            "mods": "#8875E4DE",
            "mods_hold": "#88F3E803",
            "mod_active": "#8804C1E1",
            "mod_active_hold": "#88F6AC0D"
        }
        labels = {}

        def __init__(self):
            super().__init__()
            modsLayout = QHBoxLayout()
            self.modsWidget = QWidget()          
            self.modsWidget.setLayout(modsLayout)
            self.modsWidget.setStyleSheet('''
                QLabel { font-size: 12pt; min-width: 14px; }
                .QWidget { border-bottom-left-radius: 10px; border-top-left-radius: 10px; }
            ''')

            layout = QHBoxLayout()
            layout.addWidget(self.modsWidget)
            self.widget = QWidget()
            self.widget.setLayout(layout)
            self.widget.setStyleSheet('''
                QLabel { font-size: 12pt; }
                QWidget { background-color: #88B7EBB9 }
            ''')
            self.widget.setAttribute(Qt.WA_TranslucentBackground, True)
            self.widget.setWindowFlags(Qt.FramelessWindowHint)

            for labelKey in ['shift', 'ctrl', 'alt', 'win']:
                label = QLabel()
                label.setText(labelKey[0])
                label.setAlignment(Qt.AlignCenter)
                modsLayout.addWidget(label)
                self.labels[labelKey] = label

            self.labelKey = QLabel()
            self.labelKey.setText('')
            self.labelKey.setFixedWidth(100)
            layout.addWidget(self.labelKey)

            # layout.addStretch()
            layout.setAlignment(Qt.AlignLeft)
            layout.setSpacing(0)

            self.widget.setWindowTitle("speechwindow")
            self.widget.show()

            class PostResizeThread(QThread):
                def __init__(self, widget):
                    super().__init__()
                    self.widget = widget
                def run(self):
                    time.sleep(.1)
                    self.widget.setGeometry(0, 0, 130, 40)
            self.post_resize_thread = PostResizeThread(self.widget)
            self.post_resize_thread.start()

        @pyqtSlot(str)
        def update(self, message):
            data = json.loads(message)

            modsBGColor = self.colors['mods_hold'] if data['hold'] else self.colors['mods']
            self.modsWidget.setStyleSheet("""
                QLabel { font-size: 12pt; min-width: 14px; }
                .QWidget { border-bottom-left-radius: 10px; border-top-left-radius: 10px; background-color: %s}
            """ % (modsBGColor))

            for key, label in self.labels.items():
                if data[key]:
                    colorKey = f"mod_active{'_hold' if data['hold'] else ''}"
                    label.setStyleSheet(f"background-color: {self.colors[colorKey]}")
                else:
                    label.setStyleSheet(f"background-color: none")

            self.labelKey.setText(" " + data["key"])

    qapp = QApplication(sys.argv)
    app = App()
    serverthread = Server()
    # thread safe communication, QtGui requires all gui related code to be called from the same thread
    serverthread.update_signal.connect(app.update, Qt.QueuedConnection)
    # design flaw, see https://stackoverflow.com/q/4938723/6040478
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    serverthread.start()
    qapp.exec_()
    logger.info('Quit, collecting threads.')
    serverthread.quit()
    serverthread.wait()
    # signal.pause()

run()
