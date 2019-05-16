import numpy as np


def create_array():
    return np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def select_first_col(q):
    return q[:, 0]


def select_values(x):
    return x[x > 4]


def invert_values(x):
    if (x == 0).any():
        return False
    return 1 / x
