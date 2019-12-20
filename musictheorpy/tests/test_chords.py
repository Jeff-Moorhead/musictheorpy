from unittest import TestCase

from .. import chords
from ..notegroups import InvalidDegreeError


class TestChords(TestCase):
    def setUp(self) -> None:
        self.testchord = chords.Chord('C DOMINANT 7')
        self.testtriad = chords.Chord('C MAJOR')

    def test_getitem_bass(self):
        c = self.testchord['BASS']
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

    def test_getitem_raises(self):
        with self.assertRaises(InvalidDegreeError):
            b_flat = self.testtriad['SEVENTH']
