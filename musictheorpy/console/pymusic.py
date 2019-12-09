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

INTERVAL_MAP = {'P0': 'PERFECT 0', 'd2': 'DIMINISHED 2', 'm2': 'MINOR 2', 'A0': 'AUGMENTED 0',
                'm9': 'MINOR 9', 'M2': 'MAJOR 2', 'd3': 'DIMINISHED 3', 'M9': 'MAJOR 9',
                'm3': 'MINOR 3', 'A2': 'AUGMENTED 2', 'm10': 'MINOR 10', 'M3': 'MAJOR 3',
                'd4': 'DIMINISHED 4', 'M10': 'MAJOR 10', 'P4': 'PERFECT 4', 'A3': 'AUGMENTED 3',
                'P11': 'PERFECT 11', 'd5': 'DIMINISHED 5', 'A4': 'AUGMENTED 4', 'd12': 'DIMINISHED 12',
                'P5': 'PERFECT 5', 'd6': 'DIMINISHED 6', 'P12': 'PERFECT 12', 'm6': 'MINOR 6',
                'A5': 'AUGMENTED 5', 'm13': 'MINOR 13', 'M6': 'MAJOR 6', 'd7': 'DIMINISHED 7',
                'M13': 'MAJOR 13', 'm7': 'MINOR 7', 'A6': 'AUGMENTED 6', 'm14': 'MINOR 14',
                'M7': 'MAJOR 7', 'd8': 'DIMINISHED 8', 'M14': 'MAJOR 14', 'P8': 'PERFECT 8',
                'A7': 'AUGMENTED 7', 'P15': 'PERFECT 15', 'd9': 'DIMINISHED 9',
                }


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    intervalparser = subparsers.add_parser('intervals')
    intervalparser.add_argument('notename')
    intervalparser.add_argument('interval')
    intervalparser.add_argument('-d', '--descend', action='store_true')
    intervalparser.set_defaults(func=notesfunc)

    args = parser.parse_args()
    args.func(args)

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


def notesfunc(args):
    n = notes.Note(args.notename)
    i = INTERVAL_MAP[args.interval]
    print(n.ascend_interval(i))


if __name__ == '__main__':
    main()
