import unittest
from musictheorpy.scales import Scale, InvalidDegreeError, InvalidTonicError
from musictheorpy.notes import Note


class TestScale(unittest.TestCase):
    def setUp(self):
        self.c_scale = Scale('C MAJOR')
        self.d_harm_minor = Scale('D HARMONIC MINOR')

    def test_scale(self):
        c_note_names = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        c_notes = [Note(name) for name in c_note_names]
        self.assertEqual(self.c_scale.tonic, 'C')
        self.assertEqual(self.c_scale.key_signature, [])
        self.assertEqual(self.c_scale.quality, 'MAJOR')
        self.assertEqual(self.c_scale._notes, c_notes)

        d_min_note_names = ['D', 'E', 'F', 'G', 'A', 'Bb', 'C#']
        d_min_notes = [Note(name) for name in d_min_note_names]
        self.assertEqual(self.d_harm_minor.tonic, 'D')
        self.assertEqual(self.d_harm_minor.key_signature, ['Bb'])
        self.assertEqual(self.d_harm_minor.quality, 'HARMONIC MINOR')
        self.assertEqual(self.d_harm_minor._notes, d_min_notes)

    def test_getitem(self):
        self.assertEqual(self.c_scale['SUBMEDIANT'], Note('A'))

        self.assertEqual(self.d_harm_minor['SUBDOMINANT'], Note('G'))

    def test_contains(self):
        self.assertTrue(Note('G') in self.c_scale)
        self.assertFalse(Note('D#') in self.c_scale)
        self.assertTrue(Note('Bb') in self.d_harm_minor)
        self.assertFalse(Note('F#') in self.d_harm_minor)

    def test_ascend(self):
        self.assertEqual(self.c_scale.ascend(), ['C', 'D', 'E', 'F', 'G', 'A', 'B'])

    def test_invalid_degree(self):
        with self.assertRaises(InvalidDegreeError):
            bad_degree = self.c_scale['foobar']

    def test_invalid_tonic(self):
        with self.assertRaises(InvalidTonicError):
            z = Scale('Z MAJOR')
