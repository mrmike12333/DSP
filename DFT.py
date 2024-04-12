import numpy as np

def calc_dft(x: np.ndarray, num_freq_bins: int, scale: bool):
    """A Simple Discrete Fourier Transform implementation
    NOTE: Only works for len(x) == num_freq_bins so make 
    sure to pad and truncate if needed!!

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
    assert x.ndim == 1
    assert len(x) == num_freq_bins

    num_samples = x.shape[0]

    dft = np.zeros(num_freq_bins, dtype='complex_')

    # The discrete time vector
    n = np.arange(num_samples)

    for freq_bin in range(num_freq_bins):
        complex_sine = np.exp((-2j * np.pi * freq_bin * n) / num_freq_bins)

        dft[freq_bin] = np.sum(np.multiply(x, complex_sine))

    if scale:
        dft /= np.max(np.abs(dft))
    return dft

def calc_inverse_dft(dft: np.ndarray):
    """Implementation of the Discrete Fourier Transform

    Args:
        dft (np.ndarray): A discrete fourier transform object

    Returns:
        np.ndarray: Return the original signal which the dft was calculated from. 
        NOTE: Length will be NFFT of the input dft spectrum
    """
    num_samples = len(dft)
    op_signal = np.zeros(num_samples)

    # The vector of frequency bins
    freq_vec = np.arange(num_samples)

    for sample in range(num_samples):
        complex_sine = np.exp((2j * np.pi * sample * freq_vec) / num_samples)

        idft = np.sum(np.multiply(dft, complex_sine))

        op_signal[sample] = np.real(idft) / num_samples
    return op_signal
