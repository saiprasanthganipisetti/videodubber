from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.tools.subtitles import SubtitlesClip

video_clip = VideoFileClip("original.mp4")

subtitles = SubtitlesClip("subtitle2.srt")

video_with_subtitles = video_clip.set_subtitles(subtitles)

video_with_subtitles.write_videofile("output_video.mp4")
