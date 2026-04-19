import logging
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
import pyttsx3
from PIL import Image

class VideoGenerator:
    def __init__(self, output_directory, fps=30, resolution=(1920, 1080), script_path=None, audio_path=None, video_segments=None):
        self.output_directory = output_directory
        self.fps = fps
        self.resolution = resolution
        self.script_path = script_path or 'default_script.txt'
        self.audio_path = audio_path or 'default_audio.mp3'
        self.video_segments = video_segments or []
        logging.basicConfig(level=logging.INFO)

    def generate_audio(self, text):
        engine = pyttsx3.init()
        engine.save_to_file(text, self.audio_path)
        engine.runAndWait()
        logging.info(f'Audio generated and saved to {self.audio_path}')

    def create_video_segment(self, image_path, duration):
        try:
            clip = ImageClip(image_path).set_duration(duration).resize(self.resolution)
            logging.info(f'Video segment created for {image_path} with duration {duration}')
            return clip
        except Exception as e:
            logging.error(f'Error creating video segment for {image_path}: {e}')
            raise

    def compose_video(self):
        try:
            video_clips = []
            for segment in self.video_segments:
                video_clips.append(self.create_video_segment(segment['image_path'], segment['duration']))
            final_video = concatenate_videoclips(video_clips)
            final_video.set_duration(len(video_clips) / self.fps)
            final_video.write_videofile(os.path.join(self.output_directory, 'final_video.mp4'), fps=self.fps)
            logging.info('Video composition complete. Video saved.')
        except Exception as e:
            logging.error(f'Error during video composition: {e}')
            raise

# Example usage:
# generator = VideoGenerator(output_directory='output', script_path='script.txt', audio_path='audio.mp3')
# generator.generate_audio('This is an example audio.');
# generator.compose_video()