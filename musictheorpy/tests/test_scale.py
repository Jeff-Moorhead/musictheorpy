import unittest
from musictheorpy.scales import Scale, InvalidDegreeError, InvalidTonicError


class TestScale(unittest.TestCase):
    def setUp(self):
        self.c_scale = Scale('C MAJOR')
        self.d_harm_minor = Scale('D HARMONIC MINOR')

    def test_scale(self):
        c_note_names = ('C', 'D', 'E', 'F', 'G', 'A', 'B')
        c_notes = tuple([name for name in c_note_names])
        self.assertEqual(self.c_scale.root, 'C')
        self.assertEqual(self.c_scale.key_signature, [])
        self.assertEqual(self.c_scale.quality, 'MAJOR')
        self.assertEqual(self.c_scale.notes, c_notes)

        d_min_note_names = ('D', 'E', 'F', 'G', 'A', 'Bb', 'C#')
        d_min_notes = tuple([name for name in d_min_note_names])
        self.assertEqual(self.d_harm_minor.root, 'D')
        self.assertEqual(self.d_harm_minor.key_signature, ['Bb'])
        self.assertEqual(self.d_harm_minor.quality, 'HARMONIC MINOR')
        self.assertEqual(self.d_harm_minor.notes, d_min_notes)

    def test_getitem(self):
        self.assertEqual(self.c_scale['SUBMEDIANT'], 'A')

        self.assertEqual(self.d_harm_minor['SUBDOMINANT'], 'G')

    def test_contains(self):
        self.assertTrue('G' in self.c_scale)
        self.assertFalse('D#' in self.c_scale)
        self.assertTrue('Bb' in self.d_harm_minor)
        self.assertFalse('F#' in self.d_harm_minor)

    def test_ascend(self):
        self.assertEqual(self.c_scale.ascend(), ('C', 'D', 'E', 'F', 'G', 'A', 'B'))

    def test_invalid_degree(self):
        with self.assertRaises(InvalidDegreeError):
            bad_degree = self.c_scale['foobar']

    def test_invalid_tonic(self):
        with self.assertRaises(InvalidTonicError):
            z = Scale('Z MAJOR')
