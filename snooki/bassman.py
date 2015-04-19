
from mingus.containers.Bar import Bar
from mingus.containers.Note import Note
from mingus.containers.NoteContainer import NoteContainer

import mingus.core.chords as chords

import random

def bassline(chord, beat_probas):

    chord_tones = chords.from_shorthand(chord)
    octave = 2

    b = Bar()

    for (bass, els, octa) in beat_probas:
        p = random.random()
        if p < bass:
            b.place_notes(Note(chord_tones[0], octave), 8)
        elif p < bass + els:
            b.place_notes(Note(random.choice(chord_tones[1:]), octave), 8)
        elif p < bass + els + octa:
            b.place_notes(Note(chord_tones[0], octave + 1), 8)
        else:
            b.place_rest(8)

    return b
