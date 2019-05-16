import numpy as np
from numpy_easy import gimme_ones, gimme_numbers


def test_3d_gimme_ones():
    assert np.array_equal(gimme_ones(3), np.ones(3))


def test_1d_gimme_ones():
    assert np.array_equal(gimme_ones(1), np.ones(1))


def test_gimme_numbers():
    assert np.array_equal(gimme_numbers(3, 5.67), np.ones(3) * 5.67)
