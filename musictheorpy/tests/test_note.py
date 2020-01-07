import unittest
from ..notes import Note, NoteNameError
from ..interval_utils import INTERVAL_NOTE_PAIRS, _IntervalBuilder, InvalidIntervalError


class TestNote(unittest.TestCase):
    def setUp(self):
        self.a = Note('a')
        self.c = Note('C')
        self.a_flat = Note('Ab')
        self.builder = _IntervalBuilder('A')

    def test_ascend_interval(self):
        for interval, steps in self.builder.interval_steps.items():
            top_note = INTERVAL_NOTE_PAIRS['A'][steps]
            self.assertEqual(self.a.ascend_interval(interval), Note(top_note))

    def test_descend_interval(self):
        c = self.a.descend_interval("major 6")
        self.assertEqual(c, Note('C'))

    def test_invalid_qualified_name(self):
        with self.assertRaises(NoteNameError):
            z_sharp = Note('z#')

    def test_invalid_interval(self):
        with self.assertRaises(NoteNameError):
            self.a_flat.ascend_interval('DIMINISHED 2')

    def test_invalid_interval_name(self):
        with self.assertRaises(InvalidIntervalError):
            self.a_flat.ascend_interval('bad interval')


if __name__ == '__main__':
    unittest.main()
