import unittest


def swap_numbers(x: str | int, y: str | int) -> tuple[int, int]:
    """
    Swap two integers using tuploe unpacking (no introduction of new vars)

    :param x: 1st integer to swap
    :type x: str | int
    :param y: 2nd integer to swap
    :type y: str | int
    :return: swapped numbers
    :rtype: tuple[int, int]

    """
    x, y = int(y), int(x)
    return x, y


class TestSwap(unittest.TestCase):
    def test_swaps_positive(self):
        swapped = swap_numbers(5, 3)
        self.assertEqual(swapped, (3, 5))

    def test_swaps_negative(self):
        swapped = swap_numbers(-82, -17)
        self.assertEqual(swapped, (-17, -82))

    def test_swaps_mixed(self):
        swapped = swap_numbers(9, -147)
        self.assertEqual(swapped, (-147, 9))

    def test_swaps_same(self):
        swapped = swap_numbers(0, 0)
        self.assertEqual(swapped, (0, 0))

    def test_throws_error_for_invalid_input(self):
        with self.assertRaises(ValueError):
            swap_numbers('a', 'b')


if __name__ == "__main__":
    print("Swap two numbers! (prepare to be amazed 😎)")
    print("Type 'exit' to stop swapping\n")

    while True:
        x: str | int = input("Enter first number: ")
        if x.lower() == "exit":
            break
        y: str | int = input("Enter second number: ")
        if y.lower() == "exit":
            break
        print(f"\noriginal - x: {x}, y: {y}")

        x, y = swap_numbers(x, y)
        print(f"swapped - x: {x}, y: {y}")
        print("💃 🕺\n")

    choice: str = input("\nrun tests? [Y/n]: ")
    if not choice or choice.casefold() == 'y':
        unittest.main()
