
from mingus.containers.Bar import Bar
from mingus.containers.Note import Note
from mingus.containers.NoteContainer import NoteContainer

import mingus.core.chords as chords

from random import random

def bassline(chord, beat_probas):

    bass_note = chords.from_shorthand(chord)[0]
    octave = 2

    note = Note(bass_note, octave)

    b = Bar()

    for beat_p in beat_probas:
        p = random()
        if p < beat_p:
            b.place_notes(note, 8)
        else:
            b.place_rest(8)

    return b
