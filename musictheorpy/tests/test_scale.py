import unittest
from ..scales import Scale, InvalidTonicError
from ..notegroups import InvalidQualityError, InvalidDegreeError


class TestScale(unittest.TestCase):
    def setUp(self):
        self.c_scale = Scale('c major')
        self.d_harm_minor = Scale('D harmonic minor')

    def test_scale(self):
        c_note_names = ('C', 'D', 'E', 'F', 'G', 'A', 'B')
        c_notes = tuple([name for name in c_note_names])
        self.assertEqual(self.c_scale.root, 'C')
        self.assertEqual(self.c_scale.key_signature, ())
        self.assertEqual(self.c_scale.quality, 'MAJOR')
        self.assertEqual(self.c_scale.notes, c_notes)

        d_min_note_names = ('D', 'E', 'F', 'G', 'A', 'Bb', 'C#')
        d_min_notes = tuple([name for name in d_min_note_names])
        self.assertEqual(self.d_harm_minor.root, 'D')
        self.assertEqual(self.d_harm_minor.key_signature, ('Bb',))
        self.assertEqual(self.d_harm_minor.quality, 'HARMONIC MINOR')
        self.assertEqual(self.d_harm_minor.notes, d_min_notes)

    def test_getitem(self):
        self.assertEqual(self.c_scale['submediant'], 'A')

        self.assertEqual(self.d_harm_minor['SUBDOMINANT'], 'G')

    def test_contains(self):
        self.assertTrue('g' in self.c_scale)
        self.assertFalse('D#' in self.c_scale)
        self.assertTrue('Bb' in self.d_harm_minor)
        self.assertFalse('F#' in self.d_harm_minor)

    def test_invalid_degree(self):
        with self.assertRaises(InvalidDegreeError):
            bad_degree = self.c_scale['foobar']

    def test_invalid_tonic(self):
        with self.assertRaises(InvalidTonicError):
            z = Scale('Z MAJOR')

    def test_raises_invalidquality(self):
        with self.assertRaises(InvalidQualityError):
            z = Scale('A Badqual')
