# test with mocking _parser.parse_args()

from unittest import TestCase, mock
from argparse import Namespace
from musictheorpy.console.parser import PyMusicArgumentParser


class TestParser(TestCase):
    @mock.patch('argparse.ArgumentParser.parse_args')
    def test_parser(self, parsemock):
        parsemock.return_value = Namespace(starting_note='A#', interval='P5')

        intervalparser = PyMusicArgumentParser()
        intervalargs = intervalparser._args
        self.assertEqual(intervalargs.starting_note, 'A#')
        self.assertEqual(intervalargs.interval, 'PERFECT 5')

    @mock.patch('argparse.ArgumentParser.parse_args')
    def test_invalid_args(self, parsemock):
        parsemock.return_value = Namespace(starting_note='q###', interval='w21')

        invalidparser = PyMusicArgumentParser()
        invalidargs = invalidparser._args
        self.assertEqual(invalidargs.starting_note, 'q###')
        self.assertTrue(invalidargs.interval is None)

    @mock.patch('argparse.ArgumentParser.parse_args')
    def test_pack(self, parsemock):
        parsemock.return_value = Namespace(starting_note='A#', interval='m3')

        intervalparser = PyMusicArgumentParser()
        intervalargs = intervalparser.pack()

        self.assertEqual(intervalargs['starting_note'], 'A#')
