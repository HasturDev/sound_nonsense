import numpy as np
import matplotlib.pyplot as plt

def plot_frequency_spectrum(audio_data, sample_rate):
    # FFT and frequency calculations
    fft_out = np.fft.rfft(audio_data[:, 0])  # Assuming audio_data is a 2D array with a single channel
    fft_frequency = np.fft.rfftfreq(len(audio_data), d=1./sample_rate)
    magnitude = np.abs(fft_out)

    # Plotting
    plt.figure(figsize=(12, 4))
    plt.title("Frequency Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.plot(fft_frequency, magnitude)
    plt.grid()
    plt.show()
