# user threads are not managed by talon. That's why this module exists
resources = {}


def register(name, cleanup_callback):
    if name in resources:
        resources[name]()
    resources[name] = cleanup_callback
