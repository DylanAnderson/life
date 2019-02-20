import time
import numpy as np
import curses


def model(pattern):
    """Rules of the game:
    1. Any live cell with fewer than 2 live neighbors dies, as if by underpopulation.
    2. Any live cell with 2 or 3 live neighbors lives on to the next generation
    3. Any live cell with more than 3 live neighbors dies, as if by overpopulation
    4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
    """

    # TODO we don't have a model, just sample random patterns
    neighborhood = (3, 3)
    # View neighborhoods using this crazy example:
    # https://stackoverflow.com/questions/43086557/convolve2d-just-by-using-numpy
    s = neighborhood + tuple(np.subtract(pattern.shape, neighborhood) + 1)
    neighborhoods = np.lib.stride_tricks.as_strided(pattern, shape=s, strides=pattern.strides * 2)
    new_pattern = np.zeros_like(pattern)
    for i in range(s[2]):
        for j in range(s[3]):
            cell = neighborhoods[..., i, j]
            n_alive = cell.sum()
            if cell[1, 1]:  # cell is currently alive
                if n_alive < 3:  # Rule 1
                    new_pattern[i + 1, j + 1] = False
                elif n_alive < 4:  # Rule 2
                    new_pattern[i + 1, j + 1] = True
                else:  # Rule 3
                    new_pattern[i + 1, j + 1] = False
            elif n_alive == 3:  # Rule 4
                new_pattern[i + 1, j + 1] = True
            else:
                new_pattern[i + 1, j + 1] = False
    return new_pattern


def view(stdscr, pattern):
    for x in range(pattern.shape[1]):
        for y in range(pattern.shape[0]):
            if pattern[x, y]:
                stdscr.addstr(y, x, "+")
            else:
                stdscr.addstr(y, x, " ")


def app(stdscr, pattern, frame_delay=0.1):
    # TODO change from window to pad, in case the window is too small to render the field
    # waiting for user input is non-blocking
    stdscr.nodelay(True)
    stdscr.clear()

    while True:
        # Check if we should quit
        c = stdscr.getch()
        if c == ord('q'):
            break

        # Render the current pattern
        view(stdscr, pattern)

        # Step generation
        pattern = model(pattern)
        stdscr.refresh()

        # Arbitrary framerate throttling
        time.sleep(frame_delay)


if __name__ == "__main__":
    pattern = np.random.choice([False, True], size=(25, 25))
    # model(pattern)
    curses.wrapper(app, pattern, 0.1)
