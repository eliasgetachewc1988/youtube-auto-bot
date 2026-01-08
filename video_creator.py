from moviepy.editor import *
from moviepy.audio.fx.all import audio_loop

voice = AudioFileClip("voice.wav")
music = AudioFileClip("music.mp3").volumex(0.12)

music_looped = audio_loop(music, duration=voice.duration)
final_audio = CompositeAudioClip([music_looped, voice])

background = ImageClip("background.jpg") \
    .set_duration(voice.duration) \
    .resize(height=720) \
    .set_position("center")

video = background.set_audio(final_audio)

video.write_videofile(
    "final_video.mp4",
    fps=24,
    codec="libx264",
    audio_codec="aac",
    threads=4
)

print("Sleep video created.")
