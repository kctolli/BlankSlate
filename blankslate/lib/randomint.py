import random

def randomint(stop = 1):
    """
    Generates a random integer between 0 and stop.

    Parameters:
        stop (int): The upper bound of the random integer.

    Returns:
        int: A random integer between 0 and stop.
    """
    return random.randint(1, stop)
