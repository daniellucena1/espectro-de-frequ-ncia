import numpy as np
import librosa
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

# Carregar o áudio
audio_path = "something.mp3"  # Substitua pelo caminho do áudio
audio_array, taxa_hz = librosa.load(audio_path, sr=None)

espectograma = librosa.amplitude_to_db(np.abs(librosa.stft(audio_array)), ref=np.max)

figura, ax = plt.subplots(figsize=(10, 5))
librosa.display.specshow(espectograma, sr=taxa_hz, x_axis='time', y_axis='hz', cmap='magma', ax=ax)
ax.axis('off') 

espectograma_salvo = "spectrogram.png"
plt.savefig(espectograma_salvo, bbox_inches='tight', pad_inches=0, dpi=300)
plt.close()

