import numpy as np


def invert_values(x):
    if (x == 0).any():
        return False
    return 1 / x
