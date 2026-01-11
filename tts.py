import subprocess

VOICE_MODEL = "voices/en_US-lessac-medium.onnx"

subprocess.run(
    [
        "piper",
        "--model", VOICE_MODEL,
        "--output_file", "voice.wav"
    ],
    input=open("script.txt", "r", encoding="utf-8").read(),
    text=True
)

print("Voice narration created.")

