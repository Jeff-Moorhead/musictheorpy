import argparse

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


class IntervalParser:
    def __init__(self):
        usage = "intervals: [-d, --descend] starting_note interval"
        self._parser = argparse.ArgumentParser(usage=usage)
        self._add_args()
        self._args = self._parse()


class PyMusicArgumentParser:
    def __init__(self):
        pass

    def _add_args(self):
        note_usage = "The starting note for the interval. Valid notes are uppercase English letters A through G " \
                     "possibly followed by a qualifier. Valid qualifiers are #, ##, b, and bb. No qualifier " \
                     "represents a natural. For example, A#, C, D##, Bb, Cbb are all valid notes, while AB, H#, " \
                     "and F### are invalid."
        interval_usage = "The interval to ascend or descend from the starting note. The default behavior is to ascend. "\
                         "Intervals are represented by a letter representing the quality, followed by the interval " \
                         "number. Qualifiers are m (minor), M (major), A (augmented), d (diminished), " \
                         "and P (perfect). Qualifiers are case sensitive and and follow the standard scheme from " \
                         "Western music theory that major, augmented, and perfect are capitalized, while diminished " \
                         "and minor are lowercase. Valid interval numbers are 0 through 15."
        descend_usage = "If included, the interval will be calculated descending from the starting note. If omitted, " \
                        "the default behavior of ascending from the starting note will be used."

        self._parser.add_argument('starting_note', type=str, help=note_usage)
        self._parser.add_argument('interval', type=str, help=interval_usage)
        self._parser.add_argument('-d', '--descend', action='store_true', help=descend_usage)

    def _parse(self):
        raw_args = self._parser.parse_args()
        mapped_interval = map_interval(raw_args.interval)

        mapped_args = raw_args
        mapped_args.interval = mapped_interval

        return mapped_args

    def pack(self):
        return self._args.__dict__


def map_interval(interval):
    try:
        return INTERVAL_MAP[interval]
    except KeyError:
        return None
