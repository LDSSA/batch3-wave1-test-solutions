import numpy as np


def euclidean_distance(x, y):
    if x is None:
        raise ValueError("First point must be defined.")

    if y is None:
        y = (0) * len(x)

    if len(x) != len(y):
        msg = "Cannot compute distance between points with different number of coordinates."
        raise ValueError(msg)

    x = np.array(x)
    y = np.array(y)

    return np.sqrt(np.sum(np.square(x - y)))
