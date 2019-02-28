import time
import numpy as np
import curses


def cell(neighborhood):
    n_alive = neighborhood.sum()
    if n_alive == 3:
        return True
    elif neighborhood[1, 1] and n_alive == 4:
        return True
    return False


def model(pattern):
    """Rules of the game:
    1. Any live cell with fewer than 2 live neighbors dies, as if by underpopulation.
    2. Any live cell with 2 or 3 live neighbors lives on to the next generation
    3. Any live cell with more than 3 live neighbors dies, as if by overpopulation
    4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
    """

    neighborhood = (3, 3)
    # View neighborhoods using this crazy example:
    # https://stackoverflow.com/questions/43086557/convolve2d-just-by-using-numpy
    s = neighborhood + tuple(np.subtract(pattern.shape, neighborhood) + 1)
    neighborhoods = np.lib.stride_tricks.as_strided(pattern, shape=s, strides=pattern.strides * 2)
    new_pattern = np.zeros_like(pattern)
    for i in range(s[2]):
        for j in range(s[3]):
            new_pattern[i + 1, j + 1] = cell(neighborhoods[..., i, j])
    return new_pattern


def view(stdscr, pattern, it, n_alive, alive="o", dead=" "):
    width, height = pattern.shape
    stdscr.border()
    # Render the current pattern
    for x in range(pattern.shape[0]):
        for y in range(pattern.shape[1]):
            stdscr.addstr(y + 1, x + 1, alive if pattern[x, y] else dead)

    # Display some summary statistics
    stdscr.addstr(height + 1, 1, "Epoch: {}".format(it))
    stdscr.addstr(height + 2, 1, "Alive: {}".format(n_alive))
    stdscr.clrtoeol()

    # Render current frame
    stdscr.refresh()


def app(stdscr, pattern, frame_delay=0.1):
    # waiting for user input is non-blocking
    stdscr.nodelay(True)
    stdscr.clear()
    # Resize window to the size of the pattern (+ border)
    curses.resizeterm(pattern.shape[1] + 4, pattern.shape[0] + 2)

    i = 0
    while True:
        # Check if we should quit
        c = stdscr.getch()
        if c == ord('q'):
            break

        # Render the current pattern
        view(stdscr, pattern, it=i, n_alive=pattern.sum())

        # Step generation
        pattern = model(pattern)

        # Arbitrary framerate throttling
        time.sleep(frame_delay)
        i += 1


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Conway's game of life")
    parser.add_argument('--width', metavar='width', type=int, default=25,
                        help='width of the simulation')
    parser.add_argument('--height', metavar='height', type=int, default=0,
                        help='height of the simulation')
    parser.add_argument('--frame-delay', type=float, default=0.1,
                        help='delay (seconds) between frames of the simulation')
    args = parser.parse_args()
    # Default to a square
    height = args.width if args.height == 0 else args.height

    # Create a random initial pattern
    pattern = np.random.choice([False, True], size=(args.width, height))
    # Run the game
    curses.wrapper(app, pattern, args.frame_delay)
