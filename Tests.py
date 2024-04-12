import DFT
import SignalGenerator
from matplotlib import pyplot as plt
import numpy as np

# A test script for checking code implementation
# -------------------------

# Test Values
FREQ = 1000
FS = 44100
NFFT = int(2 ** 8)
LENGTH_SECONDS = NFFT / FS # Right now only supports NFFT length signals

input_signal = SignalGenerator.create_sine(FREQ, 0, LENGTH_SECONDS * FS, FS)

plt.subplot(311)
plt.title("Input signal")
time = np.linspace(0, LENGTH_SECONDS, int(FS * LENGTH_SECONDS))
plt.plot(time, input_signal)

plt.subplot(312)
plt.title("DFT of signal")
freq_spectrum = DFT.calc_dft(input_signal, NFFT, False)
freq_axis = np.linspace(0, FS, NFFT)

plt.plot(freq_axis, np.abs(freq_spectrum), label="DFT")
plt.axvline(FREQ, label="Input Frequency", color="orange")
plt.axvline(FS - FREQ, label="Input Frequency", color="orange")
plt.legend()

plt.subplot(313)
op_signal = DFT.calc_inverse_dft(freq_spectrum)
plt.title("Inverse DFT signal")
plt.plot(time, op_signal)

plt.show()