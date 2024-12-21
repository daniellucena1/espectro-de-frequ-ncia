import numpy as np
import librosa
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
 
audio_path = "something.mp3"
audio_array, taxa_hz = librosa.load(audio_path, sr=None)

downsample_factor = 1000 
audio_array_downsampled = audio_array[::downsample_factor]

audio_array_normalized =audio_array_downsampled / np.max(np.abs(audio_array_downsampled))

plt.figure(figsize=(12, 3))
plt.plot(audio_array_normalized, color="black", linewidth=1) 
plt.axis("off")  
plt.tight_layout()

imagem_salva = "src/images/espectograma_simplificado.png"
plt.savefig(imagem_salva, bbox_inches='tight', pad_inches=0, dpi=300)
plt.close()

print(f"Imagem simples salva em: {imagem_salva}")
