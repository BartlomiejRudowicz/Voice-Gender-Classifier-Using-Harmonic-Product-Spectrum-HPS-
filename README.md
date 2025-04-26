# Voice Gender Classifier Using Harmonic Product Spectrum (HPS)

This repository contains a Python script designed to classify the gender of a speaker (male or female) based on their voice. The classification uses the Harmonic Product Spectrum (HPS) method to analyze pitch frequencies within audio files in WAV format.

## Overview

The script processes audio signals, computes their frequency spectra using FFT and Hamming windowing, and employs the HPS algorithm to effectively identify the fundamental frequency. By analyzing specific frequency ranges characteristic for male and female voices, it determines the gender of the speaker.

## Requirements

- Python 3.x
- NumPy
- SciPy

You can install the required libraries with:

```bash
pip install numpy scipy
```

## Usage

Run the script from the command line, passing a single WAV file as an argument:

```bash
python program.py path_to_audio.wav
```

### Example

```bash
python program.py sample_voice.wav
```

The script will output:

- `M` for male voice
- `K` for female voice (from Polish "kobieta")

## How it Works

### Harmonic Product Spectrum (HPS)

The HPS algorithm enhances the clarity of the fundamental frequency in audio signals by iteratively multiplying frequency spectra at integer harmonic intervals. This effectively reduces noise and highlights the most prominent pitch.

### Frequency Ranges

- **Male Voices**: typically between 85 Hz to 180 Hz
- **Female Voices**: typically between 165 Hz to 255 Hz

