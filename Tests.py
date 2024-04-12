import DFT
import SignalGenerator
from matplotlib import pyplot as plt
import numpy as np

# A test script for checking code implementation
# -------------------------

# Test Values
FREQ = 1000
LENGTH_SECONDS = 1
FS = 44100
NFFT = int(2 ** 8)

input_signal = SignalGenerator.create_sine(FREQ, 0, LENGTH_SECONDS * FS, FS)

plt.figure()
time = np.linspace(0, LENGTH_SECONDS, FS)
plt.plot(time, input_signal)

plt.figure()
freq_spectrum = DFT.calc_dft(input_signal, NFFT, False)
freq_axis = np.linspace(0, FS, NFFT)

plt.plot(freq_axis, np.abs(freq_spectrum), label="DFT")
plt.axvline(FREQ, label="Input Frequency", color="orange")
plt.axvline(FS - FREQ, label="Input Frequency", color="orange")
plt.legend()

plt.show()