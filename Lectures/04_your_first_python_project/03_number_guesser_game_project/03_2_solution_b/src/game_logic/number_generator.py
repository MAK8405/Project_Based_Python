import random

# we can write type annotation too,
# def generate_random_number(start: int, end: int)  -> int:
# start is an integer, end is an integer, and it return an integer


def generate_random_number(start, end):
    """Generate a random number between start and end (inclusive)."""
    return random.randint(start, end)
