#!/usr/bin/python3

import numpy as np
import sounddevice as sd
import toml
from dataclasses import dataclass

@dataclass
class AudioConfig:
    device_index_input: int
    device_index_output: int
    sample_rate: int
    channels: int

@dataclass
class Note:
    freq: float
    duration: float
    amplitude: float
    generator: callable

@dataclass
class HarmonicSettings:
    num_harmonics: int
    harmonic_amp: float
    falloff: float

def sine_wave(freq, t):
    return np.sin(2 * np.pi * freq * t)

def harmonic_generator(settings: HarmonicSettings):
    def generator(freq, t):
        waveform = np.sin(2 * np.pi * freq * t)
        for i in range(1, settings.num_harmonics + 1):
            overtone = 2 * i + 1
            attenuation = settings.harmonic_amp / (settings.falloff ** (i - 1))
            waveform += attenuation * np.sin(2 * np.pi * overtone * freq * t)
        return waveform
    return generator

def load_config(path: str) -> AudioConfig:
    cfg = toml.load(path)
    return AudioConfig(cfg["device_index_input"], cfg["device_index_output"],
                       cfg["sample_rate"], cfg["channels"])

def generate_wave(note: Note, sample_rate: int):
    t = np.linspace(0, note.duration, int(note.duration * sample_rate), endpoint=False)
    return note.amplitude * note.generator(note.freq, t)

def play_note(cfg: AudioConfig, note: Note):
    sig = generate_wave(note, cfg.sample_rate)
    if cfg.channels == 2:
        sig = np.column_stack([sig, sig])
    elif cfg.channels != 1:
        raise ValueError("Only 1 or 2 channels supported")
    sd.play(sig, samplerate=cfg.sample_rate, device=cfg.device_index_output )
    sd.wait()

def main():
    cfg = load_config("audio_config.toml")
    harmonic_settings = HarmonicSettings(10, 0.04, 1.4)
    gen = harmonic_generator(harmonic_settings)
    note = Note(440.0, 2.0, 0.5, gen)
    #note = Note(440.0, 2.0, 0.5, sine_wave)
    play_note(cfg, note)

if __name__ == "__main__":
    main()

