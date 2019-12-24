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
musictheorpy.notes exposes the following public classes
- `Note`

In addition, the module provides the following exception 
- `NoteNameError`.

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
are 0 - 15. Note that interval number 9 - 15 only accept MINOR, MAJOR, and
PERFECT qualifiers. 12 is the lone exception to this rule and also allows DIMINISHED.  
  
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

`descend_interval` is functionally identical, except that it descends the given
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
technically result in a C###, which is not considered valid. In this case, an `InvalidIntervalError`
is raised to inform the client that the given interval is not valid for the starting note.   

It is important to note that an `InvalidIntervalError` does *not* indicate that the given 
interval itself is bad. In this case, a `KeyError` would be raised and should be caught by the
client to alert the user that they have given a bad interval name.

Scales
------
Properties: tonic, notes, key signature, quality
Behaviors: get relative/parallel, get scale degree, get note number, validate tonic

Chords
------
Properties: root (bass), notes, quality
Behaviors: get relative/parallel, get element, get note number, possibly validate tonic
