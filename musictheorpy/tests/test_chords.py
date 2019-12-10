from unittest import TestCase

from .. import chords


class TestChords(TestCase):
    def test_get_stack_intervals_triad(self):
        major_triad_intervals = [0, 4, 7]
        intervals_from_func = chords.get_stack_intervals('TRIAD', 'MAJOR')
        self.assertEqual(major_triad_intervals, intervals_from_func)
