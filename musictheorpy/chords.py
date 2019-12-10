"""
Classes for triads and chords.
"""
import musictheorpy.interval_utils as int_utils


class Chord:
    def __init__(self, root, quality):
        """
        MAJOR, MINOR, DIMINISHED, and AUGMENTED qualities are triads. Anything with a
        number (e.g. MAJOR 7) produces a four-or-more-note chord.
        """
        self.root = root
        self.quality = quality
        self.intervals = int_utils.CHORD_INTERVALS[quality]
        self._notes = int_utils.build_group(root, self.intervals)
