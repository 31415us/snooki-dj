snooki-dj
=========

# About

Our entry for the 2015 Facebook hackathon at EPFL

snooki-dj is a small proof of concept implementation for procedural music
generation

# How it works

At the moment snooki creates 3 simultaneous tracks, Drum, Bass and Harmony. For the harmony
track we create a markov chain from the chord changes in several midi files
we got from mididb.com. Bassline and Drum tracks are generated automatically from
a discrete probability distribution for each eigth note in a 4/4 measure.
For basslines these probabilities signify how probable it is that the root node,
the octave above or any random note from the chord is played (probability of rests are implicit). 
Similarly for the drumtrack we have probabilities for bass, snare, hihat and rest
at each eigth note.

# Libraries

* python 2.7
* mingus (0.4) with this patch: https://github.com/bgr/mingus/issues/24

the visualization code for the demo uses the following additional libraries

* tkinter
* matplotlib
* networkx

# Usage

>>> from Snooki import Snooki
>>> s = Snooki()
...
>>> for chord in s.play():
        print chord
