from mingus.midi.MidiFileIn import MIDI_to_Composition


def get_composition(file):
    try:
        MIDI_to_Composition(file)
    except Exception as e:
        print (e)
        print ("Could not load midi file: " + file)


file = "./midi/dance/darude/Sandstorm.mid"
get_composition(file)
