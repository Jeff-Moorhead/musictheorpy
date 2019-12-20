from unittest import TestCase, mock

from .. import pymusic


class TestPyMusic(TestCase):
    @mock.patch('argparse.Namespace')
    def test_unpack_args(self, namespace_mock):
        namespace_ascending = namespace_mock
        namespace_ascending.startingnote = 'A'
        namespace_ascending.interval = 'M3'
        namespace_ascending.descend = False

        note, interval, descend = pymusic.unpack_interval_arguments(namespace_ascending)
        self.assertTrue(note is not None)
        self.assertEqual(interval, 'MAJOR 3')
        self.assertFalse(descend)

    @mock.patch('argparse.Namespace')
    def test_invalid_args(self, namespace_mock):
        # tests pymusic.unpack args, and consequently tests pymusic.get_note_obj and pymusic.map_interval
        namespace_invalid = namespace_mock
        namespace_invalid.startingnote = 'foo'
        namespace_invalid.interval = 'bar'
        namespace_invalid.descend = False

        invalid_note, invalid_interval, descend = pymusic.unpack_interval_arguments(namespace_invalid)
        self.assertTrue(invalid_note is None and invalid_interval is None)
