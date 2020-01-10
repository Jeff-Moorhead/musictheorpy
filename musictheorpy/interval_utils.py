"""
This module holds the main data structure that facilitate the processing of intervals.
"""

INTERVAL_NOTE_PAIRS = {'A': {0: 'A', 1: 'Bb', 2: 'B', 3: 'C', 4: 'C#', 5: 'D', 6: 'Eb',
                             7: 'E', 8: 'F', 9: 'F#', 10: 'G', 11: 'G#', 12: 'A',
                             100: 'Bbb', 101: 'A#', 102: 'Cb', 103: 'B#', 104: 'Db', 105: 'C##', 106: 'D#',
                             107: 'Fb', 108: 'E#', 109: 'Gb', 110: 'F##', 111: 'Ab', 112: 'G##'},
                       'B': {0: 'B', 1: 'C', 2: 'C#', 3: 'D', 4: 'D#', 5: 'E', 6: 'F',
                             7: 'F#', 8: 'G', 9: 'G#', 10: 'A', 11: 'A#', 12: 'B',
                             100: 'Cb', 101: 'B#', 102: 'Db', 103: 'C##', 104: 'Eb', 105: 'D##', 106: 'E#',
                             107: 'Gb', 108: 'F#', 109: 'Ab', 110: 'G##', 111: 'Bb', 112: 'A##'},
                       'C': {0: 'C', 1: 'Db', 2: 'D', 3: 'Eb', 4: 'E', 5: 'F', 6: 'Gb',
                             7: 'G', 8: 'Ab', 9: 'A', 10: 'Bb', 11: 'B', 12: 'C',
                             100: 'Dbb', 101: 'C#', 102: 'Ebb', 103: 'D#', 104: 'Fb', 105: 'E#', 106: 'F#',
                             107: 'Abb', 108: 'G#', 109: 'Bbb', 110: 'A#', 111: 'Cb', 112: 'B#'},
                       'D': {0: 'D', 1: 'Eb', 2: 'E', 3: 'F', 4: 'F#', 5: 'G', 6: 'Ab',
                             7: 'A', 8: 'Bb', 9: 'B', 10: 'C', 11: 'C#', 12: 'D',
                             100: 'Ebb', 101: 'D#', 102: 'Fb', 103: 'E#', 104: 'Gb', 105: 'F##', 106: 'G#',
                             107: 'Bbb', 108: 'A#', 109: 'Cb', 110: 'B#', 111: 'Db', 112: 'C##'},
                       'E': {0: 'E', 1: 'F', 2: 'F#', 3: 'G', 4: 'G#', 5: 'A', 6: 'Bb',
                             7: 'B', 8: 'C', 9: 'C#', 10: 'D', 11: 'D#', 12: 'E',
                             100: 'Fb', 101: 'E#', 102: 'Gb', 103: 'F##', 104: 'Ab', 105: 'G##', 106: 'A#',
                             107: 'Cb', 108: 'B#', 109: 'Db', 110: 'C##', 111: 'Eb', 112: 'D##'},
                       'F': {0: 'F', 1: 'Gb', 2: 'G', 3: 'Ab', 4: 'A', 5: 'Bb', 6: 'Cb',
                             7: 'C', 8: 'Db', 9: 'D', 10: 'Eb', 11: 'E', 12: 'F',
                             100: 'Gbb', 101: 'F#', 102: 'Abb', 103: 'G#', 104: 'Bbb', 105: 'A#', 106: 'B',
                             107: 'Dbb', 108: 'C#', 109: 'Ebb', 110: 'D#', 111: 'Fb', 112: 'E#'},
                       'G': {0: 'G', 1: 'Ab', 2: 'A', 3: 'Bb', 4: 'B', 5: 'C', 6: 'Db',
                             7: 'D', 8: 'Eb', 9: 'E', 10: 'F', 11: 'F#', 12: 'G',
                             100: 'Abb', 101: 'G#', 102: 'Bbb', 103: 'A#', 104: 'Cb', 105: 'B#', 106: 'C#',
                             107: 'Ebb', 108: 'D#', 109: 'Fb', 110: 'E#', 111: 'Gb', 112: 'F##'},
                       'Ab': {0: 'Ab', 1: 'Bbb', 2: 'Bb', 3: 'Cb', 4: 'C', 5: 'Db', 6: 'Ebb',
                              7: 'Eb', 8: 'Fb', 9: 'F', 10: 'Gb', 11: 'G', 12: 'Ab',
                              100: None, 101: 'A', 102: 'Cbb', 103: 'B', 104: 'Dbb', 105: 'C#', 106: 'D',
                              107: 'Fbb', 108: 'E', 109: 'Gbb', 110: 'F#', 111: 'Abb', 112: 'G##'},
                       'Bb': {0: 'Bb', 1: 'Cb', 2: 'C', 3: 'Db', 4: 'D', 5: 'Eb', 6: 'Fb',
                              7: 'F', 8: 'Gb', 9: 'G', 10: 'Ab', 11: 'A', 12: 'Bb',
                              100: 'Cbb', 101: 'B', 102: 'Dbb', 103: 'C#', 104: 'Ebb', 105: 'D#', 106: 'E',
                              107: 'Gbb', 108: 'F#', 109: 'Abb', 110: 'G#', 111: 'Bbb', 112: 'A#'},
                       'Cb': {0: 'Cb', 1: 'Dbb', 2: 'Db', 3: 'Ebb', 4: 'Eb', 5: 'Fb', 6: 'Gbb',
                              7: 'Gb', 8: 'Abb', 9: 'Ab', 10: 'Bbb', 11: 'Bb', 12: 'Cb',
                              100: None, 101: 'C', 102: None, 103: 'D', 104: 'Fbb', 105: 'E', 106: 'F',
                              107: None, 108: 'G', 109: None, 110: 'A', 111: 'Cbb', 112: 'B'},
                       'Db': {0: 'Db', 1: 'Ebb', 2: 'Eb', 3: 'Fb', 4: 'F', 5: 'Gb', 6: 'Abb',
                              7: 'Ab', 8: 'Bbb', 9: 'Bb', 10: 'Cb', 11: 'C', 12: 'Db',
                              100: None, 101: 'D', 102: 'Fbb', 103: 'E', 104: 'Gbb', 105: 'F#', 106: 'G',
                              107: None, 108: 'A', 109: 'Cbb', 110: 'B', 111: 'Dbb', 112: 'C#'},
                       'Eb': {0: 'Eb', 1: 'Fb', 2: 'F', 3: 'Gb', 4: 'G', 5: 'Ab', 6: 'Bbb',
                              7: 'Bb', 8: 'Cb', 9: 'C', 10: 'Db', 11: 'D', 12: 'Eb',
                              100: 'Fbb', 101: 'E', 102: 'Gbb', 103: 'F#', 104: 'Abb', 105: 'G#', 106: 'A',
                              107: 'Cbb', 108: 'B', 109: 'Dbb', 110: 'C#', 111: 'Ebb', 112: 'D#'},
                       'Fb': {0: 'Fb', 1: 'Gbb', 2: 'Gb', 3: 'Abb', 4: 'Ab', 5: 'Bbb', 6: 'Cbb',
                              7: 'Cb', 8: 'Dbb', 9: 'Db', 10: 'Ebb', 11: 'Eb', 12: 'Fb',
                              100: None, 101: 'F', 102: None, 103: 'G', 104: None, 105: 'A', 106: 'Bb',
                              107: None, 108: 'C', 109: None, 110: 'D', 111: 'Fbb', 112: 'E'},
                       'Gb': {0: 'Gb', 1: 'Abb', 2: 'Ab', 3: 'Bbb', 4: 'Bb', 5: 'Cb', 6: 'Dbb',
                              7: 'Db', 8: 'Ebb', 9: 'Eb', 10: 'Fb', 11: 'F', 12: 'Gb',
                              100: None, 101: 'G', 102: None, 103: 'A', 104: 'Cbb', 105: 'B', 106: 'C',
                              107: None, 108: 'D', 109: 'Fbb', 110: 'E', 111: 'Gbb', 112: 'F#'},
                       'A#': {0: 'A#', 1: 'B', 2: 'B#', 3: 'C#', 4: 'C##', 5: 'D#', 6: 'E',
                              7: 'E#', 8: 'F#', 9: 'F##', 10: 'G#', 11: 'G##', 12: 'A#',
                              100: 'Bb', 101: 'A##', 102: 'C', 103: 'B##', 104: 'D', 105: None, 106: 'D##',
                              107: 'F', 108: 'E##', 109: 'G', 110: None, 111: 'A', 112: None},
                       'B#': {0: 'B#', 1: 'C#', 2: 'C##', 3: 'D#', 4: 'D##', 5: 'E#', 6: 'F#',
                              7: 'F##', 8: 'G#', 9: 'G##', 10: 'A#', 11: 'A##', 12: 'B#',
                              100: 'C', 101: 'B##', 102: 'D', 103: None, 104: 'E', 105: None, 106: 'E##',
                              107: 'G', 108: None, 109: 'A', 110: None, 111: 'B', 112: None},
                       'C#': {0: 'C#', 1: 'D', 2: 'D#', 3: 'E', 4: 'E#', 5: 'F#', 6: 'G',
                              7: 'G#', 8: 'A', 9: 'A#', 10: 'B', 11: 'B#', 12: 'C#',
                              100: 'Db', 101: 'C##', 102: 'Eb', 103: 'D##', 104: 'F', 105: 'E##', 106: 'F##',
                              107: 'Ab', 108: 'G##', 109: 'Bb', 110: 'A##', 111: 'C', 112: 'B##'},
                       'D#': {0: 'D#', 1: 'E', 2: 'E#', 3: 'F#', 4: 'F##', 5: 'G#', 6: 'A',
                              7: 'A#', 8: 'B', 9: 'B#', 10: 'C#', 11: 'C##', 12: 'D#',
                              100: 'Eb', 101: 'D##', 102: 'F', 103: 'E##', 104: 'G', 105: None, 106: 'G##',
                              107: 'Bb', 108: 'A##', 109: 'C', 110: 'B##', 111: 'D', 112: 'C##'},
                       'E#': {0: 'E#', 1: 'F#', 2: 'F##', 3: 'G#', 4: 'G##', 5: 'A#', 6: 'B',
                              7: 'B#', 8: 'C#', 9: 'C##', 10: 'D#', 11: 'D##', 12: 'E#',
                              100: 'F', 101: 'E##', 102: 'G', 103: None, 104: 'A', 105: None, 106: 'A##',
                              107: 'C', 108: 'B##', 109: 'D', 110: None, 111: 'E', 112: None},
                       'F#': {0: 'F#', 1: 'G', 2: 'G#', 3: 'A', 4: 'A#', 5: 'B', 6: 'C',
                              7: 'C#', 8: 'D', 9: 'D#', 10: 'E', 11: 'E#', 12: 'F#',
                              100: 'Gb', 101: 'F##', 102: 'Ab', 103: 'G##', 104: 'Bb', 105: 'A##', 106: 'B#',
                              107: 'Db', 108: 'C##', 109: 'Eb', 110: 'D##', 111: 'F', 112: 'E##'},
                       'G#': {0: 'G#', 1: 'A', 2: 'A#', 3: 'B', 4: 'B#', 5: 'C#', 6: 'D',
                              7: 'D#', 8: 'E', 9: 'E#', 10: 'F#', 11: 'F##', 12: 'G#',
                              100: 'Ab', 101: 'G##', 102: 'Bb', 103: 'A##', 104: 'C', 105: 'B##', 106: 'C##',
                              107: 'Eb', 108: 'D##', 109: 'F', 110: 'E##', 111: 'G', 112: None},
                       'Abb': {0: 'Abb', 1: None, 2: 'Bbb', 3: 'Cbb', 4: 'Cb', 5: 'Dbb', 6: None,
                               7: 'Ebb', 8: 'Fbb', 9: 'Fb', 10: 'Gbb', 11: 'Gb', 12: 'Abb',
                               100: None, 101: 'Ab', 102: None, 103: 'Bb', 104: None, 105: 'C', 106: 'Db',
                               107: None, 108: 'Eb', 109: None, 110: 'F', 111: None, 112: 'G'},
                       'Bbb': {0: 'Bbb', 1: 'Cbb', 2: 'Cb', 3: 'Dbb', 4: 'Db', 5: 'Ebb', 6: 'Fbb',
                               7: 'Fb', 8: 'Gbb', 9: 'Gb', 10: 'Abb', 11: 'Ab', 12: 'Bbb',
                               100: None, 101: 'Bb', 102: None, 103: 'C', 104: None, 105: 'D', 106: 'Eb',
                               107: None, 108: 'F', 109: None, 110: 'B', 111: None, 112: 'A'},
                       'Cbb': {0: 'Cbb', 1: None, 2: 'Dbb', 3: None, 4: 'Ebb', 5: 'Fbb', 6: None,
                               7: 'Gbb', 8: None, 9: 'Abb', 10: None, 11: 'Bbb', 12: 'Cbb',
                               100: None, 101: 'Cb', 102: None, 103: 'Db', 104: None, 105: 'Eb', 106: 'Fb',
                               107: None, 108: 'Gb', 109: None, 110: 'Ab', 111: None, 112: 'Bb'},
                       'Dbb': {0: 'Dbb', 1: None, 2: 'Ebb', 3: 'Fbb', 4: 'Fb', 5: 'Gbb', 6: None,
                               7: 'Abb', 8: None, 9: 'Bbb', 10: 'Cbb', 11: 'Cb', 12: 'Dbb',
                               100: None, 101: 'Db', 102: None, 103: 'Eb', 104: None, 105: 'F', 106: 'Gb',
                               107: None, 108: 'Ab', 109: None, 110: 'Bb', 111: None, 112: 'C'},
                       'Ebb': {0: 'Ebb', 1: 'Fbb', 2: 'Fb', 3: 'Gbb', 4: 'Gb', 5: 'Abb', 6: None,
                               7: 'Bbb', 8: 'Cbb', 9: 'Cb', 10: 'Dbb', 11: 'Db', 12: 'Ebb',
                               100: None, 101: 'Eb', 102: None, 103: 'F', 104: None, 105: 'G', 106: 'Ab',
                               107: None, 108: 'Bb', 109: None, 110: 'C', 111: None, 112: 'D'},
                       'Fbb': {0: 'Fbb', 1: None, 2: 'Gbb', 3: None, 4: 'Abb', 5: None, 6: None,
                               7: 'Cbb', 8: None, 9: 'Dbb', 10: None, 11: 'Ebb', 12: 'Fbb',
                               100: None, 101: 'Fb', 102: None, 103: 'Gb', 104: None, 105: 'Ab', 106: 'Bbb',
                               107: None, 108: 'Cb', 109: None, 110: 'Db', 111: None, 112: 'Eb'},
                       'Gbb': {0: 'Gbb', 1: None, 2: 'Abb', 3: None, 4: 'Bbb', 5: 'Cbb', 6: None,
                               7: 'Dbb', 8: None, 9: 'Ebb', 10: 'Fbb', 11: 'Fb', 12: 'Gbb',
                               100: None, 101: 'Gb', 102: None, 103: 'Ab', 104: None, 105: 'Bb', 106: 'Cb',
                               107: None, 108: 'Db', 109: None, 110: 'Eb', 111: None, 112: 'F'},
                       'A##': {0: 'A##', 1: 'B#', 2: 'B##', 3: 'C##', 4: None, 5: 'D##', 6: 'E#',
                               7: 'E##', 8: 'F##', 9: None, 10: 'G##', 11: None, 12: 'A##',
                               100: 'B', 101: None, 102: 'C#', 103: None, 104: 'D#', 105: None, 106: None,
                               107: 'F#', 108: None, 109: 'G#', 110: None, 111: 'A#', 112: None},
                       'B##': {0: 'B##', 1: 'C##', 2: None, 3: 'D##', 4: None, 5: 'E##', 6: 'F##',
                               7: None, 8: 'G##', 9: None, 10: 'A##', 11: None, 12: 'B##',
                               100: 'C#', 101: None, 102: 'D#', 103: None, 104: 'E#', 105: None, 106: None,
                               107: 'G#', 108: None, 109: 'A#', 110: None, 111: 'B#', 112: None},
                       'C##': {0: 'C##', 1: 'D#', 2: 'D##', 3: 'E#', 4: 'E##', 5: 'F##', 6: 'G#',
                               7: 'G##', 8: 'A#', 9: 'A##', 10: 'B#', 11: 'B##', 12: 'C##',
                               100: 'D', 101: None, 102: 'E', 103: None, 104: 'F#', 105: None, 106: None,
                               107: 'A', 108: None, 109: 'B', 110: None, 111: 'C#', 112: None},
                       'D##': {0: 'D##', 1: 'E#', 2: 'E##', 3: 'F##', 4: None, 5: 'G##', 6: 'A#',
                               7: 'A##', 8: 'B#', 9: 'B##', 10: 'C##', 11: None, 12: 'D##',
                               100: 'E', 101: None, 102: 'F#', 103: None, 104: 'G#', 105: None, 106: None,
                               107: 'B', 108: None, 109: 'C#', 110: None, 111: 'D#', 112: None},
                       'E##': {0: 'E##', 1: 'F##', 2: None, 3: 'G##', 4: None, 5: 'A##', 6: 'B#',
                               7: 'B##', 8: 'C##', 9: None, 10: 'D##', 11: None, 12: 'E##',
                               100: 'F#', 101: None, 102: 'G#', 103: None, 104: 'A#', 105: None, 106: None,
                               107: 'C#', 108: None, 109: 'D#', 110: None, 111: 'E#', 112: None},
                       'F##': {0: 'F##', 1: 'G#', 2: 'G##', 3: 'A#', 4: 'A##', 5: 'B#', 6: 'C#',
                               7: 'C##', 8: 'D#', 9: 'D##', 10: 'E#', 11: 'E##', 12: 'F##',
                               100: 'G', 101: None, 102: 'A', 103: None, 104: 'B', 105: None, 106: 'B##',
                               107: 'D', 108: None, 109: 'E', 110: None, 111: 'F#', 112: None},
                       'G##': {0: 'G##', 1: 'A#', 2: 'A##', 3: 'B#', 4: 'B##', 5: 'C##', 6: 'D#',
                               7: 'D##', 8: 'E#', 9: 'E##', 10: 'F##', 11: None, 12: 'G##',
                               100: 'A', 101: None, 102: 'B', 103: None, 104: 'C#', 105: None, 106: None,
                               107: 'E', 108: None, 109: 'F#', 110: None, 111: 'G#', 112: None}
                       }


