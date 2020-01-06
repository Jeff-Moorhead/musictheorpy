from unittest import TestCase

from .. import chords
from ..notegroups import InvalidDegreeError, InvalidQualityError


class TestChords(TestCase):
    def setUp(self):
        self.c_thirteen = chords.Chord('C DOMINANT 13')
        self.c_major = chords.Chord('c major')
        self.d_minor = chords.Chord('d minor')

    def test_invalid_bass(self):
        with self.assertRaises(chords.InvalidBassError):
            z = chords.Chord('Z MAJOR')

    def test_invalid_quality(self):
        with self.assertRaises(InvalidQualityError):
            a = chords.Chord('A Foo')

    def test_getitem_bass(self):
        c = self.c_thirteen['bass']
        self.assertEqual(c, 'C')

    def test_getitem_third(self):
        e = self.c_thirteen['THIRD']
        self.assertEqual(e, 'E')

    def test_getitem_fifth(self):
        g = self.c_thirteen['FIFTH']
        self.assertEqual(g, 'G')

    def test_getitem_seventh(self):
        b_flat = self.c_thirteen['SEVENTH']
        self.assertEqual(b_flat, 'Bb')

    def test_getitem_ninth(self):
        d = self.c_thirteen['NINTH']
        self.assertEqual(d, 'D')

    def test_getitem_eleventh(self):
        f = self.c_thirteen['ELEVENTH']
        self.assertEqual(f, 'F')

    def test_getitem_thirteenth(self):
        a = self.c_thirteen['THIRTEENTH']
        self.assertEqual(a, 'A')

    def test_getitem_nonexistant_degree(self):
        b_flat = self.c_major['SEVENTH']
        self.assertTrue(b_flat is None)

    def test_getitem_invalid_degree(self):
        with self.assertRaises(InvalidDegreeError):
            bad_degree = self.c_major['baddeg']
