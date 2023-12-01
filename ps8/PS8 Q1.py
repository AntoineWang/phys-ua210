from numpy import loadtxt
import matplotlib.pyplot as plt
import numpy as np
from numpy import zeros
from cmath import exp,pi

T=1/44100

piano = loadtxt("piano.txt",float)
plt.plot(piano)
plt.xlabel("time (s)")
plt.ylabel("amplitude (unit)")
plt.title("Amplitude and time for piano signal")
plt.show()

piano_fft = np.fft.fft(piano)
n_piano=piano.size
piano_fft_freq = np.fft.fftfreq(n_piano,T)
plt.plot(piano_fft_freq,abs(piano_fft))
plt.xlabel("Frequencies (1/s)")
plt.ylabel("Amplitude (unit)")
plt.title("Frequencies for the piano signal")
plt.xlim(0,10000)
plt.show()

trumpet = loadtxt("trumpet.txt",float)
plt.plot(trumpet)
plt.xlabel("time (s)")
plt.ylabel("amplitude (unit)")
plt.title("Amplitude and time for trumpet signal")
plt.show()

trumpet_fft = np.fft.fft(trumpet)
n_trumpet=trumpet.size
trumpet_fft_freq = np.fft.fftfreq(n_trumpet,T)
plt.plot(trumpet_fft_freq,abs(trumpet_fft))
plt.xlabel("Frequencies (1/s)")
plt.ylabel("Amplitude (unit)")
plt.title("Frequencies for the trumpet signal")
plt.xlim(0,10000)
plt.show()

abs_fft_piano = abs(piano_fft)
index_piano = np.argmax(abs_fft_piano)
print(abs(piano_fft_freq[index_piano]))

abs_fft_trumpet = abs(trumpet_fft)
index_trumpet = np.argmax(abs_fft_trumpet)
print(abs(trumpet_fft_freq[index_trumpet]))

