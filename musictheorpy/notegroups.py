import abc
from . import interval_utils, notes


class IntervalBuilder:
    def __init__(self, rootnote, intervalgroup=None):
        self.intervalgroup = intervalgroup
        self.rootnote = rootnote
        self.interval_steps = {'PERFECT 0': 0, 'DIMINISHED 2': 100,
                               'MINOR 2': 1, 'AUGMENTED 0': 101, 'MINOR 9': 1,
                               'MAJOR 2': 2, 'DIMINISHED 3': 102, 'MAJOR 9': 2,
                               'MINOR 3': 3, 'AUGMENTED 2': 103, 'MINOR 10': 3,
                               'MAJOR 3': 4, 'DIMINISHED 4': 104, 'MAJOR 10': 4,
                               'PERFECT 4': 5, 'AUGMENTED 3': 105, 'PERFECT 11': 5,
                               'DIMINISHED 5': 6, 'AUGMENTED 4': 106, 'DIMINISHED 12': 6,
                               'PERFECT 5': 7, 'DIMINISHED 6': 107, 'PERFECT 12': 7,
                               'MINOR 6': 8, 'AUGMENTED 5': 108, 'MINOR 13': 8,
                               'MAJOR 6': 9, 'DIMINISHED 7': 109, 'MAJOR 13': 9,
                               'MINOR 7': 10, 'AUGMENTED 6': 110, 'MINOR 14': 10,
                               'MAJOR 7': 11, 'DIMINISHED 8': 111, 'MAJOR 14': 11,
                               'PERFECT 8': 12, 'AUGMENTED 7': 112, 'PERFECT 15': 0, 'DIMINISHED 9': 100
                               }

    def ascend_interval_from_name(self, qualified_interval_name):
        """
        :param str qualified_interval_name: The interval to ascend. Interval quality should be all caps, e.g. MAJOR 3.
        :return: A Note object representing the top note of the interval. If the top note of the interval is not
        a valid note, such as F###, and InvalidIntervalError is raised.
        """
        number_of_steps = self.interval_steps[qualified_interval_name]
        interval_top_note = interval_utils.INTERVAL_NOTE_PAIRS[self.rootnote][number_of_steps]
        return notes.Note(interval_top_note)

    def descend_interval_from_name(self, qualified_interval_name):
        number_of_steps = self.interval_steps[qualified_interval_name]
        interval_bottom_note = fetch_interval_bottom_note(self.rootnote, number_of_steps)
        return notes.Note(interval_bottom_note)


def fetch_interval_bottom_note(qualified_note_name, steps):
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


class NoteGroup(abc.ABC):
    @abc.abstractmethod
    def __init__(self, grouptype, qualified_name):
        """ Group type is the type (e.g. SCALE, CHORD) in all caps """
        builder = get_group_builder(grouptype)  # get the function that builds the group
        unpacked_name = unpack_group_name(qualified_name)
        self.validate_root(unpacked_name)
        self.root = unpacked_name['ROOT']
        self.quality = unpacked_name['QUALITY']
        self.notes = builder(self.root, self.quality)

    def validate_root(self, unpacked_name):
        """ Needed to validate the root of certain subclasses """
        pass

    @abc.abstractmethod
    def __getitem__(self, item):
        pass

    def __contains__(self, note):
        return note in self.notes


def get_group_builder(grouptype):
    if grouptype == 'SCALE':
        return build_scale
    elif grouptype == 'CHORD':
        return build_chord


def build_scale(root, quality):
    return build_group(root, interval_utils.SCALE_INTERVALS[quality])


def build_chord(root, quality):
    return build_group(root, interval_utils.CHORD_INTERVALS[quality])


def build_group(root, intervals):
    # build a group of notes (scale, triad, chord) from root using the list of intervals.
    return tuple([interval_utils.INTERVAL_NOTE_PAIRS[root][interval] for interval in intervals])


def unpack_group_name(groupname):
    split_group = groupname.split(' ', 1)
    root = split_group[0]
    quality = split_group[1]
    return {'ROOT': root, 'QUALITY': quality}


class InvalidDegreeError(Exception):
    """
    Raised when an attempting to fetch an invalid scale degree name. Valid scale degree names are
    tonic, supertonic, mediant, subdominant, dominant, submediant, and leading tone.
    """
    pass
