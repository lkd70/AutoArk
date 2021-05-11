from pynput import keyboard
from sections import commands


def set_fps_to_15():
    commands.set_fps(fps=15)


def main():
    with keyboard.GlobalHotKeys({
        '<f1>': set_fps_to_15,
    }) as h:
        h.join()


if __name__ == '__main__':
    main()
