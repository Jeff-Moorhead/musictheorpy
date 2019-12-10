from unittest import TestCase

from .. import interval_utils


class TestNoteGroups(TestCase):
    def test_build_group_scale(self):
        c_scale_intervals = interval_utils.SCALE_INTERVALS['MAJOR']
        c_scale_from_func = interval_utils.build_group('C', c_scale_intervals)
        c_scale_test = ('C', 'D', 'E', 'F', 'G', 'A', 'B')
        self.assertEqual(c_scale_from_func, c_scale_test)

    def test_build_group_triad(self):
        c_triad_intervals = interval_utils.TRIAD_INTERVALS['MAJOR']
        c_triad_from_func = interval_utils.build_group('C', c_triad_intervals)
        c_triad_test = ('C', 'E', 'G')
        self.assertEqual(c_triad_from_func, c_triad_test)

    def test_build_group_chord(self):
        c_seventh_intervals = interval_utils.CHORD_INTERVALS['DOMINANT 7']
        c_seventh_from_func = interval_utils.build_group('C', c_seventh_intervals)
        c_seventh_test = ('C', 'E', 'G', 'Bb')
        self.assertEqual(c_seventh_from_func, c_seventh_test)
