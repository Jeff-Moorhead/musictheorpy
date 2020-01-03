import abc
from . import interval_utils


class _IntervalBuilder:
    def __init__(self, rootnote, intervalgroup=None):
        self.intervalgroup = intervalgroup
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
        try:
            qualified_interval_name = qualified_interval_name.upper()
            number_of_steps = self.interval_steps[qualified_interval_name]
        except KeyError:
            raise interval_utils.InvalidIntervalError("Invalid interval name: %s" % qualified_interval_name) from None

        interval_top_note = interval_utils.INTERVAL_NOTE_PAIRS[self.rootnote][number_of_steps]
        return interval_top_note

    def descend_interval_from_name(self, qualified_interval_name):
        try:
            qualified_interval_name = qualified_interval_name.upper()
            number_of_steps = self.interval_steps[qualified_interval_name]
        except KeyError:
            raise interval_utils.InvalidIntervalError("Invalid interval name: %s" % qualified_interval_name) from None
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
    return interval_utils.INTERVAL_NOTE_PAIRS[qualified_note_name][steps_compliment]


class _NoteGroup(abc.ABC):
    @abc.abstractmethod
    def __init__(self, grouptype, qualified_name):
        """ Represents a group such as a scale or chord """
        builder = _get_group_builder(grouptype)  # get the function that builds the group
        unpacked_name = _unpack_group_name(qualified_name)
        self._validate_root(unpacked_name)
        self.root = unpacked_name['ROOT'].upper()
        self.quality = unpacked_name['QUALITY'].upper()
        try:
            self.notes = builder(self.root, self.quality)
        except KeyError:
            raise InvalidQualityError("Quality %s is not valid" % self.quality) from None

    def _validate_root(self, unpacked_name):
        """ Needed to validate the root of certain subclasses """
        pass

    def __str__(self):
        return str(self.notes)

    def __repr__(self):
        return str(self.notes)

    @abc.abstractmethod
    def __getitem__(self, item):
        pass

    def __contains__(self, note):
        note = note[0].upper() + note[1:]
        return note in self.notes


def _get_group_builder(grouptype):
    if grouptype == 'SCALE':
        return _build_scale
    elif grouptype == 'CHORD':
        return _build_chord


def _build_scale(root, quality):
    scale_intervals = {'MAJOR': [0, 2, 4, 5, 7, 9, 11],
                       'NATURAL MINOR': [0, 2, 3, 5, 7, 8, 10],
                       'HARMONIC MINOR': [0, 2, 3, 5, 7, 8, 11],
                       'MELODIC MINOR': [0, 2, 3, 5, 7, 9, 11],
                       }
    return _build_group(root, scale_intervals[quality])


def _build_chord(root, quality):
    chord_intervals = {'MAJOR': [0, 4, 7],
                       'MINOR': [0, 3, 7],
                       'DIMINISHED': [0, 3, 6],
                       'AUGMENTED': [0, 4, 108],
                       'DOMINANT 7': [0, 4, 7, 10],
                       'MAJOR 7': [0, 4, 7, 11],
                       'MINOR 7': [0, 3, 7, 10],
                       'MINOR 7b5': [0, 3, 6, 10],
                       'DOMINANT 9': [0, 4, 7, 10, 2],
                       'DOMINANT b9': [0, 4, 7, 10, 1],
                       'DOMINANT #9': [0, 4, 7, 10, 103],
                       'MAJOR 9': [0, 4, 7, 11, 2],
                       'MINOR 9': [0, 3, 7, 10, 2],
                       'DOMINANT 11': [0, 4, 7, 10, 2, 5],
                       'DOMINANT b11': [0, 4, 7, 10, 2, 104],
                       'DOMINANT #11': [0, 4, 7, 10, 2, 106],
                       'MAJOR 11': [0, 4, 7, 11, 2, 5],
                       'MINOR 11': [0, 3, 7, 10, 2, 5],
                       'DOMINANT 13': [0, 4, 7, 10, 2, 5, 9],
                       'DOMINANT b13': [0, 4, 7, 10, 2, 5, 8],
                       'DOMINANT #13': [0, 4, 7, 10, 2, 5, 110],
                       'MAJOR 13': [0, 4, 7, 11, 2, 5, 9],
                       'MINOR 13': [0, 3, 7, 10, 2, 5, 9]
                       }
    return _build_group(root, chord_intervals[quality])


def _build_group(root, intervals):
    # build a group of notes (scale, triad, chord) from root using the list of intervals.
    return tuple([interval_utils.INTERVAL_NOTE_PAIRS[root][interval] for interval in intervals])


def _unpack_group_name(groupname):
    split_group = groupname.split(' ', 1)
    try:
        root = split_group[0]
        quality = split_group[1]
    except IndexError:
        raise InvalidQualityError("No quality given.") from None
    return {'ROOT': root, 'QUALITY': quality}


class InvalidDegreeError(Exception):
    """
    Raised when an attempting to fetch an invalid scale degree name. Valid scale degree names are
    tonic, supertonic, mediant, subdominant, dominant, submediant, and leading tone.
    """
    pass


class InvalidQualityError(Exception):
    """
    Raised when the quality of a scale or chord is invalid.
    """
    pass
