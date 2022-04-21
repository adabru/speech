import os.path
from tokenize import triple_quoted
from talon import tracking_system, Module
from talon.plugins.eye_mouse_2 import BaseMouse

print(tracking_system.trackers)
print(tracking_system.topics)
# print(tracking_system.lambdas)
# print(tracking_system.display_mapping)
for tracker in tracking_system.trackers:
    # print(tracker)
    # print(tracker.stream_types)
    # print(tracker.streams)
    break


class DebugMouse(BaseMouse):
    trace = []

    def on_gaze(self, frame):
        self.trace.append(f"{frame.ts} {frame.num} {frame.gaze.x} {frame.gaze.y}")


mouse = DebugMouse()

mod = Module()
trace_path = os.path.expanduser("~/s")


@mod.action_class
class Actions:
    def start_eye_record():
        """???"""
        mouse.start()

    def end_eye_record():
        """???"""
        mouse.stop()
        with open(trace_path, "w") as file:
            file.write("\n".join(mouse.trace))
        mouse.trace = []
