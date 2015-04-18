from mingus.midi.MidiFileIn import MIDI_to_Composition
from mingus.containers.NoteContainer import NoteContainer
from mingus.midi import fluidsynth

import os


def get_composition(file):
    try:
        return MIDI_to_Composition(file)
    except Exception as e:
        print (e)
        print ("Could not load midi file: " + file)


def get_longest_progression(f):
    try:
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

                            if len(curr_chord) != 0 and curr_chord[0][0].isupper():
                                curr_chord = curr_chord[0]
                            else:
                                curr_chord = None
                                break

                            chord_length = 1
                        else:
                            curr_chord = NoteContainer(notes).determine()

                            if len(curr_chord) != 0 and curr_chord[0][0].isupper():
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

        prev_progression = max_progression[0]
        count = max_progression[1]
        progression = []

        for p in max_progression[1:]:
            if prev_progression[0] == p[0]:
                count += p[1]
            else:
                progression.append((prev_progress[0], count))
                prev_progression = p
                count = p[1]

        return progression
    
    except:
        return []


def get_all_progressions():
    with open("../midi/dance/paths.txt") as f:
        for line in f:
            yield get_longest_progression(os.path.normpath("../midi/" + line.strip()))


