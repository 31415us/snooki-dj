from mingus.midi.MidiFileIn import MIDI_to_Composition

from mingus.containers.NoteContainer import NoteContainer

from mingus.midi import fluidsynth


def get_composition(file):
    try:
        return MIDI_to_Composition(file)
    except Exception as e:
        print (e)
        print ("Could not load midi file: " + file)


#file = "../midi/dance/darude/Sandstorm.mid"
#(comp, bpm) = get_composition(file)
#
#fluidsynth.init("../soundfonts/soundfont.sf2", "alsa")
#
#fluidsynth.play_Composition(comp, None, bpm)

f = "./prog.mid"

(comp, bpm) = get_composition(f)

for track in comp:
    for bar in track:
        for cont in bar:
            notes = cont[2]
            if len(notes) > 2:
                print(NoteContainer(notes).determine()[0])
