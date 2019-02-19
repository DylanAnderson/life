# Rules of the game:
# 1. Any live cell with fewer than 2 live neighbors dies, as if by underpopulation.
# 2. Any live cell with 2 or 3 live neighbors lives on to the next generation
# 3. Any live cell with more than 3 live neighbors dies, as if by overpopulation
# 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
import time
import numpy as np
import curses


def model(pattern):
    # TODO we don't have a model, just sample random patterns
    return np.random.choice([False, True], size=pattern.shape)


def view(stdscr, pattern):
    for x in range(pattern.shape[1]):
        for y in range(pattern.shape[0]):
            if pattern[x, y]:
                stdscr.addstr(y, x, "+")
            else:
                stdscr.addstr(y, x, " ")


def app(stdscr, pattern, frame_delay=0.1):
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
    pattern = model(np.zeros((25, 25)))
    curses.wrapper(app, pattern, 0.1)
