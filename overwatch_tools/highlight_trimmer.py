#!/usr/bin/env python3
import argparse
import os
import pathlib
import platform
import shutil
import subprocess


def get_windows_profile_path():
    """
    If this program is run through WSL, this should return something like
    "/mnt/c/Users/Username'.
    @return The user's home directory.
    """
    profile_path = None
    if platform.system() == "Linux":
        with open("/proc/version", "r") as f:
            if "Microsoft" in f.read():
                cmd = "wslpath $(cmd.exe /C 'echo %USERPROFILE%')"
                p = subprocess.run(
                    cmd,
                    shell=True,
                    universal_newlines=True,
                    stdout=subprocess.PIPE
                )
                profile_path = p.stdout.strip()
    else:
        return str(pathlib.Path.home())
    return profile_path


def get_overwatch_record_path():
    overwatch_record_path = os.environ.get("OVERWATCH_RECORD_PATH")
    if not overwatch_record_path:
        windows_profile_path = get_windows_profile_path()
        if windows_profile_path:
            overwatch_record_path = (
                pathlib.Path(windows_profile_path) / "Documents" / "Overwatch"
            )
        else:
            raise FileNotFoundError(
                "Could not find Overwatch record folder. "
                "Please set OVERWATCH_RECORD_PATH environment variable."
            )
    return overwatch_record_path


def get_overwatch_highlight_paths():
    """
    @return An iterator containing all file paths in the highlights folder.
    """
    ow_highlight_path = get_overwatch_record_path() / "videos" / "overwatch"
    return ow_highlight_path.iterdir()


def fix_highlight_name(name):
    """
    Strips off the time format Blizzard appends to highlights.

    >>> fix_highlight_name("countercalculated_18-09-19_00-14-09.mp4")
    'countercalculated.mp4'
    """
    filename = pathlib.Path(name)
    return "".join([filename.stem[:-18], filename.suffix])


def most_recent_highlight(highlights):
    """
    @return The most recent highlight of the supplied highlight paths.
    """
    return max(highlights, key=lambda i: i.stat().st_mtime)


def trim_clip(ffmpeg_path, input_filename, output_filename):
    """
    The work horse method of the whole program, this trims off the highlight
    intro and the Overwatch logo of any Overwatch highlight video, cutting a
    24-second clip down to 7.5.
    It does so by a simple ffmpeg command, so ffmpeg needs to be installed for
    it to work.
    @param ffmpeg_path Path to the ffmpeg executable
    @param input_filename The filename of the raw Overwatch highlight.
    @param output_filename The filename to which the new clip should be
    written.
    """
    start = 5.4375
    duration = 12
    ffmpeg_args = [
        ffmpeg_path,
        "-ss", str(start),
        "-t", str(duration),
        "-strict",
        "-2",
        "-i",
        input_filename,
        output_filename
    ]
    p = subprocess.run(
        ffmpeg_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        universal_newlines=True
    )
    print(p.stdout)


def get_arguments(args=None):
    overwatch_record_path = get_overwatch_record_path()
    ow_highlight_path = overwatch_record_path / "videos" / "overwatch"
    highlights = ow_highlight_path.iterdir()
    highlight_paths = list(get_overwatch_highlight_paths())
    if len(highlight_paths):
        mr_highlight_path = most_recent_highlight(highlight_paths)
        default_input = str(mr_highlight_path)
        default_output = fix_highlight_name(mr_highlight_path.name)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--input", type=str, default=default_input,
        help="The clip to be trimmed. Defaults to \"{}\"".format(default_input)
    )
    parser.add_argument(
        "-o", "--output", type=str, default=default_output,
        help="Output filename. Defaults to \"{}\"".format(default_output),
    )
    # Make ffmpeg_path required only if shutil doesn't find it.
    ffmpeg_path = shutil.which("ffmpeg")
    parser.add_argument(
        "-f", "--ffmpeg_path", type=str,
        help="Path to FFMPEG executable." + (
            " Defaults to {}".format(ffmpeg_path) if ffmpeg_path else ""
        ),
        required=not ffmpeg_path,
        default=ffmpeg_path
    )
    namespace_args = parser.parse_args(args=args)
    return namespace_args


def main():
    args = get_arguments()
    trim_clip(args.ffmpeg_path, args.input, args.output)


if __name__ == "__main__":
    main()
