
from chord_extractor import get_all_progressions

from MarkovChain import MarkovChain

from voicing import voice

from mingus.containers.Bar import Bar
from mingus.containers.NoteContainer import NoteContainer
from mingus.midi import fluidsynth

class Snooki(object):

    def __init__(self):
        fluidsynth.init('../soundfonts/soundfont.sf2', 'alsa')
        self.m_chain = MarkovChain(get_all_progressions())
        self.sim = self.m_chain.infinite_progression()

    def _next_bar(self):
        prev = None
        while True:
            b = Bar()

            nxt_chord = next(self.sim)

            nxt_voiced = voice(prev, nxt_chord)

            prev = nxt_voiced

            b + NoteContainer(nxt_voiced)

            b[0][1] = 1

            yield b


    def play(self):
        fluidsynth.set_instrument(1, 70)
        for b in self._next_bar():
            fluidsynth.play_Bar(b, 1, 110)
