
import unittest

from snooki.MarkovChain import MarkovChain

class MarkovChainTest(unittest.TestCase):

    def test_bigrams(self):

        test_seq0 = [('a', 0), ('b', 0), ('c', 0)]
        test_seq1 = [('b', 0), ('c', 0)]

        chain = MarkovChain([test_seq0, test_seq1])

        self.assertTrue(chain.bigram_count[(MarkovChain.START, 'a')] == 2)
        self.assertTrue(chain.bigram_count[(MarkovChain.START, 'a')] == 2)
        self.assertTrue(chain.bigram_count[('a', 'b')] == 2)
        self.assertTrue(chain.bigram_count[('b', 'c')] == 3)
