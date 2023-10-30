import noisereduce as nr

def reduce_noise(audio_clip, sample_rate):
    # Assuming the first 0.5 seconds of the recorded audio is noise
    noise_clip = audio_clip[:int(0.5 * sample_rate)]
    reduced_noise = nr.reduce_noise(audio_clip=audio_clip, noise_clip=noise_clip, verbose=False)
    return reduced_noise
