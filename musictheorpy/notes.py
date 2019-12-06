"""
========
notes.py
========

Provides an interface for performing calculations related to individual notes, such as ascending and descending
intervals.

Classes
-------
- Note
   Represents an individual note.

Exceptions
----------
- NoteNameError
   Raised when a note name is not valid.
"""
from musictheorpy.interval_utils import INTERVAL_NOTE_PAIRS, INTERVAL_STEPS, InvalidIntervalError

VALID_NOTES = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
VALID_QUALIFIERS = ['', '#', '##', 'b', 'bb']
VALID_QUALIFIED_NAMES = [name + qualifier for name in VALID_NOTES for qualifier in VALID_QUALIFIERS]


class Note:
    """
    Represent individual notes. Notes are the atomic element in Western music theory and are comprised of a note name
    and an optional qualifier.

    Public Attributes
    -----------------
    qualified_name - Note name followed by an optional qualifier.
    """
    def __init__(self, qualified_name):
        """
        :param qualified_name: The qualified name of the note. The note's qualified name is the capitalized note
        name, optionally followed by the qualifier. Valid note names are English capital letters A through G. Valid
        qualifiers are # (sharp), b (flat), ## (double sharp), bb (double flat). Note that flats must be lowercase or
        a NoteNameError is raised. A note name followed by no qualifier represents a natural, e.g. 'A' represents 'A
        natural'. If an invalid qualified note name is passed, a NoteNameError is raised. Once a Note object is created,
        it's qualified name should not be modified.
        """
        self.qualified_name = qualified_name

    @property
    def qualified_name(self):
        return self._qualified_name

    @qualified_name.setter
    def qualified_name(self, name):
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
        :param str qualified_interval_name: the interval to fetch. Interval quality should be all caps, e.g. MAJOR 3
        :return: a Note object representing the top note of the interval. If the top note of the interval is not
        a valid note, such as F###, a note object with a qualified name of Z# is returned.
        """
        try:
            number_of_steps = INTERVAL_STEPS[qualified_interval_name]
            interval_top_note = INTERVAL_NOTE_PAIRS[self._qualified_name][number_of_steps]
            return Note(interval_top_note)
        except NoteNameError:
            raise InvalidIntervalError("Ascending a %s from %s results in an invalid note." % (qualified_interval_name,
                                                                                               self._qualified_name))

    def descend_interval(self, qualified_interval_name):
        """
        :param qualified_interval_name: the interval to fetch. Interval quality should be all caps, e.g. MAJOR 3
        :return: a Note object representing the bottom note of the interval. If the bottom note of the interval is not
        a valid note, such as F###, a note object with a qualified name of Z# is returned.
        """
        try:
            number_of_steps = INTERVAL_STEPS[qualified_interval_name]
            interval_bottom_note = fetch_interval_bottom_note(self._qualified_name, number_of_steps)
            return Note(interval_bottom_note)
        except NoteNameError:
            raise InvalidIntervalError("Descending a %s from %s results in an invalid note." % (qualified_interval_name,
                                                                                                self._qualified_name))


class NoteNameError(Exception):
    """
    Raised when attempting to create a Note object with a qualified note name that is not valid.
    """
    pass


def fetch_interval_bottom_note(qualified_note_name, steps):
    # Finds the bottom note of an interval. Compliment to the interval is 12 - steps
    if steps >= 100:  # Most diminished and augmented intervals, except for diminished 5, have an interval code over 100
        if steps % 10 == 6:  # augmented 4 compliment is a diminished 5
            steps_compliment = 6
        else:
            steps_compliment = 12 - (steps % 100) + 100
    else:
        if steps == 6:  # diminished 5 compliment is an augmented 4
            steps_compliment = 106
        else:
            steps_compliment = 12 - steps
    return INTERVAL_NOTE_PAIRS[qualified_note_name][steps_compliment]
