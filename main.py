import argparse
import os
from civil_rights_video_generator import CivilRightsVideoGenerator


def main():
    parser = argparse.ArgumentParser(description='Generate civil rights videos.')
    parser.add_argument('--output-dir', type=str, help='Directory to save the generated videos.', default='output')
    parser.add_argument('--fps', type=int, help='Frames per second for the video.', default=30)
    parser.add_argument('--resolution', type=str, help='Resolution of the video (e.g. 1920x1080).', default='1920x1080')

    args = parser.parse_args()

    # Create the output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)

    # Initialize the generator with provided parameters
    generator = CivilRightsVideoGenerator(output_directory=args.output_dir, fps=args.fps, resolution=args.resolution)

    # Start video generation (assuming a method start() exists in CivilRightsVideoGenerator)
    generator.start()


if __name__ == '__main__':
    main()