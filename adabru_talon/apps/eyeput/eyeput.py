import asyncio
import os.path
import pickle
import threading


# see ~/downloads/talon-linux/talon/resources/python/lib/python3.9/site-packages/talon/plugins/eye_mouse_2.pyi
# see ~/downloads/talon-linux/talon/resources/python/lib/python3.9/site-packages/talon/track/tobii.pyi
# see https://developer.tobii.com/product-integration/stream-engine
# see https://tobiitech.github.io/stream-engine-docs

from talon import Module, actions, registry
from talon.plugins.eye_mouse_2 import BaseControlMouse

from ...code.unix_socket import UnixSocket
from .resource import register
from .session_bus import SessionBus
from .shared_tags import Event, TagSharing, Tags

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
    sock_gaze = UnixSocket("/tmp/gaze_input.sock", 200)

    def update(self, tracker, screen, frame) -> None:
        global i
        if i == 0:
            print(
                frame.gaze_frame.left.pos,
            )
        i += 1
        try:
            self.sock_gaze.try_send(
                pickle.dumps(
                    (
                        frame.gaze_frame.ts,
                        list(frame.gaze_frame.left.pos),
                        list(frame.gaze_frame.left.gaze3d),
                        list(frame.gaze_frame.right.pos),
                        list(frame.gaze_frame.right.gaze3d),
                    )
                )
            )
        except (BlockingIOError, OSError) as e:
            if i == 1:
                print(e)
            # print("eyeput unavailable")


recording_mouse = RecordingMouse()
streaming_mouse = StreamingMouse()


tags = Tags()

# couple bus thread and talon thread via talon.registry.dispatch_async
bus_thread_id = None


def tag_changed(tag, value):
    # relay to talon thread
    if threading.get_native_id() == bus_thread_id:
        registry.dispatch_async("eyeput", tag, value)
        return

    if tag == "follow":
        actions.user.toggle_mouse(value)
    elif tag == "connect":
        streaming_mouse.start()


tags.tag_changed.subscribe(tag_changed)

registry.register("eyeput", tag_changed)


class BusConnection:
    def __init__(self):
        # there's no running event loop
        self.run_event_loop = True
        th = threading.Thread(target=self.run)
        th.start()
        global bus_thread_id
        bus_thread_id = th.native_id

    def run(self):
        asyncio.run(self.run2())

    async def run2(self):
        # start bus
        self.bus = SessionBus("/tmp/adabru", client_only=True)
        self.bus.subscribe(self.bus_event)

        # synchronize between talon and bus
        self.tag_sharing = TagSharing(
            tags,
            self.bus,
            "talon.tags",
            "eyeput.tags",
            asyncio.get_running_loop(),
        )

        # keep event loop running
        while self.run_event_loop:
            await asyncio.sleep(1)
        print("Stop event loop.")

    def bus_event(self, event):
        print("bus event:", event)
        if event == "connect":
            # streaming_mouse.start() or cron.after can't be called from a async function:
            # > IO No active resource context in this thread/coroutine.
            registry.dispatch_async("eyeput", "connect", True)

    def cleanup(self):
        self.run_event_loop = False
        streaming_mouse.sock_gaze.sock.close()


connection = BusConnection()

register("eyeput", connection.cleanup)


# destructor and module unload is quite unreliable
#
# class _C:
#     def __del__(self):
#         print("destructor cleanup")
#         connection.cleanup()
# unload_trigger = _C()
#
# def unloading_module():
#     print("module  cleanup")
#     connection.cleanup()
# # https://docs.python.org/3/library/weakref.html#weakref.finalize
# weakref.finalize(sys.modules[__name__], unloading_module)


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

    def set_tag(tag: str, value: bool):
        """..."""
        tags.set_tag_value(tag, value)

    def toggle_tag(tag: str):
        """..."""
        tags.toggle_tag(tag)