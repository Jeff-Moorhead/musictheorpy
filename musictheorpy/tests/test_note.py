import unittest
from ..notes import Note, NoteNameError, InvalidIntervalError
from ..interval_utils import INTERVAL_NOTE_PAIRS
from ..notegroups import IntervalBuilder


class TestNote(unittest.TestCase):
    def setUp(self):
        self.a = Note('A')
        self.c = Note('C')
        self.a_flat = Note('Ab')
        self.builder = IntervalBuilder('A')

    def test_ascend_interval(self):
        for interval, steps in self.builder.interval_steps.items():
            top_note = INTERVAL_NOTE_PAIRS['A'][steps]
            self.assertEqual(self.a.ascend_interval(interval), Note(top_note))

    def test_descend_interval(self):
        c = self.a.descend_interval("MAJOR 6")
        self.assertEqual(c, Note('C'))

    def test_invalid_qualified_name(self):
        with self.assertRaises(NoteNameError):
            z_sharp = Note('z#')

    def test_invalid_type(self):
        with self.assertRaises(NoteNameError):
            two = Note(2)

    def test_invalid_interval(self):
        with self.assertRaises(InvalidIntervalError):
            self.a_flat.ascend_interval('DIMINISHED 2')


if __name__ == '__main__':
    unittest.main()
