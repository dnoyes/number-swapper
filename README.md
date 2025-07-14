# Number Swapper

This script swaps two integers _without_ introducing new variables, using tuple unpacking. This is very similar to destructuring in JavaScript.

## Run script

Using >= python 3.3:

```
python swap.py
```

You'll be prompted to enter two numbers:

```
Swap two numbers! (prepare to be amazed 😎)
Type 'exit' to stop swapping

Enter first number: 7
Enter second number: 3
```

It will then print the original input and then the swapped input

```
original - x: 7, y: 3
swapped - x: 3, y: 7
💃 🕺
```

To stop swapping, type `exit` as one of the numbers.

## Run Tests

First, set up a virtual env and install dependencies (`pytest`)

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then run the tests

```
python -m pytest tests/*.py

=================== test session starts ====================
collected 2 items

tests/test_swapnums.py ..                             [100%]
==================== 2 passed in 0.00s =====================
```

Deactivate virtual env when done

```
deactivate
```

## Conclusion

And that's it. I hope you enjoyed this short exercise. If you want to see any other exercises, let me know :)
