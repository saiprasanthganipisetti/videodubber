import time
start = time.time()
from pydub import AudioSegment
# from moviepy.editor import AudioFileClip, concatenate_audioclips
def f1(audio_clips):

    total_duration_ms = 10000  # 10 seconds




    final_audio = AudioSegment.silent(duration=total_duration_ms)
    for clip in audio_clips:
        start_time = float(clip[1]) * 1000
        end_time = float(clip[2]) * 1000  
        clip_path = 'audios/'+clip[3]
        audio_clip = AudioSegment.from_mp3(clip_path)
        audio_clip = audio_clip[start_time:end_time]
        final_audio = final_audio.overlay(audio_clip, position=start_time)
    final_audio.export('pydubfinal_audio.mp3', format='mp3')

    print("Final audio file 'final_audio.mp3' created successfully.")

# def f2(audio_clips):

#     total_duration = 10  # seconds
#     final_audio = AudioFileClip("silence.mp3")

#     for clip in audio_clips:
#         start_time = float(clip[1])
#         end_time = float(clip[2])
#         clip_path = 'audios/'+clip[3]

#         audio_clip = AudioFileClip(clip_path).subclip(start_time, end_time)

#         final_audio = concatenate_audioclips([final_audio, audio_clip])

#     final_audio.write_audiofile('moviepyfinal_audio.mp3', codec='mp3')

#     print("Final audio file 'final_audio.mp3' created successfully.")


arr = [[1, '00.0', '06.0', 'gtts1.mp3'], [2, '010.0', '013.0', 'gtts2.mp3'], [3, '016.0', '020.0', 'gtts3.mp3'], [4, '023.0', '026.0', 'gtts4.mp3'], [5, '026.0', '031.0', 'gtts5.mp3'], [6, '040.0', '047.0', 'gtts6.mp3'], [7, '050.0', '054.0', 'gtts7.mp3'], [8, '055.0', '062.0', 'gtts8.mp3'], [9, '063.0', '065.0', 'gtts9.mp3']]
temp = time.time()
print("temp:",temp-start)
# f1(arr)
# f1time = time.time()
# print("Time taken for pydub:",f1time - temp)
f1(arr)
f1time = time.time()
print("Time taken for moviepy:", f1time - temp)