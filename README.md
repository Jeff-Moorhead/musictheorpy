# Musictheorpy

Musictheorpy is a Python library to perform musical calculations,
including intervals, triads/chords, and scales.

Installation
------------
Musictheorpy is free to use and modify under the MIT license. To install the package, simply run `pip install musictheorpy`.
Note that only Python version 3.6 and above are officially supported. If you do not want
to use pip for whatever reason, you can also download the source from Github at https://github.com/Jeff-Moorhead/musictheorpy
and install the package from source. Once musictheorpy is installed, feel free to run the tests found in musictheorpy/tests 
using `nosetests` to make sure everything is working as expected. Once you have the library
installed, continue to the API reference below.

Contributing
------------
Musictheorpy is under active development and will grow to include new features in the future. I am always open
to hearing people's ideas, so if you have a thought on how the project can improve, please
feel free to send me an email at **jeff.moorhead1@gmail.com** with your name, thoughts on improving the library, and 
how I can best contact you to continue the discussion. I only ask that you be patient, as between work, graduate school,
and life, it may take me a few days to respond.  

Happy coding!


API Reference
-------------
All of the classes below can be accessed directly from within the musictheorpy namespace, for example:
```
>>> import musictheorpy
>>> note = musictheorpy.Note('A')
```

Notes
-----


##### *class* Note(*qualified_name*)
Note objects are composed of a string representing a qualified note name. The 
qualified note name should be a letter A through G, 
optionally followed by a qualifier. Valid qualifiers are `#`, `##`, `b`, and 
`bb` (lowercase B). A note name with no qualifier is also allowed and represents a natural. 
For example, `Note('A')`, `Note('C#')`, and `Note('Gb')` are all valid, while 
`Note('H')` and `Note('Fbbb')` are invalid. Note that note names can be lowercase or 
uppercase, but qualifiers must be lowercase (e.g. `Note('ab')` is valid, but `Note('aB')` is not). 
If you attempt to create a Note object with an invalid qualified note name, a NoteNameError is raised.  

Note objects expose the following public methods:
- ascend_interval(*qualified_interval*)
- descend_interval(*qualified_interval*)

Both ascend_ and descend_interval accept a string representing a
qualified interval name. Qualified interval names are comprised of
a quality followed by an interval number. Valid qualities
are major, minor, perfect, augmented, and diminished. Valid interval numbers
are 0 - 15. Standard music theory nomenclature applies, i.e. fourths,
fifths, unisons, octaves, elevenths, twelfths, and fifteenths can only be
perfect, diminished, or augmented, while all other intervals can only be
major, minor, diminished, or augmented. 
  
Both methods return a Note object representing the note at
the other end of the given interval. For example,
```
>>> c = Note('C')
>>> a = c.ascend_interval('major 6')
>>> a.qualified_name
'A'
>>>
``` 
In this example, we start with C, and ascend a major sixth, which is an A.

descend_interval is functionally identical, except that it descends the given
interval. For example,
```
>>> c = Note('C')
>>> a = c.descend_interval('minor 3')
>>> a.qualified_name
'A'
>>>
```
In some cases, an interval name may be perfectly valid, but the note on the other
side of the interval is not a valid note. This is particularly common in flat and sharp
notes. For example, ascending an augmented third (`augmented 3`) from A# would
technically result in a C###, which is not considered valid. In this case, a NoteNameError
is raised to inform the client that the given interval is not valid for the starting note.   

If the qualified interval name passed to either method is itself invalid, for example, major 5,
then an InvalidIntervalException is raised.

Scales
------

##### *class* Scale(*qualified_name*)
A scale object is constructed with a string representing the qualified scale
name. The qualified scale name consists of a tonic followed by a scale quality. 
Valid tonics are letters A through G. Valid qualities are
major, harmonic minor, melodic minor, and natural minor. If an invalid tonic
passed, an InvalidTonicError is raised. If an invalid quality is passed, an
InvalidQualityError is raised. For example,

