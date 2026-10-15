
import wave
from pathlib import Path


def inspect_wav_audio_file(file_path):
    """Inspect WAV metadata and check whether the sample rate is 16 kHz."""

    audio_path = Path(file_path)

    # Validate the file
    if not audio_path.exists() or not audio_path.is_file():
        print(f"[ERROR] File not found: {file_path}")
        return

    if audio_path.suffix.lower() != ".wav":
        print("[ERROR] Invalid file type. Please provide a .wav file.")
        return

    try:
        with wave.open(str(audio_path), "rb") as wav_file:
            channels = wav_file.getnchannels()
            sample_width = wav_file.getsampwidth()
            sample_rate = wav_file.getframerate()
            total_frames = wav_file.getnframes()

            # Calculate duration
            duration = total_frames / sample_rate if sample_rate else 0

            channel_type = {
                1: "Mono",
                2: "Stereo"
            }.get(channels, f"{channels} channels")

            print("\n--- Audio File Properties ---")
            print(f"File Name: {audio_path.name}")
            print(f"Channels: {channels} ({channel_type})")
            print(f"Sample Width: {sample_width * 8}-bit")
            print(f"Sample Rate: {sample_rate} Hz")
            print(f"Total Frames: {total_frames}")
            print(f"Duration: {duration:.2f} seconds")

            if sample_rate == 16000:
                print("[OK] Sample rate meets the 16 kHz standard.")
            else:
                print(
                    f"[WARN] Sample rate is {sample_rate} Hz, "
                    "not 16000 Hz. Resampling is recommended."
                )

    except (wave.Error, EOFError, OSError) as error:
        print(f"[ERROR] Unable to read WAV file: {error}")


if __name__ == "__main__":
    print("Day 16 - Audio Preprocessing Module")
    print("Enter a WAV file path, or press Enter to exit.")

    while True:
        file_path = input("\nWAV file path: ").strip().strip('"')

        if not file_path:
            print("Program ended.")
            break

        inspect_wav_audio_file(file_path)
