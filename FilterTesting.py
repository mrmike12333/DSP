import numpy as np
from matplotlib import pyplot as plt

# Define filter in the S domain


def calcAmplitudeAtFrequency(f, cutoff, order):
    G_0 = 1
    w = 2 * np.pi * f # Frequency rads/s
    w_c = 2 * np.pi * cutoff
    
    H_jw = (G_0 ** 2) / ((1 + (w / w_c) ** (2 * order)))
    
    return np.sqrt(H_jw)

cutoffFrequency = 100 # Hz
filterOrder = 1

print("Gain in pass band:", calcAmplitudeAtFrequency(200, cutoffFrequency, filterOrder))
print("Gain at -3dB point", calcAmplitudeAtFrequency(cutoffFrequency, cutoffFrequency, filterOrder))
print("Gain at Double:", calcAmplitudeAtFrequency(cutoffFrequency * 2, cutoffFrequency, filterOrder))

frequencyAxis = np.linspace(20, 1000, 50)

for filterOrder in range(1, 9):
    frequencyResponse = calcAmplitudeAtFrequency(frequencyAxis, cutoff=cutoffFrequency, order=filterOrder)
    plt.semilogx(frequencyAxis, 20 * np.log10(np.abs(frequencyResponse)), label=str(filterOrder))
    
plt.xlabel("Frequency")
plt.ylabel("Amplitude (dB)")
plt.axvline(cutoffFrequency, color="red", label="Cutoff frequency", linestyle="-.")
plt.axhline(-3, color="Green", label="-3dB point", linestyle="-.")   
plt.ylim(bottom=-100, top=6)
plt.legend()
plt.grid()
plt.show()