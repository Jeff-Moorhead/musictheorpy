from .notegroups import _NoteGroup, InvalidDegreeError


class Chord(_NoteGroup):
    def __init__(self, qualified_name):
        """
        MAJOR, MINOR, DIMINISHED, and AUGMENTED qualities are triads. Anything with a
        number (e.g. MAJOR 7) produces a four-or-more-note chord.
        """
        qualified_name = qualified_name.upper()
        super().__init__('CHORD', qualified_name)

    def __getitem__(self, element):
        degree_names = {'BASS': 0, 'THIRD': 1, 'FIFTH': 2, 'SEVENTH': 3, 'NINTH': 4, 'ELEVENTH': 5, 'THIRTEENTH': 6}
        try:
            element = element.upper()
            chord_degree = degree_names[element]
            return self.notes[chord_degree]
        except (IndexError, KeyError):
            raise InvalidDegreeError("Invalid degree name: %s" % element) from None

    def _validate_root(self, unpacked_name):
        valid_roots = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        valid_qualifiers = ['', '#', '##', 'b', 'bb']
        valid_qualified_roots = [root + qualifier for root in valid_roots for qualifier in valid_qualifiers]
        if unpacked_name['ROOT'] not in valid_qualified_roots:
            raise InvalidBassError("Invalid bass note: %s" % unpacked_name['ROOT'])


class InvalidBassError(Exception):
    pass
