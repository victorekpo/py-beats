from pydub import AudioSegment
from pydub.playback import play
import time

# Load samples (you need to have these sound files in the correct path)
kick = AudioSegment.from_file("./src/07_Kick_03_SP.wav")
snare = AudioSegment.from_file("./src/07_Snare_01_SP.wav")
hihat = AudioSegment.from_file("./src/07_Hats_14_SP.wav")
piano = AudioSegment.from_file("./src/Bass (6).wav")  # A piano note

# Create a basic drum pattern
def create_drum_pattern():
    pattern = []
    # Basic 4/4 rhythm: kick on beats 1 and 3, snare on 2 and 4
    for i in range(4):
        if i == 0 or i == 2:  # Kick on 1 and 3
            pattern.append(kick)
        elif i == 1 or i == 3:  # Snare on 2 and 4
            pattern.append(snare)
        else:
            pattern.append(hihat)  # Hi-hat as background
    return pattern

# Create a simple melody
def create_melody():
    return [piano, piano + 100, piano + 200]  # Simple ascending melody

# Play the beat
def play_beat():
    pattern = create_drum_pattern()
    melody = create_melody()
    for _ in range(4):  # Repeat pattern 4 times for 1 bar
        for sound in pattern:
            play(sound)
            time.sleep(0)  # Wait for the sound to finish before playing the next one

        for note in melody:  # Play melody in between
            play(note)
            time.sleep(0)
