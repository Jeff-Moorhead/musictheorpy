from . import interval_utils


class NoteGroup:
    """ Not intended for instantiation. Subclass only. """
    def __init__(self, grouptype, qualified_name):
        """ Group type is the type (e.g. SCALE, CHORD) in all caps """
        builder = get_group_builder(grouptype)  # get the function that builds the group
        unpacked_name = unpack_group_name(qualified_name)
        self.validate_root(unpacked_name)
        self.root = unpacked_name['ROOT']
        self.quality = unpacked_name['QUALITY']
        self.notes = builder(self.root, self.quality)

    def validate_root(self, unpacked_name):
        """ Needed to validate the root of certain subclasses """
        pass

    def __getitem__(self, item):
        pass

    def __contains__(self, note):
        return note in self.notes

    def ascend(self):
        return tuple([note for note in self.notes])


def get_group_builder(grouptype):
    if grouptype == 'SCALE':
        return build_scale
    elif grouptype == 'CHORD':
        return build_chord


def build_scale(root, quality):
    return build_group(root, interval_utils.SCALE_INTERVALS[quality])


def build_chord(root, quality):
    return build_group(root, interval_utils.CHORD_INTERVALS[quality])


def build_group(root, intervals):
    # build a group of notes (scale, triad, chord) from root using the list of intervals.
    return tuple([interval_utils.INTERVAL_NOTE_PAIRS[root][interval] for interval in intervals])


def unpack_group_name(groupname):
    split_group = groupname.split(' ', 1)
    root = split_group[0]
    quality = split_group[1]
    return {'ROOT': root, 'QUALITY': quality}


class InvalidDegreeError(Exception):
    """
    Raised when an attempting to fetch an invalid scale degree name. Valid scale degree names are
    tonic, supertonic, mediant, subdominant, dominant, submediant, and leading tone.
    """
    pass