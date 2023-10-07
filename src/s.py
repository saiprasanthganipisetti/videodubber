from pytube import YouTube

# Replace 'youtube_video_url' with the URL of the YouTube video you want to download
youtube_video_url = 'https://www.youtube.com/watch?v=12qEBzM-yKc'

# Create a YouTube object
yt = YouTube(youtube_video_url)

# Select the stream with the audio (usually the highest quality)
audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

# Replace 'output_audio.mp3' with the desired name for the extracted audio file
output_audio_path = 'output_audio.mp3'

# Download the audio stream
audio_stream.download(output_path='.', filename=output_audio_path)

print(f"Audio extracted and saved as '{output_audio_path}'")
