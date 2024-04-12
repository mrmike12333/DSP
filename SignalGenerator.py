import numpy as np

def create_sine(frequency, phase_offset: float, length_samples: int, sample_rate: int):
    """Generate a sine wave with the following parameters:
        
    Args:
        frequency (int, float): The frequency of the sine wave in Hz.
        phase_offset (float): The start offset of the sinewave in radians.
        length_samples (int): Length of the generated sine wave in number of samples.
        sample_rate (int): The Sample rate to generate at.

    Returns:
        np.array: The generated sine wave as a numpy array
    """
    time = np.arange(length_samples) / sample_rate
    omega = 2 * np.pi * frequency

    sine = np.sin(omega * time + phase_offset)
    return sine
    