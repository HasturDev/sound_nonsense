import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate

def detect_echo(original, recording, sample_rate):
    # Ensure both signals are mono (single channel)
    if len(original.shape) > 1:
        original = original[:, 0]
    if len(recording.shape) > 1:
        recording = recording[:, 0]

    # Cross-correlate the signals and find the delay
    correlation = correlate(recording, original, mode='full', method='auto')
    delay_samples = np.argmax(correlation) - (len(original) - 1)
    delay_time = delay_samples / sample_rate

    print(f"Estimated delay (echo): {delay_time} seconds")

    # Optional: Plot the correlation
    plt.figure()
    plt.plot(correlation)
    plt.title('Cross-correlation between original and recorded signal')
    plt.xlabel('Lag')
    plt.ylabel('Correlation')
    plt.show()

    return delay_time  # This could be useful for further processing or analysis