class _IntervalBuilder:
    """
    This class can be used as a utility class to facilitate interval calculations. Objects store a root note as a string
    and builds intervals on that note.
    """
    def __init__(self, rootnote):
        self.rootnote = rootnote
        self.interval_steps = {'PERFECT 0': 0, 'DIMINISHED 2': 100, 'DIMINISHED 9': 100,
                               'MINOR 2': 1, 'AUGMENTED 0': 101, 'MINOR 9': 1, 'AUGMENTED 8': 101,
                               'MAJOR 2': 2, 'DIMINISHED 3': 102, 'MAJOR 9': 2, 'DIMINISHED 10': 102,
                               'MINOR 3': 3, 'AUGMENTED 2': 103, 'MINOR 10': 3, 'AUGMENTED 9': 103,
                               'MAJOR 3': 4, 'DIMINISHED 4': 104, 'MAJOR 10': 4, 'DIMINISHED 11': 104,
                               'PERFECT 4': 5, 'AUGMENTED 3': 105, 'PERFECT 11': 5, 'AUGMENTED 10': 105,
                               'DIMINISHED 5': 6, 'AUGMENTED 4': 106, 'DIMINISHED 12': 6, 'AUGMENTED 11': 106,
                               'PERFECT 5': 7, 'DIMINISHED 6': 107, 'PERFECT 12': 7, 'DIMINISHED 13': 107,
                               'MINOR 6': 8, 'AUGMENTED 5': 108, 'MINOR 13': 8, 'AUGMENTED 12': 108,
                               'MAJOR 6': 9, 'DIMINISHED 7': 109, 'MAJOR 13': 9, 'DIMINISHED 14': 109,
                               'MINOR 7': 10, 'AUGMENTED 6': 110, 'MINOR 14': 10, 'AUGMENTED 13': 110,
                               'MAJOR 7': 11, 'DIMINISHED 8': 111, 'MAJOR 14': 11, 'DIMINISHED 15': 111,
                               'PERFECT 8': 12, 'AUGMENTED 7': 112, 'PERFECT 15': 0, 'AUGMENTED 14': 109,
                               'AUGMENTED 15': 101
                               }

    def ascend_interval_from_name(self, qualified_interval_name):
        """
        Ascend a specified interval from the root note.

        :raises: InvalidIntervalError: If ascending the specified interval from the root would result in an
            invalid note, such as a triple sharp or triple flat.
        """
        try:
            qualified_interval_name = qualified_interval_name.upper()
            number_of_steps = self.interval_steps[qualified_interval_name]
        except KeyError:
            raise InvalidIntervalError("Invalid interval name: %s" % qualified_interval_name) from None

        interval_top_note = INTERVAL_NOTE_PAIRS[self.rootnote][number_of_steps]
        return interval_top_note

    def descend_interval_from_name(self, qualified_interval_name):
        """
        Descend a specified interval from the root note.

        :raises: InvalidIntervalError: If descending the specified interval from the root would result in an
            invalid note, such as a triple sharp or triple flat.
        """
        try:
            qualified_interval_name = qualified_interval_name.upper()
            number_of_steps = self.interval_steps[qualified_interval_name]
        except KeyError:
            raise InvalidIntervalError("Invalid interval name: %s" % qualified_interval_name) from None
        interval_bottom_note = _fetch_interval_bottom_note(self.rootnote, number_of_steps)
        return interval_bottom_note


def _fetch_interval_bottom_note(qualified_note_name, steps):
    if steps >= 100:  # Most diminished and augmented intervals, except for diminished 5, have an interval code over 100
        if steps % 10 == 6:  # augmented 4 is encoded as 106. Its compliment is a diminished 5, or six steps.
            steps_compliment = 6
        else:
            steps_compliment = 12 - (steps % 100) + 100
    else:
        if steps == 6:  # diminished 5 compliment is an augmented 4, which is encoded as 106.
            steps_compliment = 106
        else:
            steps_compliment = 12 - steps
    return INTERVAL_NOTE_PAIRS[qualified_note_name][steps_compliment]


class InvalidIntervalError(Exception):
    """
    Raised when an interval would result in an invalid top (ascending) or bottom (descending) note, e.g. a diminished
    third ascending from Gb would technically be a Bbbb (B triple flat). While this is enharmonically equivalent to Ab,
    Gb to Ab is a major second, not a diminished third. Because the technically correct note is not a valid note name,
    an InvalidIntervalError should be raised.
    """
    pass
