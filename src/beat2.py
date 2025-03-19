from pydub import AudioSegment
from pydub.playback import play
import time

# Load your samples (replace with your actual sound files)
kick = AudioSegment.from_file("./src/07_Kick_03_SP.wav")
snare = AudioSegment.from_file("./src/07_Snare_01_SP.wav")
hihat = AudioSegment.from_file("./src/07_Hats_14_SP.wav")
piano = AudioSegment.from_file("./src/Bass (6).wav")  # A piano note


# Helper function to calculate beat timing in milliseconds
def get_beat_time(tempo, beat_number, beats_per_bar=4):
    """
    Calculate the time for each beat based on the tempo.
    :param tempo: Beats per minute (BPM)
    :param beat_number: The specific beat (e.g., 1, 2, 3, 4)
    :param beats_per_bar: Length of the bar (usually 4 for 4/4 time signature)
    :return: Time in milliseconds
    """
    seconds_per_beat = 60.0 / tempo
    return (beat_number - 1) * seconds_per_beat * 1000  # Return time in milliseconds


# Create a dynamic grid for patterns
class BeatGrid:
    def __init__(self, tempo=120, beats_per_bar=4, instruments=None):
        self.tempo = tempo
        self.beats_per_bar = beats_per_bar
        self.grid = []  # A list of instruments' beat patterns
        self.instruments = instruments if instruments else []

    def add_instrument(self, instrument_name, pattern):
        """
        Add a new instrument with its beat pattern to the grid.
        :param instrument_name: The name of the instrument (e.g., "kick", "snare")
        :param pattern: A list representing the beats the instrument plays on (e.g., [1, 3] for kick)
        """
        self.instruments.append(instrument_name)
        self.grid.append(pattern)

    def calculate_beat_times(self):
        """
        Calculate the time for each event in the grid, considering the tempo.
        :return: A list of timed events for each instrument
        """
        timed_grid = []
        for i, instrument in enumerate(self.instruments):
            pattern = self.grid[i]
            timed_pattern = [(instrument, get_beat_time(self.tempo, beat)) for beat in pattern]
            timed_grid.append(timed_pattern)
        return timed_grid


# Function to play the grid with calculated timings
def play_beat_grid(beat_grid):
    timed_grid = beat_grid.calculate_beat_times()

    current_time = 0
    for _ in range(4):  # Loop through 4 bars (can adjust based on song length)
        for i in range(len(beat_grid.instruments)):
            instrument = beat_grid.instruments[i]
            for sound, beat_time in timed_grid[i]:
                time_diff = (beat_time - current_time) / 1000  # Convert to seconds
                if time_diff > 0:
                    time.sleep(time_diff)  # Wait until it's time to play the next sound
                current_time = beat_time

                # Play the corresponding sound
                if instrument == "kick":
                    play(kick)
                elif instrument == "snare":
                    play(snare)
                elif instrument == "hihat":
                    play(hihat)
                elif instrument == "piano":
                    play(piano)
