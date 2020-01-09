from .interval_utils import _IntervalBuilder

VALID_NOTES = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
VALID_QUALIFIERS = ['', '#', '##', 'b', 'bb']
VALID_QUALIFIED_NAMES = [name + qualifier for name in VALID_NOTES for qualifier in VALID_QUALIFIERS]


class Note:
    def __init__(self, qualified_name):
        """
        :param qualified_name: The qualified name of the note. The note's qualified name is the note
        name, optionally followed by the qualifier. Valid note names are English capital letters A through G. Valid
        qualifiers are # (sharp), b (flat), ## (double sharp), bb (double flat). Note that flats must be lowercase or
        a NoteNameError is raised. A note name followed by no qualifier represents a natural, e.g. 'A' represents 'A
        natural'. If an invalid qualified note name is passed, a NoteNameError is raised. Once a Note object is created,
        it's qualified name should not be modified.
        """
        self.qualified_name = qualified_name
        self._interval_builder = _IntervalBuilder(self.qualified_name)

    @property
    def qualified_name(self):
        return self._qualified_name

    @qualified_name.setter
    def qualified_name(self, name):
        name = str(name)[0].upper() + str(name)[1:]
        if name not in VALID_QUALIFIED_NAMES:
            raise NoteNameError("Invalid note name: %s." % name)
        else:
            self._qualified_name = name

    def __str__(self):
        return self.qualified_name

    def __repr__(self):
        return self.qualified_name

    def __eq__(self, other):
        return self.qualified_name == other.qualified_name

    def ascend_interval(self, qualified_interval_name):
        """
        :param str qualified_interval_name: The interval to ascend, e.g. major 3.
        :return: A Note object representing the top note of the interval. If the top note of the interval is not
        a valid note, such as F###, and InvalidIntervalError is raised.
        """
        try:
            return Note(self._interval_builder.ascend_interval_from_name(qualified_interval_name))
        except NoteNameError:
            raise NoteNameError("Ascending a %s from %s results in an invalid note." % (qualified_interval_name,
                                                                                        self._qualified_name)) from None

    def descend_interval(self, qualified_interval_name):
        """
        :param qualified_interval_name: the interval to fetch, e.g. major 3.
        :return: a Note object representing the bottom note of the interval. If the bottom note of the interval is not
        a valid note, such as F###, an InvalidInvervalError is raised.
        """
        try:
            return Note(self._interval_builder.descend_interval_from_name(qualified_interval_name))
        except NoteNameError:
            raise NoteNameError("Descending a %s from %s results in an invalid note." % (qualified_interval_name,
                                                                                         self._qualified_name)) from None

    def find_interval_from_root(self, top_note):
        """
        :param top_note: a string that is
        :return <str> interval: the interval at which the top note is in relation from the root
        """
        root_note = self.qualified_name
        try:
            note_name = Note(top_note).qualified_name
            top_note = note_name.upper() if len(note_name) == 1 else note_name[:1].upper() + note_name[1:]
        except NoteNameError:
            raise NoteNameError("%s is an invalid note." % top_note) from None

        return self._interval_builder.find_interval_from_root(root_note, top_note)


class NoteNameError(Exception):
    """
    Raised when attempting to create a Note object with a qualified note name that is not valid.
    """
    pass
