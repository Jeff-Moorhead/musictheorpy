import unittest
from musictheorpy.notes import Note, NoteNameError, InvalidIntervalError
from musictheorpy.interval_utils import INTERVAL_NOTE_PAIRS, INTERVAL_STEPS


class TestNote(unittest.TestCase):
    def setUp(self):
        self.a = Note('A')
        self.c = Note('C')
        self.a_flat = Note('Ab')

    def test_ascend_interval(self):
        for interval, steps in INTERVAL_STEPS.items():
            top_note = INTERVAL_NOTE_PAIRS['A'][steps]
            self.assertEqual(self.a.ascend_interval(interval), Note(top_note))

    def test_descend_interval(self):
        for note, pairs in INTERVAL_NOTE_PAIRS.items():
            for interval, steps in INTERVAL_STEPS.items():
                if steps >= 100:
                    if steps % 10 == 6:  # augmented 4 compliment is a diminished 5
                        steps_compliment = 6
                    else:
                        steps_compliment = 12 - (steps % 100) + 100
                else:
                    if steps == 6:  # diminished 5 compliment is an augmented 4
                        steps_compliment = 106
                    else:
                        steps_compliment = 12 - steps

                try:
                    bottom_note = INTERVAL_NOTE_PAIRS[note][steps_compliment]
                except KeyError:
                    failure_msg = f"Starting_note: {note}, Bottom note: {bottom_note}, Steps: {steps}, Interval: {interval}"
                    print(failure_msg)

                this_note = Note(note)
                # print('Starting note: %s\nBottom note: %s\nInterval: %s' % (note, bottom_note, interval))

                failure_msg = f"Starting_note: {note}, Bottom note: {bottom_note}, Steps: {steps}, Interval: {interval}"
                if bottom_note is None:
                    with self.assertRaises(InvalidIntervalError):
                        this_note.descend_interval(interval)
                else:
                    self.assertEqual(this_note.descend_interval(interval), Note(bottom_note), failure_msg)

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
