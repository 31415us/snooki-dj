
from collections import defaultdict

class MarkovChain(object):

    START = "start"

    def __init__(self, sequences):
        # laplace smoothing similar to naive bayes
        self.bigram_count = defaultdict(lambda: 1)

        for seq in sequences:
            self._seq_to_bigrams(seq)

    def _seq_to_bigrams(self, seq):

        prev = self.START

        for (chord, repetitions) in seq:
            self.bigram_count[(prev, chord)] += 1
            prev = chord
