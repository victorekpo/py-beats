from pydub import AudioSegment
from pydub.playback import play
from pydub.silence import detect_nonsilent
import time

# Load samples (ensure these files are correct)
kick = AudioSegment.from_file("./src/07_Kick_03_SP.wav")
snare = AudioSegment.from_file("./src/07_Snare_01_SP.wav")
hihat = AudioSegment.from_file("./src/07_Hats_14_SP.wav")
piano = AudioSegment.from_file("./src/07_Hats_14_SP.wav")  # A piano note

# 🎚️ Helper: Trim silence dynamically and manually
def trim_audio(audio, silence_thresh=-20, buffer_ms=0, trim_location=None, trim_length_ms=None):
    """
    Trims silence from the beginning and end of the audio dynamically or manually.
    :param audio: AudioSegment to trim.
    :param silence_thresh: dB threshold to detect silence.
    :param buffer_ms: Extra buffer to avoid over-trimming.
    :param trim_location: Where to trim ("beginning", "end", or "specific_time").
    :param trim_length_ms: Length of the trim in milliseconds for specific time.
    :return: Trimmed AudioSegment.
    """
    # Trim silence dynamically
    non_silent_ranges = detect_nonsilent(audio, min_silence_len=10, silence_thresh=silence_thresh)
    if not non_silent_ranges:
        print("No non-silent audio detected.")  # Debugging output
        return audio  # No sound detected, return original audio

    print(f"Non-silent ranges: {non_silent_ranges}")  # Debugging output
    start_trim, end_trim = non_silent_ranges[0][0], non_silent_ranges[-1][1]

    trimmed_audio = audio[start_trim:end_trim]  # Dynamically trimmed audio

    # Manual trimming based on location
    if trim_location == "beginning" and trim_length_ms is not None:
        trimmed_audio = trimmed_audio[trim_length_ms:]  # Trim from the beginning
    elif trim_location == "end" and trim_length_ms is not None:
        trimmed_audio = trimmed_audio[:-trim_length_ms]  # Trim from the end
    elif trim_location == "specific_time" and trim_length_ms is not None:
        trimmed_audio = trimmed_audio[trim_length_ms:]  # Trim at a specific time (after the given length)

    # Apply buffer if necessary
    if buffer_ms > 0:
        trimmed_audio = trimmed_audio[:buffer_ms]  # Apply buffer at the end

    return trimmed_audio

# 🎚️ Apply a simple reverb effect (for a slight echo)
def apply_reverb(audio, reverb_amount=5):
    """
    Apply a basic reverb effect to the audio using volume manipulation.
    :param audio: AudioSegment to apply reverb to.
    :param reverb_amount: Amount of reverb effect (higher = more reverb).
    :return: AudioSegment with reverb.
    """
    reverb_audio = audio
    for i in range(reverb_amount):
        reverb_audio = reverb_audio + 2  # Simulate reverb by adding faint echoes
    return reverb_audio

# 🎚️ Apply a simple delay effect (for rhythmic echo)
def apply_delay(audio, delay_amount=100):
    """
    Apply a simple delay effect to the audio (in milliseconds).
    :param audio: AudioSegment to apply delay to.
    :param delay_amount: Delay in milliseconds.
    :return: AudioSegment with delay.
    """
    delay_audio = audio
    delay_audio = delay_audio + delay_amount  # Shift audio by delay
    return delay_audio

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
    return [piano, piano + 100]  # Simple ascending melody

# Play the beat
def play_beat():
    global kick, snare, hihat, piano  # Update samples globally to trim them

    # Trim all samples dynamically
    kick = trim_audio(kick, silence_thresh=-30, trim_location="end", trim_length_ms=130)
    snare = trim_audio(snare, silence_thresh=-30, trim_location="end", trim_length_ms=10)
    hihat = trim_audio(hihat, silence_thresh=-40, trim_location="end", trim_length_ms=10)
    piano = trim_audio(piano, silence_thresh=-20, trim_location="beginning", trim_length_ms=10)

    # Apply effects to the audio
    kick = apply_reverb(kick, reverb_amount=3)  # Reverb on kick
    snare = apply_delay(snare, delay_amount=150)  # Delay on snare

    pattern = create_drum_pattern()
    melody = create_melody()

    for _ in range(10):  # Repeat pattern 4 times for 1 bar
        for sound in pattern:
            play(sound)
          #  time.sleep(sound.duration_seconds)  # Wait for the sound to finish before playing the next one

        for note in melody:  # Play melody in between
            play(note)
           # time.sleep(note.duration_seconds)  # Wait for the melody to finish before the next note

# Main function to run the beat
if __name__ == "__main__":
    play_beat()
