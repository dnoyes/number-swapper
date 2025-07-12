import unittest
from swap import swap_numbers


class TestSwap(unittest.TestCase):
    def test_swaps_successfully(self):
        cases = [
            [(5, 3), (3, 5)],
            [(-82, -17), (-17, -82)],
            [(9, -147), (-147, 9)],
            [(-0, 0), (0, 0)],
            [(3, 3), (3, 3)],
        ]
        for case in cases:
            [original, expected] = case
            swapped = swap_numbers(*original)
            self.assertEqual(expected, swapped)

    def test_throws_error_for_invalid_input(self):
        with self.assertRaises(ValueError):
            swap_numbers('a', 'b')
