from mingus.midi.MidiFileIn import MIDI_to_Composition
from mingus.containers.NoteContainer import NoteContainer
from mingus.midi import fluidsynth


def get_composition(file):
    try:
        return MIDI_to_Composition(file)
    except Exception as e:
        print (e)
        print ("Could not load midi file: " + file)


def get_longest_progression(f):
    (comp, bpm) = get_composition(f)
    progression = []
    progressions = []
    curr_chord = None
    chord_length = 1

    for track in comp:
        for bar in track:
            for cont in bar:
                notes = cont[2]

                if len(notes) > 2:
                    if curr_chord is not None:
                        progression.append((curr_chord, chord_length))
                        curr_chord = NoteContainer(notes).determine()

                        if len(curr_chord) != 0:
                            curr_chord = curr_chord[0]
                        else:
                            curr_chord = None
                            break

                        chord_length = 1
                    else:
                        curr_chord = NoteContainer(notes).determine()

                        if len(curr_chord) != 0:
                            curr_chord = curr_chord[0]
                        else:
                            curr_chord = None
                            break
                else:
                    chord_length += 1

        progressions.append(progression)

    max = 0;
    max_progression = None
    for p in progressions:
        if len(p) > max:
            max_progression = p

    return p


def get_all_progressions():
    progressions = []

    with open("../midi/dance/paths.txt") as f:
        progressions.append(get_longest_progression("../midi/" + f.readline()))

    return progressions


#file = "../midi/dance/darude/Sandstorm.mid"
#(comp, bpm) = get_composition(file)
#
#fluidsynth.init("../soundfonts/soundfont.sf2", "alsa")
#
#fluidsynth.play_Composition(comp, None, bpm)

#f = "./prog.mid"
#f = "../midi/dance/darude/Sandstorm.mid"

print get_all_progressions()
