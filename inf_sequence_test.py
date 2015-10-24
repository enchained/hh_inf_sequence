import unittest
from inf_sequence import get_pos


class PosInSeqTests(unittest.TestCase):
    """
    unit-tests to cover provided example cases data
    """
    def test6789_from_example(self):
        s = "6789"
        self.assertEqual(get_pos(s), 6)

    def test111_from_example(self):
        s = "111"
        self.assertEqual(get_pos(s), 12)

if __name__ == '__main__':
    unittest.main()
