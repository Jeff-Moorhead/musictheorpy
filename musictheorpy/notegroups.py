import abc
from . import interval_utils


class _NoteGroup(abc.ABC):
    """
    An abstract base class used to define an interface for note groups, such as scales and chords.
    """
    @abc.abstractmethod
    def __init__(self, grouptype, qualified_name):
        """ Represents a group such as a scale or chord """
        builder = _get_group_builder(grouptype)  # get the function that builds the group
        unpacked_name = _unpack_group_name(qualified_name)
        self._validate_root(unpacked_name)
        self.root = unpacked_name['ROOT']
        self.quality = unpacked_name['QUALITY']
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

    def __eq__(self, other):
        return self.notes == other.notes

    @abc.abstractmethod
    def __getitem__(self, item):
        pass

    def __contains__(self, note):
        note = note[0].upper() + note[1:]
        return note in self.notes


def _unpack_group_name(groupname):
    split_group = groupname.split(' ', 1)
    try:
        root = split_group[0][0].upper() + split_group[0][1:]
        quality = split_group[1].upper()
    except IndexError:
        raise InvalidQualityError("No quality given.") from None
    return {'ROOT': root, 'QUALITY': quality}


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
