from unittest import TestCase

from .. import chords
from ..notegroups import InvalidDegreeError, InvalidQualityError


class TestChords(TestCase):
    def setUp(self):
        self.testchord = chords.Chord('C DOMINANT 13')
        self.testtriad = chords.Chord('c major')

    def test_invalid_bass(self):
        with self.assertRaises(chords.InvalidBassError):
            z = chords.Chord('Z MAJOR')

    def test_invalid_quality(self):
        with self.assertRaises(InvalidQualityError):
            a = chords.Chord('A Foo')

    def test_getitem_bass(self):
        c = self.testchord['bass']
        self.assertEqual(c, 'C')

    def test_getitem_third(self):
        e = self.testchord['THIRD']
        self.assertEqual(e, 'E')

    def test_getitem_fifth(self):
        g = self.testchord['FIFTH']
        self.assertEqual(g, 'G')

    def test_getitem_seventh(self):
        b_flat = self.testchord['SEVENTH']
        self.assertEqual(b_flat, 'Bb')

    def test_getitem_ninth(self):
        d = self.testchord['NINTH']
        self.assertEqual(d, 'D')

    def test_getitem_eleventh(self):
        f = self.testchord['ELEVENTH']
        self.assertEqual(f, 'F')

    def test_getitem_thirteenth(self):
        a = self.testchord['THIRTEENTH']
        self.assertEqual(a, 'A')

    def test_getitem_invalid_degree(self):
        with self.assertRaises(InvalidDegreeError):
            b_flat = self.testtriad['SEVENTH']
