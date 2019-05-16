import numpy as np
from numpy_exercise import (
    create_array, select_first_col, select_values, invert_values
)


def test_create_array():
    assert np.array_equal(create_array(), np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def test_select_first_col():
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    assert np.array_equal(select_first_col(a), a[:, 0])


def test_select_values():
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    assert np.array_equal(select_values(a), a[a > 4])


def test_invert_values():
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    assert np.array_equal(invert_values(a), 1 / a)


def test_invert_values_array_with_zero():
    a = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])

    assert not invert_values(a)
