""" Classes and functions to implement scales """
from musictheorpy.interval_utils import SCALE_INTERVALS, INTERVAL_NOTE_PAIRS
from musictheorpy.notes import Note

VALID_SCALE_NAMES = {'MAJOR': ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                               'C#', 'F#',
                               'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Gb'],
                     'MINOR': ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                               'A#', 'D#', 'G#', 'C#', 'F#',
                               'Ab', 'Eb', 'Bb']}

SHARPS = ['F#', 'C#', 'G#', 'D#', 'A#', 'E#', 'B#']
FLATS = ['Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb', 'Fb']

KEY_SIGNATURE_NUMBERS = {'C MAJOR': 0, 'G MAJOR': 1, 'D MAJOR': 2, 'A MAJOR': 3, 'E MAJOR': 4, 'B MAJOR': 5,
                         'F# MAJOR': 6, 'C# MAJOR': 7,
                         'F MAJOR': -1, 'Bb MAJOR': -2, 'Eb MAJOR': -3, 'Ab MAJOR': -4, 'Db MAJOR': -5,
                         'Gb MAJOR': -6, 'Cb MAJOR': -7,
                         'A MINOR': 0, 'E MINOR': 1, 'B MINOR': 2, 'F# MINOR': 3, 'C# MINOR': 4, 'G# MINOR': 5,
                         'D# MINOR': 6, 'A# MINOR': 7,
                         'D MINOR': -1, 'G MINOR': -2, 'C MINOR': -3, 'F MINOR': -4, 'Bb MINOR': -5,
                         'Eb MINOR': -6, 'Ab MINOR': -7}

KEY_SIGNATURES = {0: [], 1: SHARPS[:1], 2: SHARPS[:2], 3: SHARPS[:3], 4: SHARPS[:4], 5: SHARPS[:5],
                  6: SHARPS[:6], 7: SHARPS[:7],
                  -1: FLATS[:1], -2: FLATS[:2], -3: FLATS[:3], -4: FLATS[:4], -5: FLATS[:5],
                  -6: FLATS[:6], -7: FLATS[:7]}


def build_scale(tonic, quality):
    """
    :param tonic: a string representing the tonic of the scale.
    :param quality: a string indicating the quality of the scale.
    :return: a list of Note objects in the scale.
    """
    scale_intervals = SCALE_INTERVALS[quality]
    scale_note_names = [INTERVAL_NOTE_PAIRS[tonic][interval] for interval in scale_intervals]
    return tuple([Note(note_name) for note_name in scale_note_names])


class Scale:
    def __init__(self, scale_name):
        """
        :param scale_name: a string representing the scale name and quality, e.g. C NATURAL MINOR. Scale_name should be
        all caps.
        """
        unpacked_scale_name = unpack_scale_name(scale_name)
        validate_tonic(unpacked_scale_name)

        self._tonic = unpacked_scale_name['TONIC']
        self._quality = unpacked_scale_name['QUALITY']
        self._notes = build_scale(self._tonic, self._quality)
        self.key_signature = fetch_key_signature(self._tonic, self._quality)

    def __getitem__(self, degree):
        """
        :param degree: a string representing the scale degree, such as TONIC, MEDIANT, etc. degree should be all caps.
        :return: a Note object representing the scale degree.
        """
        if self._quality != 'MAJOR' and 'MINOR' not in self._quality:
            raise InvalidDegreeError("Only major and minor scales are subscriptable")

        degree_names = {'TONIC': 0, 'SUPERTONIC': 1, 'MEDIANT': 2, 'SUBDOMINANT': 3,
                        'DOMINANT': 4, 'SUBMEDIANT': 5, 'LEADING TONE': 6}

        try:
            degree_number = degree_names[degree]
            return self._notes[degree_number]
        except KeyError:
            raise InvalidDegreeError('Invalid degree name: %s' % degree)

    def __contains__(self, note):
        return note in self._notes

    def ascend(self):
        """
        :return: a list of strings representing the qualified names of each note in this scale, in ascending order.
        """
        return tuple([note.qualified_name for note in self._notes])


class InvalidTonicError(Exception):
    """
    Raised when attempting to create a Scale object with an invalid tonic. This situation could arise from attempting to
    create a Scale object with a tonic that is greater than G, or when attempting to create a Scale object with a valid
    tonic name (that is an English letter between A and G), but for whom the passed quality would result in a scale that
    includes invalid note names in its key signature, such as double sharps. An example of this situation is a G# Major
    scale.
    """
    pass


class InvalidDegreeError(Exception):
    """
    Raised when an attempting to fetch an invalid scale degree name. Valid scale degree names are
    tonic, supertonic, mediant, subdominant, dominant, submediant, and leading tone.
    """
    pass


def fetch_key_signature(tonic, quality):
    """
    :param tonic: a string representing the scale's tonic note.
    :param quality: a string representing the scale's quality. Valid qualities are MAJOR, NATURAL MINOR, HARMONIC MINOR
    and MELODIC MINOR.
    :return: a list of strings representing the scale's key signature. C major and A minor scales return an empty list.
    """
    qualified_tonic = tonic + (' MINOR' if 'MINOR' in quality else ' MAJOR')
    key_signature_number = KEY_SIGNATURE_NUMBERS[qualified_tonic]
    return KEY_SIGNATURES[key_signature_number]


def unpack_scale_name(scale):
    """
    :param scale: a string consisting of the desired scale's tonic followed by the quality.
    :return: a dictionary containing the tonic and quality of the scale as string.
    """
    split_scale = scale.split(' ', 1)
    tonic = split_scale[0]
    quality = split_scale[1]
    return {'TONIC': tonic, 'QUALITY': quality}


def validate_tonic(unpacked_scale_name):
    """
    :param unpacked_scale_name: a dictionary of the unpacked scale data.
    :return: None. Raise an InvalidTonicError if the scale name is invalid.
    """
    if 'MINOR' in unpacked_scale_name['QUALITY']:
        valid_tonics = VALID_SCALE_NAMES['MINOR']
    else:
        valid_tonics = VALID_SCALE_NAMES['MAJOR']

    if unpacked_scale_name['TONIC'] not in valid_tonics:
        raise InvalidTonicError("Invalid tonic: %s. It is possible that this tonic is a valid note name but that "
                                "building the desired scale from this note would result in a scale with an invalid "
                                "key signature." % unpacked_scale_name['TONIC'])

# TODO: Implement a main() for cli
