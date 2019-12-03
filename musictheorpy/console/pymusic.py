#!/usr/bin/env python3

import sys
import argparse

import musictheorpy.notes as notes
# from musictheorpy.console import parser

invalid_note_help = "You have entered an invalid note name. Valid notes are uppercase English letters A through G\n"\
                    "possibly followed by a qualifier. Valid qualifiers are #, ##, b, and bb. No qualifier represents\n"\
                    "a natural. For example, A#, C, D##, Bb, Cbb are all valid notes, while AB, H#, and F### are\n"\
                    "invalid. "

invalid_interval_help = "You have entered an invalid interval.\n" \
                        "Intervals are represented by a letter representing the quality, followed by the interval\n"\
                        "number. Qualifiers are m (minor), M (major), A (augmented), d (diminished), and P (perfect).\n"\
                        "Qualifiers are case sensitive and and follow the standard scheme from Western music theory\n"\
                        "that major, augmented, and perfect are capitalized, while diminished and minor are\n"\
                        "lowercase. Valid interval numbers are 0 through 15."


def main():
    # get an ArgumentParser object
    # add subparsers to ArgumentParser
    # create one subparser per pymusic subcommand
    # add appropriate arguments to each subparser

    # ----- Notes -----
    # validate note input, validate interval input
    # print appropriate messages to user if input is invalid
    # if input is valid, print output

    # ----- Scales  -----
    # validate tonic and quality
    # if no options are passed, print all notes in the scale
    # if -d, --degree is passed, validate degree name input, print output
    # if -n, --number is passed, validate degree number, print output
    # if -m, --mode is passed, validate mode name, print output
    # if -f, --minor is passed, validate minor quality, print output
    pass


if __name__ == '__main__':
    main()
