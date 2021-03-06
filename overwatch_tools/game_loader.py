#!/usr/bin/env python3
import argparse
import sys
import time

try:
    import pyautogui
    import pyperclip
except ImportError:
    err = (
        "You need to install pyautogui first:\n"
        "pip install pyautogui"
    )
    quit(err)

def _get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "rule_file",
        type=argparse.FileType("r"),
        help=(
            "The rules to be pasted into Overwatch Workshop. "
            "This file can be generated by selecting all rules in the workshop"
            ", clicking the \"copy\" button, and pasting them into a text "
            "file."
        ),
    )
    parser.add_argument(
        "-x",
        type=int,
        required=False,
        help=(
            "The x-coordinate at which to place the mouse at first click."
        ),
    )
    parser.add_argument(
        "-y",
        type=int,
        required=False,
        help=(
            "The y-coordinate at which to place the mouse at first click."
        ),
    )
    return parser.parse_args()


def main():
    args = _get_args()
    workshop_rules = args.rule_file.read()
    pyperclip.copy(workshop_rules)

    if args.x is None or args.y is None:
        msg = (
            "Calibrating..."
            "Make sure Overwatch is at the title screen and the window running"
            " this program has focus.\n"
            "Move your mouse to the titlebar of the Overwatch window, then hit "
            "Enter."
        )
        input(msg)
        position = pyautogui.position()
        coord_args = ["-x", str(position.x), "-y", str(position.y)]
        next_usage_args = sys.argv + coord_args
        print(
            "Use this line to skip calibration next time: \n",
            " ".join(next_usage_args)
        )
    else:
        pyautogui.moveTo(args.x, args.y);

    pyautogui.click();
    # Enter "play" menu.
    pyautogui.typewrite(['esc', 'esc', 'down', 'space'])

    # Select Game Browser.
    pyautogui.typewrite(['left', 'left', 'space'])

    # Select "+CREATE"
    pyautogui.typewrite(['tab'] * 4 + ['space'])

    # Transition animations for things that wait on user input are stupid.
    # SO NOW WE WAIT
    print("Waiting on the \"create game\" transition animation.")
    time.sleep(3)

    # Tab aaaaall the way to settings.
    # TODO: Would prefer just selecting the settings button by mouse.
    # Have to tab twice to get past the "move" button for some reason.
    pyautogui.typewrite(['tab'] * 21 + ['space'])

    # Select Workshop
    pyautogui.typewrite(['down', 'down'] + ['space'])

    # Paste rules button is already selected.
    pyautogui.typewrite(['space'])

    # Go back to lobby.
    pyautogui.typewrite(['escape'] * 2, .5)
    print("Set up complete.")


if __name__ == "__main__":
    main()