```
>>> c = Scale('C major')
>>> c_harm = Scale('C harmonic minor')
>>> c_badquality = Scale('C Foo')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/jmoorhead/projects/musictheorpy/musictheorpy/scales.py", line 36, in __init__
    super().__init__('SCALE', qualified_name)
  File "/home/jmoorhead/projects/musictheorpy/musictheorpy/notegroups.py", line 74, in __init__
    raise InvalidQualityError("Quality %s is not valid" % self.quality) from None
musictheorpy.notegroups.InvalidQualityError: Quality Foo is not valid
>>>
>>> c_badtonic = Scale('Z major')
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

As indicated in the trace back for `c_badtonic` above, it is possible to pass a valid note name, but still receive an InvalidTonicError. This occurs when the
key signature of the given scale name would include qualifiers beyond sharps and flats.
For example, G# Major would have F## in its key signature. Because key signatures like
this are generally not used in music theory, they are not valid.  

The key signature of a Scale object is accessible through its
key_signature property, which is a tuple of strings representing the
notes that make up the scale's key signature. For example,
```
>>> a_major = Scale('A major')
>>> a_major.key_signature
('F#', 'C#', 'G#')
>>> e_minor = Scale('E natural minor')
>>> 'F#' in e_minor.key_signature
True
```

In addition, you can access all the notes in the scale through the
object's notes attribute, which provides a tuple of strings representing
all the notes in the scale. Finally, Scale objects implement the 
`__getitem__` and `__contains__` magic methods. The `__getitem__` method
allows lookup of notes in a scale by degree name. Valid degree names are
tonic, supertonic, mediant, subdominant, dominant, submediant, and 
leading tone. For example,
```
>>> a_major = Scale('A major')
>>> a_major['tonic']
'A'
>>> a_major['submediant']
'F#'
```

Finally, users can test if a note is in a given scale using Python's
built-in `in` keyword, thanks to the `__contains__` method.
```
>>> a_major = Scale('A major')
>>> 'F#' in a_major
True
>>> 'B#' in a_major
False
```

Chords
------
##### *class* Chord(*qualified_name*)

Chord objects are constructed with a string representing the qualified
name of the chord. Like scales, the qualified name of a chord is made up
of a bass note name (letters A through G) followed by a quality. Valid
chord qualities are major, minor, diminished, augmented, and minor 7b5.
Chords containing upper extensions 7, 9, 11, and 13 are also possible. All upper
extensions can be dominant, major, or minor, e.g. dominant 7, major 9, minor 13.
In addition, extensions 9, 11, and 13 can be modified with a flat (b)
or sharp (#) for dominant chords, e.g. dominant #9, dominant b13.  

If an invalid bass note is passed, an InvalidBassError is raised. Similarly,
if an invalid chord quality is passed, an InvalidQualityError is raised. For 
example,
```
>>> c = Chord('C major')
>>> c_seventh = Chord('C dominant 7')
>>> z = Chord('Z major')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/jmoorhead/projects/musictheorpy/musictheorpy/chords.py", line 10, in __init__
    super().__init__('CHORD', qualified_name)
  File "/home/jmoorhead/projects/musictheorpy/musictheorpy/notegroups.py", line 68, in __init__
    self._validate_root(unpacked_name)
  File "/home/jmoorhead/projects/musictheorpy/musictheorpy/chords.py", line 25, in _validate_root
    raise InvalidBassError("Invalid bass note: %s" % unpacked_name['ROOT'])
musictheorpy.chords.InvalidBassError: Invalid bass note: Z
>>>
>>> c_badqual = Chord('C FOO')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/jmoorhead/projects/musictheorpy/musictheorpy/chords.py", line 10, in __init__
    super().__init__('CHORD', qualified_name)
  File "/home/jmoorhead/projects/musictheorpy/musictheorpy/notegroups.py", line 74, in __init__
    raise InvalidQualityError("Quality %s is not valid" % self.quality) from None
musictheorpy.notegroups.InvalidQualityError: Quality FOO is not valid
```

Users can access the notes in a Chord object via the object's notes attribute. This
attribute provides a tuple containing all the notes in the chord as strings. For example,
```
>>> c_dominant = Chord('C dominant 7')
>>> c_dominant.notes
('C', 'E', 'G', 'Bb')
```
In addition, Chord objects implement the `__getitem__` method so users can check if a note is
in the chord directly:
```
>>> c = Chord('C major')
>>> 'E' in c
True
>>> 'F' in c
False
```
Finally, Chord objects allow access to its constituent notes via the `__getitem__` method, which allows
lookup by degree name. Valid degree names are bass, third, fifth, seventh, ninth, eleventh, and thirteenth.
Note that not all degrees apply to all chords, and only thirteenth chords will
have all degrees. In general, chords only contain a subset of these degrees. If the caller tries to access a
degree that is not present in the given chord, `__getitem__` returns None. For example,
```
>>> c = Chord('C major')  # a triad, no extensions
>>> c['third']  # valid degree
'E'
>>> c['ninth'] is None  # C triad does not have a ninth
True
```

If an invalid degree is passed, an InvalidDegreeError is raised.
```
>>> c = Chord('C major')
>>> c['foo']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/jmoorhead/projects/musictheorpy/musictheorpy/chords.py", line 18, in __getitem__
    raise InvalidDegreeError("Invalid degree name: %s" % element) from None
musictheorpy.notegroups.InvalidDegreeError: Invalid degree name: foo
```