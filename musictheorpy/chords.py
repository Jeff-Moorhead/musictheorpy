from .notegroups import NoteGroup, InvalidDegreeError


class Chord(NoteGroup):
    def __init__(self, qualified_name):
        """
        MAJOR, MINOR, DIMINISHED, and AUGMENTED qualities are triads. Anything with a
        number (e.g. MAJOR 7) produces a four-or-more-note chord.
        """
        super().__init__('CHORD', qualified_name)

    def __getitem__(self, element):
        degree_names = {'BASS': 0, 'THIRD': 1, 'FIFTH': 2, 'SEVENTH': 3}
        chord_degree = degree_names[element]
        try:
            return self.notes[chord_degree]
        except IndexError:
            raise InvalidDegreeError
