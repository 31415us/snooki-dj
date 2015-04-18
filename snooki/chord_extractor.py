from mingus.midi.MidiFileIn import MIDI_to_Composition

from mingus.midi import fluidsynth


def get_composition(file):
    try:
        return MIDI_to_Composition(file)
    except Exception as e:
        print (e)
        print ("Could not load midi file: " + file)


file = "../midi/dance/darude/Sandstorm.mid"
(comp, bpm) = get_composition(file)

fluidsynth.init("../soundfonts/soundfont.sf2", "alsa")

fluidsynth.play_Composition(comp, None, bpm)
