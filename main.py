import numpy as np
import librosa
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

# Carregar o áudio
audio_path = "something.mp3"  # Substitua pelo caminho do áudio
audio_array, taxa_hz = librosa.load(audio_path, sr=None)

espectograma = librosa.amplitude_to_db(np.abs(librosa.stft(audio_array)), ref=np.max)

