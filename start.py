
# putting this first import as a placeholder 
import sounddevice as sd
import numpy as np
import soundfile as sf
from frequency_analysis import plot_frequency_spectrum
from noise_reduction import reduce_noise
from signal_correlation import detect_echo

# Constants
RECORD_SECONDS = 5
SAMPLE_RATE = 44100
TRIGGER_FREQ = 1000
TRIGGER_DURATION = 0.1

def main():
    # Step 1: Generate and play a trigger sound
    trigger_sound = generate_trigger_sound()
    sd.play(trigger_sound, SAMPLE_RATE)
    sd.wait()

    print("Recording sound...")
    recorded_audio = record_sound()

    print("Reducing noise...")
    reduced_noise = reduce_noise(recorded_audio, SAMPLE_RATE)

    print("Analyzing for echo...")
    detect_echo(trigger_sound, reduced_noise, SAMPLE_RATE)

    print("Performing frequency analysis...")
    plot_frequency_spectrum(reduced_noise, SAMPLE_RATE)

    print("All steps completed.")

def generate_trigger_sound():
    t = np.linspace(0, TRIGGER_DURATION, int(TRIGGER_DURATION * SAMPLE_RATE), False)
    trigger = 0.5 * np.sin(2 * np.pi * TRIGGER_FREQ * t)
    return trigger

def record_sound():
    recording = sd.rec(int(RECORD_SECONDS * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='float32')
    sd.wait()
    return recording

# Execute the script
if __name__ == "__main__":
    main()
