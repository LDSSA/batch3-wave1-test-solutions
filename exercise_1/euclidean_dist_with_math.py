import math


def euclidean_distance(x, y):
    if x is None:
        raise ValueError("First point must be defined.")

    if y is None:
        y = (0,) * len(x)

    if len(x) != len(y):
        msg = "Cannot compute distance between points with different number of coordinates."
        raise ValueError(msg)

    squared_diffs = []
    for i in range(len(x)):
        squared_diffs.append((x[i] - y[i])**2)

    return math.sqrt(sum(squared_diffs))
