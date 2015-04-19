
from mingus.containers.Note import Note
from mingus.containers.Bar import Bar

from random import random

BASS = Note('C', 2)
SNARE = Note('E', 2)
HIHAT = Note('C#', 2)

def drum_beat(beat_probas):
    b = Bar()

    for (bass, snare, hhat) in beat_probas:
        p = random()
        if p < bass:
            b.place_notes(BASS, 8)
        elif p < bass + snare:
            b.place_notes(SNARE, 8)
        elif p < bass + snare + hhat:
            b.place_notes(HIHAT, 8)
        else:
            b.place_rest(8)

    return b

