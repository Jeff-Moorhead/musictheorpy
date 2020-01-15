from .notegroups import _NoteGroup, InvalidDegreeError
from .chords import Chord


class Scale(_NoteGroup):
    """
    Represents a collection of notes. Scales are built from a series of whole and half steps and have a key signature
    and tonic. Each note in a scale is identified either by a number (1 through 7) or a degree name. Valid tonics are
    English letters A through G, and valid qualities are MAJOR, HARMONIC MINOR, MELODIC MINOR, and NATURAL MINOR. An
    InvalidTonicError is raised if the scale name has a key signature involving double sharps or double flats.
    """
    _VALID_SCALE_NAMES = {'MAJOR': ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                                    'C#', 'F#',
                                    'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Gb'],
                          'MINOR': ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                                    'A#', 'D#', 'G#', 'C#', 'F#',
                                    'Ab', 'Eb', 'Bb']}

    _SHARPS = ['F#', 'C#', 'G#', 'D#', 'A#', 'E#', 'B#']
    _FLATS = ['Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb', 'Fb']

    _KEY_SIGNATURE_NUMBERS = {'C MAJOR': 0, 'G MAJOR': 1, 'D MAJOR': 2, 'A MAJOR': 3, 'E MAJOR': 4, 'B MAJOR': 5,
                              'F# MAJOR': 6, 'C# MAJOR': 7,
                              'F MAJOR': -1, 'Bb MAJOR': -2, 'Eb MAJOR': -3, 'Ab MAJOR': -4, 'Db MAJOR': -5,
                              'Gb MAJOR': -6, 'Cb MAJOR': -7,
                              'A MINOR': 0, 'E MINOR': 1, 'B MINOR': 2, 'F# MINOR': 3, 'C# MINOR': 4, 'G# MINOR': 5,
                              'D# MINOR': 6, 'A# MINOR': 7,
                              'D MINOR': -1, 'G MINOR': -2, 'C MINOR': -3, 'F MINOR': -4, 'Bb MINOR': -5,
                              'Eb MINOR': -6, 'Ab MINOR': -7}

    _KEY_SIGNATURES = {0: [], 1: _SHARPS[:1], 2: _SHARPS[:2], 3: _SHARPS[:3], 4: _SHARPS[:4], 5: _SHARPS[:5],
                       6: _SHARPS[:6], 7: _SHARPS[:7],
                       -1: _FLATS[:1], -2: _FLATS[:2], -3: _FLATS[:3], -4: _FLATS[:4], -5: _FLATS[:5],
                       -6: _FLATS[:6], -7: _FLATS[:7]}

    def __init__(self, qualified_name):
        super().__init__('SCALE', qualified_name)
        self.key_signature = Scale._fetch_key_signature(self.root, self.quality)

    def __getitem__(self, degree):
        """
        :param degree: a string representing the scale degree, such as TONIC, MEDIANT.
        :return: a Note object representing the scale degree.
        """
        degree_names = {'TONIC': 0, 'SUPERTONIC': 1, 'MEDIANT': 2, 'SUBDOMINANT': 3,
                        'DOMINANT': 4, 'SUBMEDIANT': 5, 'SEVENTH': 6, 'LEADING TONE': 6}

        try:
            degree = degree.upper()
            degree_number = degree_names[degree]
            return self.notes[degree_number]
        except KeyError:
            raise InvalidDegreeError('Invalid degree name: %s' % degree) from None

    def get_relative(self):
        """
        Returns the relative major or minor of the current scale.

        :rtype: Scale
        """
        if self.quality == 'MAJOR':
            relative_quality = 'NATURAL MINOR'
            relative_tonic = self.__getitem__('SUBMEDIANT')
        else:
            relative_quality = 'MAJOR'
            relative_tonic = self.__getitem__('MEDIANT')
        qualified_relative_name = '%s %s' % (relative_tonic, relative_quality)
        return Scale(qualified_relative_name)

    def get_parallel(self):
        """
        Returns the parallel major or minor of the current scale.

        :rtype: Scale
        """
        if self.quality == 'MAJOR':
            parallel_quality = 'NATURAL MINOR'
        else:
            parallel_quality = 'MAJOR'
        qualified_parallel_name = '%s %s' % (self.root, parallel_quality)
        return Scale(qualified_parallel_name)

    def get_triad_for_degree(self, degree):
        """
        Builds a triad based on the current scale's quality and the given degree.

        :param degree: a string representing the scale degree, such as TONIC, MEDIANT.
        :raises: InvalidDegreeError
        :return: a Chord object with the scale degree as its root.
        """
        degree = degree.upper()
        if self.quality == 'MAJOR':
            triad_qualities = {'TONIC': 'MAJOR', 'SUPERTONIC': 'MINOR', 'MEDIANT': 'MINOR', 'SUBDOMINANT': 'MAJOR',
                               'DOMINANT': 'MAJOR', 'SUBMEDIANT': 'MINOR', 'SEVENTH': 'DIMINISHED', 'LEADING TONE': 'DIMINISHED'}
        elif self.quality == 'NATURAL MINOR':
            triad_qualities = {'TONIC': 'MINOR', 'SUPERTONIC': 'DIMINISHED', 'MEDIANT': 'MAJOR', 'SUBDOMINANT': 'MINOR',
                               'DOMINANT': 'MINOR', 'SUBMEDIANT': 'MAJOR', 'SEVENTH': 'MAJOR', 'LEADING TONE': 'MAJOR'}
        elif self.quality == 'HARMONIC MINOR':
            triad_qualities = {'TONIC': 'MINOR', 'SUPERTONIC': 'DIMINISHED', 'MEDIANT': 'AUGMENTED',
                               'SUBDOMINANT': 'MINOR', 'DOMINANT': 'MAJOR', 'SUBMEDIANT': 'MAJOR', 'SEVENTH': 'DIMINISHED',
                               'LEADING TONE': 'DIMINISHED'}
        else:
            triad_qualities = {'TONIC': 'MINOR', 'SUPERTONIC': 'MINOR', 'MEDIANT': 'AUGMENTED', 'SUBDOMINANT': 'MAJOR',
                               'DOMINANT': 'MAJOR', 'SUBMEDIANT': 'DIMINISHED', 'SEVENTH': 'DIMINISHED',
                               'LEADING TONE': 'DIMINISHED'}

        triad_root = self.__getitem__(degree)  # Raises InvalidDegreeError
        triad_quality = triad_qualities[degree]
        triad_name = "%s %s" % (triad_root, triad_quality)
        return Chord(triad_name)

    def _validate_root(self, unpacked_name):
        """
        Ensures that the tonic of the scale is valid.

        :param list unpacked_name: The qualified name of the scale unpacked into a list.
        :raises: InvalidTonicError: If the tonic is an invalid note or if the key signature of the
            scale would contain double sharps or double flats.
        """
        if 'MINOR' in unpacked_name['QUALITY']:
            valid_tonics = Scale._VALID_SCALE_NAMES['MINOR']
        else:
            valid_tonics = Scale._VALID_SCALE_NAMES['MAJOR']

        if unpacked_name['ROOT'] not in valid_tonics:
            raise InvalidTonicError(
                "Invalid tonic: %s. It is possible that this tonic is a valid note name but that "
                "building the desired scale from this note would result in a scale with an invalid "
                "key signature." % unpacked_name['ROOT'])

    @classmethod
    def _fetch_key_signature(cls, tonic, quality):
        """ Returns a list of strings with the note names that make up the scale's key signature. """
        qualified_tonic = tonic + (' MINOR' if 'MINOR' in quality else ' MAJOR')
        key_signature_number = cls._KEY_SIGNATURE_NUMBERS[qualified_tonic]
        return tuple(cls._KEY_SIGNATURES[key_signature_number])


class InvalidTonicError(Exception):
    """
    Raised when attempting to create a Scale object with an invalid tonic. This situation could arise from attempting to
    create a Scale object with a tonic that is greater than G, or when attempting to create a Scale object with a valid
    tonic name (that is an English letter between A and G), but for whom the passed quality would result in a scale that
    includes invalid note names in its key signature, such as double sharps. An example of this situation is a G# Major
    scale.
    """
    pass
