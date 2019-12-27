# Musictheorpy

Musictheorpy is a Python library to perform musical calculations,
including intervals, triads/chords, and scales. The following modules
are available to use
- musictheorpy.notes
- musictheorpy.scales
- musictheorpy.chords

All other modules contain implementation details and should not be
imported by clients.

Notes
-----


#####*class* Note  
The Note class is built with a string representing a qualified note name. The 
qualified note name should be an uppercase letter A - G, 
optionally followed by a qualifier. Valid qualifiers are `#`, `##`, `b`, and 
`bb` (lowercase B). A note name with no qualifier is also allowed and represents a natural. 
For example, `Note('A')`, `Note('C#')`, and `Note('Gb')` are all valid, while 
`Note('H')` and `Note('Fbbb')` are invalid. If the client attempts to create
a Note object with an invalid qualified note name, a NoteNameError is raised.  

Note objects expose the following public methods:
- ascend_interval
- descend_interval

Both ascend_ and descend_interval accept a string representing a
qualified interval name. Qualified interval names are comprised of
an all-uppercase quality followed by an interval number. Valid qualities
are MAJOR, MINOR, PERFECT, AUGMENTED, and DIMINISHED. Valid interval numbers
are 0 - 15. Standard music theory nomenclature applies, i.e. fourths,
fifths, unisons, octaves, elevenths, twelfths, and fifteenths can only be
perfect, diminished, or augmented, while all other intervals can only be
major, minor, diminished, or augmented. 
  
Both methods return a Note object representing the note at
the other end of the given interval. For example,
```
>>> c = Note('C')
>>> a = c.ascend_interval('MAJOR 6')
>>> a.qualified_name
'A'
>>>
``` 
In this example, we start with C, and ascend a major sixth, which is an A.

descend_interval is functionally identical, except that it descends the given
interval. For example,
```
>>> c = Note('C')
>>> a = c.descend_interval('MINOR 3')
>>> a.qualified_name
'A'
>>>
```
In some cases, an interval name may be perfectly valid, but the note on the other
side of the interval is not a valid note. This is particularly common in flat and sharp
notes. For example, ascending an augmented third (`AUGMENTED 3`) from A# would
technically result in a C###, which is not considered valid. In this case, an `NoteNameError`
is raised to inform the client that the given interval is not valid for the starting note.   

If the qualified interval name passed to either method is itself invalid, for example `MAJOR 5`,
then an `InvalidIntervalException` is raised.

Scales
------

#####*class* Scale
A scale object is constructed with a string representing the qualified scale
name. The qualified scale name consists of an uppercase tonic followed by a
uppercase scale quality. Valid tonics are letters A - G. Valid qualities are
MAJOR, HARMONIC MINOR, MELODIC MINOR, and NATURAL MINOR. If an invalid tonic
passed, an InvalidTonicError is raised. If an invalid quality is passed, an
InvalidQualityError is raised. For example,

```
>>> c = Scale('C MAJOR')
>>> c_harm = Scale('C HARMONIC MINOR')
>>> c_badquality = Scale('C Foo')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/jmoorhead/projects/musictheorpy/musictheorpy/scales.py", line 36, in __init__
    super().__init__('SCALE', qualified_name)
  File "/home/jmoorhead/projects/musictheorpy/musictheorpy/notegroups.py", line 74, in __init__
    raise InvalidQualityError("Quality %s is not valid" % self.quality) from None
musictheorpy.notegroups.InvalidQualityError: Quality Foo is not valid
>>> c_badtonic = Scale('Z MAJOR')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/jmoorhead/projects/musictheorpy/musictheorpy/scales.py", line 36, in __init__
    super().__init__('SCALE', qualified_name)
  File "/home/jmoorhead/projects/musictheorpy/musictheorpy/notegroups.py", line 68, in __init__
    self._validate_root(unpacked_name)
  File "/home/jmoorhead/projects/musictheorpy/musictheorpy/scales.py", line 66, in _validate_root
    "key signature." % unpacked_name['ROOT'])
musictheorpy.scales.InvalidTonicError: Invalid tonic: Z. It is possible that this tonic is a valid 
note name but that building the desired scale from this note would result in a scale with an invalid 
key signature.
```

As indicated in the trace back for `c_badtonic` above, it is possible to pass a valid note name
to `Scale`, but still receive an InvalidTonicError. This occurs when the
key signature of the given scale name would include qualifiers beyond sharps and flats.
For example, G# Major would have F## in its key signature. Because key signatures like
this are generally not used in music theory, they are not valid.  

The key signature of a `Scale` object is accessible through its
`key_signature` property, which is a tuple of strings representing the
notes that make up the scale's key signature. For example,
```
>>> a_major = Scale('A MAJOR')
>>> a_major.key_signature
('F#', 'C#', 'G#')
>>> e_minor = Scale('E NATURAL MINOR')
>>> 'F#' in e_minor.key_signature
True
```

In addition, you can access all the notes in the scale through the
object's `notes` attribute, which provides a tuple of strings representing
all the notes in the scale. Finally, `Scale` objects implement the 
`__getitem__` and `__contains__` magic methods. The `__getitem__` method
allows lookup of notes in a scale by degree name. Valid degree names are
TONIC, SUPERTONIC, MEDIANT, SUBDOMINANT, DOMINANT, SUBMEDIANT, and 
LEADING TONE. Note that degree names must be all uppercase. For example,
```
>>> a_major = Scale('A MAJOR')
>>> a_major['TONIC']
'A'
>>> a_major['SUBMEDIANT']
'F#'
```

Finally, users can test if a note is in a given scale using Python's
built-in `in` keyword, thanks to the `__contains__` method.
```
>>> a_major = Scale('A MAJOR')
>>> 'F#' in a_major
True
>>> 'B#' in a_major
False
```

Chords
------
Properties: root (bass), notes, quality
Behaviors: get relative/parallel, get element, get note number, possibly validate tonic
