def swap_numbers(x: str | int, y: str | int) -> tuple[int, int]:
    """
    Swap two integers using tuple unpacking (no introduction of new vars)

    :param x: 1st integer to swap
    :type x: str | int
    :param y: 2nd integer to swap
    :type y: str | int
    :raises ValueError: when valid ints aren't passed in
    :return: swapped numbers
    :rtype: tuple[int, int]

    """
    x, y = int(y), int(x)
    return x, y


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
