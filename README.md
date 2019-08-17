# overwatch_tools
Utilities designed to help players of the game Overwatch.

## Description

This repository is meant to contain various tools I come up with to supplement stuff I do in Overwatch. So far I just have a utility to trim highlights (reduces file size and makes it a lot easier to deal with them in video editing).

It should be known that Blizzard has a [very strong stance against third-party applications that provide an unfair advantage](https://us.forums.blizzard.com/en/overwatch/t/unauthorized-third-party-software/213220) so this repository will take special care to only improve the competitive integrity of Overwatch.

## Requirements
- [Python 3](https://www.python.org/) needs to be installed to run anything python. Pip is usually included with the installation, and that's needed to actually install this script.
- [ffmpeg](https://ffmpeg.org/) needs to be installed in order for the highlight trimmer to perform video manipulation.
- The highlight trimmer has been tested in both Windows Powershell and Windows Subsystem for Linux. Support for actual Linux installations of Overwatch has not been implemented yet.

## Installation

- Clone the repository to wherever you feel comfortable. Or download the zip and extract it somewhere.
    `$ git clone https://github.com/CarvellScott/overwatch_tools.git`
- Change directories into overwatch_tools.:
    `$ cd overwatch_tools`
- Finally pip install . to install it from the setup.py file.
    `$ pip install .`

## Usage:
    
    usage: highlight-trimmer [-h] [-i INPUT] [-o OUTPUT] [-f FFMPEG_PATH]

    optional arguments:
      -h, --help            show this help message and exit
      -i INPUT, --input INPUT
                            The clip to be trimmed.
      -o OUTPUT, --output OUTPUT
                            Output filename.
      -f FFMPEG_PATH, --ffmpeg_path FFMPEG_PATH
                            Path to FFMPEG executable.
