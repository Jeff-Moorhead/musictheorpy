import musictheorpy.scales as scales
from .intervalsmain import get_note_obj


def get_minor_scale(tonic, minor):
    if minor.upper() not in ['NATURAL', 'HARMONIC', 'MELODIC']:
        return None

    qualified_scalename = f"{tonic} {minor.upper()} MINOR"
    return get_scale_obj(qualified_scalename)


def get_scale_obj(scalename):
    try:
        return scales.Scale(scalename)
    except scales.InvalidTonicError:
        return None


def unpack_scale_arguments(args):
    currentargs = []
    note = get_note_obj(args.tonic)
    currentargs.append(note)

    if args.minor:
        currentargs.append(args.minor)
    else:
        currentargs.append(None)

    if args.degree:
        currentargs.append(args.degree)
    else:
        currentargs.append(None)

    if args.number:
        currentargs.append(args.number)
    else:
        currentargs.append(None)

    if args.relative:
        currentargs.append(True)
    else:
        currentargs.append(False)

    if args.parallel:
        currentargs.append(True)
    else:
        currentargs.append(False)

    return currentargs  # return value should be unpacked into individual variables
