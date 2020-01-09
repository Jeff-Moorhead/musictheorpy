from .notegroups import _NoteGroup, InvalidDegreeError
from .notes import VALID_QUALIFIED_NAMES


class Chord(_NoteGroup):
    def __init__(self, qualified_name):
        """
        MAJOR, MINOR, DIMINISHED, and AUGMENTED qualities are triads. Anything with a
        number (e.g. MAJOR 7) produces a four-or-more-note chord.
        """
        super().__init__('CHORD', qualified_name)

    def __getitem__(self, element):
        degree_names = {'BASS': 0, 'THIRD': 1, 'FIFTH': 2, 'SEVENTH': 3, 'NINTH': 4, 'ELEVENTH': 5, 'THIRTEENTH': 6}
        try:
            element = element.upper()
            chord_degree = degree_names[element]
            return self.notes[chord_degree]
        except IndexError:
            return None
        except KeyError:
            raise InvalidDegreeError("Invalid degree name: %s" % element) from None

    def _validate_root(self, unpacked_name):
        if unpacked_name['ROOT'] not in VALID_QUALIFIED_NAMES:
            raise InvalidBassError("Invalid bass note: %s" % unpacked_name['ROOT'])


class InvalidBassError(Exception):
    """
    Raised when attempting to create a Chord object with an invalid bass note.
    """
    pass
