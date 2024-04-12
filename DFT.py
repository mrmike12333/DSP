import numpy as np

def calc_dft(x: np.ndarray, num_freq_bins: int, scale: bool):
    """A Simple Discrete Fourier Transform implementation

    Args:
        x (np.ndarray): Some real input signal
        num_freq_bins (int):    The number of frequency bins to perform
                                the DFT over.
                                NOTE: Remember that this is from 0->Fs
        scale (bool): Scale the DFT so the max value is 1

    Returns:
        np.ndarray: The complex Fourier Transform of input x.
    """
    # Only support mono
    assert(x.ndim == 1)

    num_samples = x.shape[0]

    dft = np.zeros(num_freq_bins)

    # The discrete time vector
    n = np.arange(num_samples)

    for freq_bin in range(num_freq_bins):
        complex_sine = np.exp((-1j * 2 * np.pi * freq_bin * n) / num_freq_bins)

        dft[freq_bin] = np.sum(np.multiply(x, complex_sine))

    if scale:
       dft /= np.max(np.abs(dft))
       
    return dft
