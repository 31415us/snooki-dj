
import mingus.core.chords as chords
import mingus.core.notes as notes

def voice(old_voiced, nxt_chord):

    if old_voiced is None:
        return chords.from_shorthand(nxt_chord)

    old = [notes.note_to_int(n) for n in old_voiced]
    new = {notes.note_to_int(n) for n in chords.from_shorthand(nxt_chord)}

    res = []
    for note in old:
        if new:
            closest = min(new, key=lambda n: abs(note - n))
            res.append(closest)
            new.remove(closest)
        else:
            if len(old) == 4:
                res.append(res[0])

    for n in new:
        best_index = 0
        min_dist = 12
        for i in range(0, len(old)):
            dist = abs(old[i] - n)
            if dist < min_dist:
                min_dist = dist
                best_index = i

        res.insert(i, n)


    return [notes.int_to_note(n) for n in res]

