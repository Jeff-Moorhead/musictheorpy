from unittest import TestCase

from .. import chords


class TestChords(TestCase):
    def test_major_triad_intervals(self):
        major_triad_intervals = [0, 4, 7]
        major_triad = chords.Chord('C', 'MAJOR')
        self.assertEqual(major_triad_intervals, major_triad.intervals)

    def test_minor_triad_intervals(self):
        minor_triad_intervals = [0, 3, 7]
        minor_triad = chords.Chord('C', 'MINOR')
        self.assertEqual(minor_triad_intervals, minor_triad.intervals)

    def test_c_major_triad(self):
        c_major_triad = ('C', 'E', 'G')
        triad_from_func = chords.Chord('C', 'MAJOR')
        self.assertEqual(c_major_triad, triad_from_func._notes)

    def test_a_minor_triad(self):
        a_minor_triad = ('A', 'C', 'E')
        triad_from_func = chords.Chord('A', 'MINOR')
        self.assertEqual(a_minor_triad, triad_from_func._notes)
