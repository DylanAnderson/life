import numpy as np
import life


def test_block():
    """Block still life."""
    pattern = np.array([[0, 0, 0, 0],
                        [0, 1, 1, 0],
                        [0, 1, 1, 0],
                        [0, 0, 0, 0]], dtype=bool)
    new_pattern = life.model(pattern)
    np.testing.assert_array_equal(pattern, new_pattern)


def test_beehive():
    """Beehive still life."""
    pattern = np.array([[0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 0, 0],
                        [0, 1, 0, 0, 1, 0],
                        [0, 0, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0]], dtype=bool)
    new_pattern = life.model(pattern)
    np.testing.assert_array_equal(pattern, new_pattern)


def test_loaf():
    """Loaf still life."""
    pattern = np.array([[0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 0, 0],
                        [0, 1, 0, 0, 1, 0],
                        [0, 0, 1, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0]], dtype=bool)
    new_pattern = life.model(pattern)
    np.testing.assert_array_equal(pattern, new_pattern)


def test_boat():
    """Boat still life."""
    pattern = np.array([[0, 0, 0, 0, 0],
                        [0, 1, 1, 0, 0],
                        [0, 1, 0, 1, 0],
                        [0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0]], dtype=bool)
    new_pattern = life.model(pattern)
    np.testing.assert_array_equal(pattern, new_pattern)
