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


def test_blinker():
    """Blinker (period 2)."""
    pattern_1 = np.array([[0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 1, 1, 1, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0]], dtype=bool)
    pattern_2 = np.array([[0, 0, 0, 0, 0],
                          [0, 0, 1, 0, 0],
                          [0, 0, 1, 0, 0],
                          [0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0]], dtype=bool)
    np.testing.assert_array_equal(pattern_1, life.model(pattern_2))
    np.testing.assert_array_equal(pattern_2, life.model(pattern_1))


def test_toad():
    """Toad (period 2)."""
    pattern_1 = np.array([[0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0, 0],
                          [0, 1, 0, 0, 1, 0],
                          [0, 1, 0, 0, 1, 0],
                          [0, 0, 1, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0]], dtype=bool)
    pattern_2 = np.array([[0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 1, 1, 1, 0],
                          [0, 1, 1, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0]], dtype=bool)
    np.testing.assert_array_equal(pattern_1, life.model(pattern_2))
    np.testing.assert_array_equal(pattern_2, life.model(pattern_1))


def test_beacon():
    """Beacon (period 2)."""
    pattern_1 = np.array([[0, 0, 0, 0, 0, 0],
                          [0, 1, 1, 0, 0, 0],
                          [0, 1, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 0],
                          [0, 0, 0, 1, 1, 0],
                          [0, 0, 0, 0, 0, 0]], dtype=bool)
    pattern_2 = np.array([[0, 0, 0, 0, 0, 0],
                          [0, 1, 1, 0, 0, 0],
                          [0, 1, 1, 0, 0, 0],
                          [0, 0, 0, 1, 1, 0],
                          [0, 0, 0, 1, 1, 0],
                          [0, 0, 0, 0, 0, 0]], dtype=bool)
    np.testing.assert_array_equal(pattern_1, life.model(pattern_2))
    np.testing.assert_array_equal(pattern_2, life.model(pattern_1))
