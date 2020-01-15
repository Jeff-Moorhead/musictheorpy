import unittest
from ..scales import Scale, InvalidTonicError
from ..notegroups import InvalidQualityError, InvalidDegreeError
from ..chords import Chord


class TestScale(unittest.TestCase):
    def setUp(self):
        self.c_scale = Scale('c major')
        self.b_flat = Scale('Bb major')
        self.d_harm_minor = Scale('D harmonic minor')

    def test_scale(self):
        c_note_names = ('C', 'D', 'E', 'F', 'G', 'A', 'B')
        self.assertEqual(self.c_scale.root, 'C')
        self.assertEqual(self.c_scale.key_signature, ())
        self.assertEqual(self.c_scale.quality, 'MAJOR')
        self.assertEqual(self.c_scale.notes, c_note_names)

        bflat_notes = ('Bb', 'C', 'D', 'Eb', 'F', 'G', 'A')
        self.assertEqual(self.b_flat.root, 'Bb')
        self.assertEqual(self.b_flat.key_signature, ('Bb', 'Eb'))
        self.assertEqual(self.b_flat.notes, bflat_notes)

        d_min_note_names = ('D', 'E', 'F', 'G', 'A', 'Bb', 'C#')
        self.assertEqual(self.d_harm_minor.root, 'D')
        self.assertEqual(self.d_harm_minor.key_signature, ('Bb',))
        self.assertEqual(self.d_harm_minor.quality, 'HARMONIC MINOR')
        self.assertEqual(self.d_harm_minor.notes, d_min_note_names)

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

    def test_get_relative_minor(self):
        a_minor = self.c_scale.get_relative()
        self.assertEqual(a_minor.notes, ('A', 'B', 'C', 'D', 'E', 'F', 'G'))

    def test_get_relative_major(self):
        f_major = self.d_harm_minor.get_relative()
        self.assertEqual(f_major.notes, ('F', 'G', 'A', 'Bb', 'C', 'D', 'E'))

    def test_get_parallel_minor(self):
        c_minor = self.c_scale.get_parallel()
        self.assertEqual(c_minor.notes, ('C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'))

    def test_get_parallel_major(self):
        d_major = self.d_harm_minor.get_parallel()
        self.assertEqual(d_major.notes, ('D', 'E', 'F#', 'G', 'A', 'B', 'C#'))

    def test_get_triad_for_degree(self):
        e_minor = self.c_scale.get_triad_for_degree('mediant')
        to_compare = Chord('E minor')
        self.assertEqual(e_minor, to_compare)

    def test_get_triad_raises(self):
        with self.assertRaises(InvalidDegreeError):
            bad = self.c_scale.get_triad_for_degree('foo')
