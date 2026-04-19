import argparse
import os
from video_generator import CivilRightsVideoGenerator

def main():
    parser = argparse.ArgumentParser(description='Generate civil rights videos.')
    parser.add_argument('--script-path', type=str, help='Path to the script file.', default='script.txt')
    parser.add_argument('--audio-path', type=str, help='Path to save the generated audio.', default='output/audio.mp3')
    parser.add_argument('--video-segments', type=str, help='Comma-separated list of video segments.', default='segment1,segment2')
    parser.add_argument('--output-dir', type=str, help='Directory to save the generated videos.', default='output')
    parser.add_argument('--fps', type=int, help='Frames per second for the video.', default=30)
    parser.add_argument('--resolution', type=str, help='Resolution of the video (e.g. 1920x1080).', default='1920x1080')

    args = parser.parse_args()

    # Create the output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)

    # Parse video segments
    video_segments = args.video_segments.split(',')

    # Initialize the generator with provided parameters
    generator = CivilRightsVideoGenerator(
        script_path=args.script_path,
        audio_path=args.audio_path,
        video_segments=video_segments,
        output_directory=args.output_dir,
        fps=args.fps,
        resolution=args.resolution
    )

    # Start video generation
    generator.compose_video()

if __name__ == '__main__':
    main()