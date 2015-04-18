import midi

def get_pattern(file):
    return midi.read_midfile(file)

print get_pattern("midi/dance/darude/Sandstorm.mid")
