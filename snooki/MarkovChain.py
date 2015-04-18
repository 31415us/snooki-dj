
from collections import defaultdict
from random import random

class MarkovChain(object):

    START = "start"

    def __init__(self, sequences):
        self.bigram_count = defaultdict(int)
        self.neighbours = defaultdict(set)

        for seq in sequences:
            self._seq_to_bigrams(seq)

    def _seq_to_bigrams(self, seq):

        prev = self.START

        for (chord, repetitions) in seq:
            self.bigram_count[(prev, chord)] += 1
            self.neighbours[prev].add(chord)
            prev = chord

    def _next_state(self, state):

        weights = 0

        probas = {}

        for n in self.neighbours[state]:
            b_count = self.bigram_count[(state, n)]
            weights += b_count
            probas[n] = float(b_count)

        for n in probas:
            probas[n] /= weights

        r = random()

        acc = 0

        for n in probas:
            acc += probas[n]
            if r < acc:
                return n

        return state

    def create_progression(self, length):
        current_state = self.START
        
        for i in range(0, length):
            current_state = self._next_state(current_state)
            yield current_state

    def infinite_progression(self):
        current_state = self.START
        while True:
            current_state = self._next_state(current_state)
            yield current_state
