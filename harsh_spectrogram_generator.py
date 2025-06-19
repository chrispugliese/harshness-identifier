import librosa 
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os



def save_mel_spectrogram(wav_path, out_path, sr=22050):
    y, sr = librosa.load(wav_path, sr=sr)
    
    # Generate Mel spectrogram
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
    S_dB = librosa.power_to_db(S, ref=np.max)
    
    # Save as PNG
    plt.figure(figsize=(2.56, 2.56))  # For 256x256 images
    librosa.display.specshow(S_dB, sr=sr, x_axis=None, y_axis=None)
    plt.axis('off')  # No ticks or borders
    plt.tight_layout()
    plt.savefig(out_path, bbox_inches='tight', pad_inches=0)
    plt.close()

def convert_all_wavs_to_spectrograms(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    skipped = []

        
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.wav'):
            wav_path = os.path.join(input_dir, filename)
            out_path = os.path.join(output_dir, filename.replace('.wav', '.png'))

            try:
                save_mel_spectrogram(wav_path, out_path)
            except Exception as e:
                print(f"⚠️ Skipping {filename}: {e}")
                skipped.append(filename)

    print(f"\nDone. Skipped {len(skipped)} files.")


if __name__ == "__main__":
    input_dir = "/Users/chrispugliese/Desktop/git/CS3120/final_project/data/audio_files/harsh"
    output_dir = "/Users/chrispugliese/Desktop/git/CS3120/final_project/data/spectrograms/harsh2"

    convert_all_wavs_to_spectrograms(input_dir, output_dir)
