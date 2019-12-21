#!/usr/bin/env python3

""" The main commandline entry point to Pymusic """
# TODO: update usage for invalid intervals. Fix formatting of usage output.

import sys
import argparse

import musictheorpy.notes as notes
import musictheorpy.scales as scales

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
    parser = get_parser()
    args = parser.parse_args()
    args.func(args)


def intervalsmain(args):
    unpacker = get_unpacker('intervals')
    startingnote, interval, descend = unpacker(args)

    if startingnote is None:
        print(invalid_note_help)
        sys.exit()

    if interval is None:
        print(invalid_interval_help)
        sys.exit()

    article = "An" if interval.startswith('AUGMENTED') else "A"

    if descend:
        try:
            bottom_note = startingnote.descend_interval(interval)
            print("%s %s descending from %s is %s.\n" % (article, interval.lower(), startingnote, bottom_note))
        except notes.InvalidIntervalError:
            print("%s %s descending from %s results in an invalid note.\n" % (article, interval.lower(), startingnote))
        finally:
            sys.exit()
    else:
        try:
            top_note = startingnote.ascend_interval(interval)
            print("%s %s ascending from %s is %s.\n" % (article, interval.lower(), startingnote, top_note))
        except notes.InvalidIntervalError:
            print("%s %s ascending from %s results in an invalid notes.\n" % (article, interval.lower(), startingnote))
        finally:
            sys.exit()


def scalesmain(args):
    unpacker = get_unpacker('scales')
    tonic, minor, degree, number, relative, parallel = unpacker(args)

    if tonic is None:
        print(invalid_note_help)
        sys.exit()

    if minor:
        scale = get_minor_scale(tonic, minor.upper())
    else:
        qualified_scalename = f"{tonic} MAJOR"
        scale = get_scale_obj(qualified_scalename)

    if scale is None:
        print("Invalid tonic or minor quality.")
        sys.exit()

    if not any([minor, degree, number, relative, parallel]):
        print(*scale.notes)


def chordsmain(args):
    unpacker = get_unpacker('chords')


def get_note_obj(notename):
    try:
        return notes.Note(notename)
    except notes.NoteNameError:
        return None


def get_minor_scale(tonic, minor):
    if minor.upper() not in ['NATURAL', 'HARMONIC', 'MELODIC']:
        return None

    qualified_scalename = f"{tonic} {minor.upper()} MINOR"
    return get_scale_obj(qualified_scalename)


def get_scale_obj(scalename):
    try:
        return scales.Scale(scalename)
    except scales.InvalidTonicError:
        return None


def map_interval(interval):
    try:
        return INTERVAL_MAP[interval]
    except KeyError:
        return None


def get_unpacker(unpackertype):
    if unpackertype == 'intervals':
        return unpack_interval_arguments
    elif unpackertype == 'scales':
        return unpack_scale_arguments
    elif unpackertype == 'chords':
        return unpack_chord_arguments
    else:
        raise ValueError('That is not a valid argument unpacker.')


def unpack_interval_arguments(args):
    note = get_note_obj(args.startingnote)
    interval = map_interval(args.interval)

    if args.descend:
        descend = args.descend
        return note, interval, descend

    return note, interval, False


def unpack_scale_arguments(args):
    currentargs = []
    note = get_note_obj(args.tonic)
    currentargs.append(note)

    if args.minor:
        currentargs.append(args.minor)
    else:
        currentargs.append(None)

    if args.degree:
        currentargs.append(args.degree)
    else:
        currentargs.append(None)

    if args.number:
        currentargs.append(args.number)
    else:
        currentargs.append(None)

    if args.relative:
        currentargs.append(True)
    else:
        currentargs.append(False)

    if args.parallel:
        currentargs.append(True)
    else:
        currentargs.append(False)

    return currentargs  # return value should be unpacked into individual variables


def unpack_chord_arguments(args):
    pass


def get_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    intervalparser = subparsers.add_parser('intervals')
    intervalparser.add_argument('startingnote')
    intervalparser.add_argument('interval')
    intervalparser.add_argument('-d', '--descend', action='store_true')
    intervalparser.set_defaults(func=intervalsmain)

    scaleparser = subparsers.add_parser('scales')
    scaleparser.add_argument('tonic')
    scaleparser.add_argument('-m', '--minor')
    scaleparser.add_argument('-d', '--degree')
    scaleparser.add_argument('-n', '--number')
    scaleparser.add_argument('-r', '--relative', action='store_true')
    scaleparser.add_argument('-p', '--parallel', action='store_true')
    scaleparser.set_defaults(func=scalesmain)

    chordparser = subparsers.add_parser('chords')
    chordparser.add_argument('root')
    chordparser.add_argument('-m', '--minor')
    chordparser.add_argument('-d', '--degree')
    chordparser.add_argument('-r', '--relative')
    chordparser.add_argument('-p', '--parallel')
    chordparser.set_defaults(func=chordsmain)

    return parser


if __name__ == '__main__':
    main()
