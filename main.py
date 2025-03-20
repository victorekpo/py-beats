# This is a sample Python script.
from src.beat1 import play_beat
from src.beat2 import BeatGrid, play_beat_grid


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # Call the function to play the beat
    play_beat()

    # Create the grid and add instruments
    beat_grid = BeatGrid(tempo=120)

    # Define a pattern for each instrument (beats 1, 2, 3, 4)
    beat_grid.add_instrument("kick", [1, 3])  # Kick on beats 1 and 3
    beat_grid.add_instrument("snare", [2, 4])  # Snare on beats 2 and 4
    beat_grid.add_instrument("hihat", [1, 2, 3, 4])  # Hi-hat on every beat
    beat_grid.add_instrument("piano", [1, 2, 3])  # Play piano on beats 1, 2, and 3

    # Example: Playing the beat grid
   # play_beat_grid(beat_grid)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
