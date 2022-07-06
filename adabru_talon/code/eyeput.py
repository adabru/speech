import os.path

# see ~/downloads/talon-linux/talon/resources/python/lib/python3.9/site-packages/talon/plugins/eye_mouse_2.pyi
# see ~/downloads/talon-linux/talon/resources/python/lib/python3.9/site-packages/talon/track/tobii.pyi
# see https://developer.tobii.com/product-integration/stream-engine
# see https://tobiitech.github.io/stream-engine-docs

from talon import tracking_system, Module
from talon.plugins.eye_mouse_2 import BaseControlMouse

from .unix_socket import UnixSocket

# print(tracking_system.trackers)
# print(tracking_system.topics)
# print(tracking_system.lambdas)
# print(tracking_system.display_mapping)
# for tracker in tracking_system.trackers:
#     print(tracker)
#     print(tracker.stream_types)
#     print(tracker.streams)
#     break


class RecordingMouse(BaseControlMouse):
    trace = []
    trace_path = os.path.expanduser("~/s")

    def on_gaze(self, frame):
        self.trace.append(f"{frame.ts} {frame.num} {frame.gaze.x} {frame.gaze.y}")

    def stop(self):
        """..."""
        super().stop()
        with open(self.trace_path, "w") as file:
            file.write("\n".join(self.trace))
        self.trace = []


i = 0


class StreamingMouse(BaseControlMouse):
    sock_gaze = UnixSocket("/tmp/gaze_input.sock", 100)

    def on_gaze(self, frame):
        global i
        if i == 0:
            # print(frame.left)
            print(frame.left.validity, frame.left.detected, frame.left.gaze.x)
        i += 1
        try:
            self.sock_gaze.try_send(
                f"{frame.ts} {frame.left.gaze.x} {frame.left.gaze.y} {frame.right.gaze.x} {frame.right.gaze.y}"
            )
        except BlockingIOError as e:
            # print("eyeput unavailable")
            pass


recording_mouse = RecordingMouse()
streaming_mouse = StreamingMouse()

mod = Module()


@mod.action_class
class Actions:
    def start_eye_record():
        """???"""
        recording_mouse.start()

    def end_eye_record():
        """???"""
        recording_mouse.stop()

    def start_eye_stream():
        """???"""
        streaming_mouse.start()

    def end_eye_stream():
        """???"""
        streaming_mouse.stop()
