import numpy as np
import sounddevice as sd

fs = 48000
duration = 1.0
frequency = 440.0

t = np.linspace(0, duration, int(fs * duration), endpoint=False)
waveform = 0.5 * np.sin(2 * np.pi * frequency * t)

sd.play(waveform, samplerate=fs, device=6)
sd.wait()

