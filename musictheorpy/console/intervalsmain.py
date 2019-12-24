import musictheorpy.notes as notes


def get_note_obj(notename):
    try:
        return notes.Note(notename)
    except notes.NoteNameError:
        return None