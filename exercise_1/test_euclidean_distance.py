import pytest
from math import isclose
from euclidean_dist_with_numpy import euclidean_distance


def test_valid_int_values():
    a = (8, -3, 4)
    b = (7, 14, 0)

    assert isclose(euclidean_distance(a, b), 17.4928, rel_tol=1e-2)


def test_valid_float_values():
    a = (1.2, 3, 4.1)
    b = (5, 7.8, -9.0)

    assert isclose(euclidean_distance(a, b), 14.4599, rel_tol=1e-2)


def test_point_a_is_none():
    a = None
    b = (1, 2)

    with pytest.raises(ValueError) as e:
        euclidean_distance(a, b)

    assert str(e.value) == 'First point must be defined.'


def test_point_b_is_none():
    a = (1, 2, 3)
    b = None

    assert isclose(euclidean_distance(a, b), 3.7416, rel_tol=1e-2)


def test_mismatching_dimensions():
    a = (8, 9)
    b = (1.2, 3, -7, 8)

    with pytest.raises(ValueError) as e:
        euclidean_distance(a, b)

    msg = 'Cannot compute distance between points with different number of coordinates.'
    assert str(e.value) == msg


def test_overlapping_points():
    a = (4, 4, 4)
    b = (4, 4, 4)

    assert euclidean_distance(a, b) == 0
