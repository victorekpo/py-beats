from pydub import AudioSegment
from pydub.playback import play
from pydub.silence import detect_nonsilent
import time

# Load samples (ensure these files are correct)
kick = AudioSegment.from_file("./src/07_Kick_03_SP.wav")
snare = AudioSegment.from_file("./src/07_Snare_01_SP.wav")
hihat = AudioSegment.from_file("./src/07_Hats_14_SP.wav")
piano = AudioSegment.from_file("./src/Bass (6).wav")  # A piano note

# 🎚️ Helper: Trim silence dynamically
def trim_audio(audio, silence_thresh=-40, buffer_ms=10):
    """
    Trims silence from the beginning and end of the audio dynamically.
    :param audio: AudioSegment to trim.
    :param silence_thresh: dB threshold to detect silence.
    :param buffer_ms: Extra buffer to avoid over-trimming.
    :return: Trimmed AudioSegment.
    """
    non_silent_ranges = detect_nonsilent(audio, min_silence_len=10, silence_thresh=silence_thresh)

    if not non_silent_ranges:
        print("No non-silent audio detected.")  # Debugging output
        return audio  # No sound detected, return original audio

    print(f"Non-silent ranges: {non_silent_ranges}")  # Debugging output

    # Instead of trimming from both ends, return only the non-silent part
    start_trim, end_trim = non_silent_ranges[0][0], non_silent_ranges[-1][1]

    return audio[start_trim:end_trim]  # Only the non-silent part

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
    global kick, snare, hihat, piano  # Update samples globally to trim them

    # Trim all samples dynamically
    kick = trim_audio(kick, silence_thresh=-50)  # Higher threshold for stricter silence trimming
    snare = trim_audio(snare, silence_thresh=-50)
    hihat = trim_audio(hihat, silence_thresh=-50)
    piano = trim_audio(piano, silence_thresh=-50)

    pattern = create_drum_pattern()
    melody = create_melody()

    for _ in range(4):  # Repeat pattern 4 times for 1 bar
        for sound in pattern:
            play(sound)  # Play each sound in the pattern

        for note in melody:  # Play melody in between
            play(note)  # Play melody

# Main function to run the beat
if __name__ == "__main__":
    play_beat()
