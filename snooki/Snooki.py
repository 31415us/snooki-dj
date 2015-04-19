
from chord_extractor import get_all_progressions

from MarkovChain import MarkovChain

from voicing import voice

from bassman import bassline

from mingus.containers.Bar import Bar
from mingus.containers.NoteContainer import NoteContainer
from mingus.midi import fluidsynth

class Snooki(object):

    def __init__(self):
        fluidsynth.init('../soundfonts/soundfont.sf2', 'alsa')
        self.m_chain = MarkovChain(get_all_progressions())
        self.sim = self.m_chain.infinite_progression()

        down1 = (0.7, 0.05, 0.2)
        down2 = (0.2, 0.05, 0.7)
        off = (0.0, 0.4, 0.1)

        self.bassproba = [down1, off, down2, off, down1, off, down2, off]

    def _next_bar(self):
        prev = None
        while True:
            chord_bar = Bar()

            nxt_chord = next(self.sim)

            nxt_voiced = voice(prev, nxt_chord)

            prev = nxt_voiced

            chord_bar + NoteContainer(nxt_voiced)

            chord_bar[0][1] = 1

            yield (chord_bar, bassline(nxt_chord, self.bassproba))


    def play(self):
        fluidsynth.set_instrument(1, 73) # chords
        fluidsynth.set_instrument(2, 32) # bass
        fluidsynth.main_volume(1, 50)
        fluidsynth.main_volume(2, 100)
        for bars in self._next_bar():
            fluidsynth.play_Bars(bars, [1, 2], 110)
