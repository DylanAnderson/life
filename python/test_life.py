import numpy as np
import life


class TestCell(object):

    def combos(self, p):
        return (life.cell(p),
                life.cell(np.flipud(p)),
                life.cell(np.fliplr(p)),
                life.cell(np.flipud(np.fliplr(p))))

    def test_corner(self):
        # No rule - dead
        p = np.array([[1, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]])
        assert not any(self.combos(p))

    def test_stack(self):
        # No rule - dead
        p = np.array([[1, 1, 0],
                      [0, 0, 0],
                      [0, 0, 0]])
        assert not any(self.combos(p))

    def test_row(self):
        # Rule 4
        p = np.array([[1, 1, 1],
                      [0, 0, 0],
                      [0, 0, 0]])
        assert all(self.combos(p))

    def test_short_L(self):
        # No rule - dead
        p = np.array([[1, 1, 1],
                      [1, 0, 0],
                      [0, 0, 0]])
        assert not any(self.combos(p))

    def test_long_L(self):
        # No rule - dead
        p = np.array([[1, 1, 1],
                      [1, 0, 0],
                      [1, 0, 0]])
        assert not any(self.combos(p))

    def test_G(self):
        # No rule - dead
        p = np.array([[1, 1, 1],
                      [1, 0, 0],
                      [1, 1, 0]])
        assert not any(self.combos(p))

    def test_U(self):
        # No rule - dead
        p = np.array([[1, 1, 1],
                      [1, 0, 0],
                      [1, 1, 1]])
        assert not any(self.combos(p))

    def test_donut(self):
        # No rule - dead
        p = np.array([[1, 1, 1],
                      [1, 0, 1],
                      [1, 1, 1]])
        assert not any(self.combos(p))

    def test_lone_survivor(self):
        # Rule 1: dead
        p = np.array([[0, 0, 0],
                      [0, 1, 0],
                      [0, 0, 0]])
        assert not any(self.combos(p))

    def test_duo(self):
        # Rule 1: dead
        p = np.array([[1, 0, 0],
                      [0, 1, 0],
                      [0, 0, 0]])
        assert not any(self.combos(p))

    def test_triangle(self):
        # Rule 2: alive
        p = np.array([[1, 0, 1],
                      [0, 1, 0],
                      [0, 0, 0]])
        assert all(self.combos(p))

    def test_squads(self):
        # Rule 2: alive
        p = np.array([[1, 0, 1],
                      [0, 1, 0],
                      [0, 1, 0]])
        assert all(self.combos(p))

    def test_fives_company(self):
        # Rule 3: dead
        p = np.array([[1, 0, 1],
                      [0, 1, 0],
                      [1, 1, 0]])
        assert not any(self.combos(p))


class TestStillLife(object):
    def test_block(self):
        """Block still life."""
        pattern = np.array([[0, 0, 0, 0],
                            [0, 1, 1, 0],
                            [0, 1, 1, 0],
                            [0, 0, 0, 0]], dtype=bool)
        new_pattern = life.model(pattern)
        np.testing.assert_array_equal(pattern, new_pattern)

    def test_beehive(self):
        """Beehive still life."""
        pattern = np.array([[0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 1, 0, 0],
                            [0, 1, 0, 0, 1, 0],
                            [0, 0, 1, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0]], dtype=bool)
        new_pattern = life.model(pattern)
        np.testing.assert_array_equal(pattern, new_pattern)

    def test_loaf(self):
        """Loaf still life."""
        pattern = np.array([[0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 1, 0, 0],
                            [0, 1, 0, 0, 1, 0],
                            [0, 0, 1, 0, 1, 0],
                            [0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0]], dtype=bool)
        new_pattern = life.model(pattern)
        np.testing.assert_array_equal(pattern, new_pattern)

    def test_boat(self):
        """Boat still life."""
        pattern = np.array([[0, 0, 0, 0, 0],
                            [0, 1, 1, 0, 0],
                            [0, 1, 0, 1, 0],
                            [0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0]], dtype=bool)
        new_pattern = life.model(pattern)
        np.testing.assert_array_equal(pattern, new_pattern)


class TestOscillators(object):

    def test_blinker(self):
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

    def test_toad(self):
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

    def test_beacon(self):
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
