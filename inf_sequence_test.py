import unittest
from inf_sequence import kmp_get_pos
from random import randrange


def bruteforce_get_pos(a):
    """
    Generate a sequence of positive integers,
    and use brute-force algorithm
    to find first substring position in this sequence.

    Args:
        a (str): target substring A.
    Returns:
        seq.index(a)+1 (int): first ocurrence of substring A
        in sequence S, starting from 1.
    """
    found = False
    n = 1  # sequence start
    seq = ""

    while not found:
        seq += str(n)
        if a in seq:
            found = True
            return seq.index(a) + 1
        n += 1


def gen_substring(n):
    # Returns string of n random digits in range 0-9
    substring = ""

    for i in range(n):
        substring += str(randrange(10))

    return substring


class PosInSeqTests(unittest.TestCase):
    """
    Unit-tests to cover provided example cases data
    and check improved algorithm correctness.
    """
    def test6789_from_example(self):
        s = "6789"
        self.assertEqual(kmp_get_pos(s), 6)

    def test111_from_example(self):
        s = "111"
        self.assertEqual(kmp_get_pos(s), 12)

    def test_kmp(self):
        for i in range(100):
            # Generate random substring
            n = randrange(1, 5)
            substring = gen_substring(n)

            # Compare bruteforce vs KMP solution
            bruteforce = bruteforce_get_pos(substring)
            kmp = kmp_get_pos(substring)
            self.assertEqual(bruteforce, kmp)


if __name__ == '__main__':
    unittest.main()
