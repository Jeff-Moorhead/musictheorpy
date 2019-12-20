"""
=========
scales.py
=========

Provides tools to perform calculations related to scales, such as determining key signatures, and building scales of
different qualities.

Classes
-------
-Scale
   Represents a scale and facilitates key signature and note calculations.

Exceptions
----------
- InvalidTonicError
   Raised when a tonic results in an invalid key signature.
-InvalidDegreeError
   Raised when accessing an invalid scale degree.

"""
import musictheorpy.interval_utils as int_utils

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


class Scale(int_utils.NoteGroup):
    """
    Represents a collection of notes. Scales are built from a series of whole and half steps and have a key signature
    and tonic. Each note in a scale is identified either by a number (1 through 7) or a degree name. Valid tonics are
    English letters A through G, and valid qualities are MAJOR, HARMONIC MINOR, MELODIC MINOR, and NATURAL MINOR. An
    InvalidTonicError is raised if the scale name has a key signature involving double sharps or double flats.

    Attributes
    ----------
    key_signature
       A list of note names indicating the sharp or flat notes for the given scale. An empty list represents all
       natural notes.
    """
    def __init__(self, qualified_name):
        super().__init__('SCALE', qualified_name)
        self.key_signature = fetch_key_signature(self.root, self.quality)

    def __getitem__(self, degree):
        """
        :param degree: a string representing the scale degree, such as TONIC, MEDIANT, etc. degree should be all caps.
        :return: a Note object representing the scale degree.
        """
        if self.quality != 'MAJOR' and 'MINOR' not in self.quality:
            raise InvalidDegreeError("Only major and minor scales are subscriptable")

        degree_names = {'TONIC': 0, 'SUPERTONIC': 1, 'MEDIANT': 2, 'SUBDOMINANT': 3,
                        'DOMINANT': 4, 'SUBMEDIANT': 5, 'LEADING TONE': 6}

        try:
            degree_number = degree_names[degree]
            return self.notes[degree_number]
        except KeyError:
            raise InvalidDegreeError('Invalid degree name: %s' % degree)

    def __contains__(self, note):
        return note in self.notes

    def ascend(self):
        """
        :return: a list of strings representing the qualified names of each note in this scale, in ascending order.
        """
        return tuple([note for note in self.notes])

    def validate_root(self, unpacked_name):
        if 'MINOR' in unpacked_name['QUALITY']:
            valid_tonics = VALID_SCALE_NAMES['MINOR']
        else:
            valid_tonics = VALID_SCALE_NAMES['MAJOR']

        if unpacked_name['ROOT'] not in valid_tonics:
            raise InvalidTonicError(
                "Invalid tonic: %s. It is possible that this tonic is a valid note name but that "
                "building the desired scale from this note would result in a scale with an invalid "
                "key signature." % unpacked_name['ROOT'])


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
    # return a list of strings representing the scale's key signature. C major and A minor scales return an empty list.
    qualified_tonic = tonic + (' MINOR' if 'MINOR' in quality else ' MAJOR')
    key_signature_number = KEY_SIGNATURE_NUMBERS[qualified_tonic]
    return KEY_SIGNATURES[key_signature_number]
