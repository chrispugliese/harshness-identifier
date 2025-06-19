from pydub import AudioSegment
from pydub.effects import high_pass_filter, low_pass_filter
import os

def simulate_harshness(input_path, output_path):
    audio = AudioSegment.from_file(input_path)

    # Boost 2–4 kHz range
    band = high_pass_filter(audio, 2000)
    band = low_pass_filter(band, 4000)
    boosted = band + 10  # Boost mids by 10 dB

    # Overlay boosted mids on original
    harsh_audio = audio.overlay(boosted)

    # Slight clipping effect
    harsh_audio += 4

    # Export to output
    harsh_audio.export(output_path, format="wav")


def convert_clean_to_harsh(clean_dir, harsh_dir):
    os.makedirs(harsh_dir, exist_ok=True)

    for filename in os.listdir(clean_dir):
        if filename.endswith(".wav"):
            in_path = os.path.join(clean_dir, filename)
            out_path = os.path.join(harsh_dir, filename)

            try:
                simulate_harshness(in_path, out_path)
            except Exception as e:
                print(f"⚠️ Skipped {filename}: {e}")


if __name__ == "__main__":
    input_dir = "/Users/chrispugliese/Desktop/git/CS3120/final_project/data/audio_files/clean"
    output_dir = "/Users/chrispugliese/Desktop/git/CS3120/final_project/data/audio_files/clean"

    convert_clean_to_harsh(input_dir, output_dir)