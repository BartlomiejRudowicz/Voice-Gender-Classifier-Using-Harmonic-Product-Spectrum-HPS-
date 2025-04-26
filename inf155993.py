import sys
import numpy as np
from scipy.io import wavfile
from numpy.fft import rfft

#Parametry HPS
HARMONICS=4

def harmonic_product_spectrum(sample_rate, audio_signal):
    #Okno Hamminga i FFT
    window=np.hamming(len(audio_signal))
    fft_values=np.abs(rfft(audio_signal*window))

    #HPS-iteracyjne redukowanie widma
    hps_spectrum=fft_values.copy()
    for harmonic in range(2, HARMONICS+1):
        reduced=fft_values[::harmonic]
        hps_spectrum[:len(reduced)]*=reduced

    return hps_spectrum


def classify_gender(sample_rate, audio_data):
    #Oblicz widmo HPS dla całego sygnału
    spectrum=harmonic_product_spectrum(sample_rate, audio_data)

    #Oblicz częstotliwości FFT
    freqs=np.fft.rfftfreq(len(spectrum)*2-2, d=1/sample_rate)

    #Wyodrębnienie energii w zakresach dla mężczyzn i kobiet
    male_energy=sum(spectrum[(freqs>=85) & (freqs<=180)])
    female_energy=sum(spectrum[(freqs>=165) & (freqs<=255)])

    if male_energy>female_energy:
        return "M"
    return "K"

def algorithm():
    if len(sys.argv)!=2:
        print("Użycie: python program.py <plik.wav>")
        sys.exit(1)

    file_path=sys.argv[1]
    sample_rate, data=wavfile.read(file_path)

    #Konwersja stereo na mono, jeśli konieczne
    if len(data.shape)>1:
        data=np.mean(data, axis=1)

    gender=classify_gender(sample_rate, data)
    print(gender)


algorithm()