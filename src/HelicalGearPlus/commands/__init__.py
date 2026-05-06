# Here you define the commands that will be added to your add-in.
#
# Port the legacy command(s) from docs/HelicalGearPlus/HelicalGearPlus.py into
# new submodules under this directory (one folder per command, each containing
# entry.py + resources/), then import and register them here.

commands = []


def start():
    for command in commands:
        command.start()


def stop():
    for command in commands:
        command.stop()
