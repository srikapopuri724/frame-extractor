import cv2
import os
import argparse


def extract_frames(video_path, output_dir, every_n=30):
    """Read a video and save every Nth frame as a JPEG image."""
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise FileNotFoundError(f"Could not open video: {video_path}")

    frame_idx = 0
    saved = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # no more frames

        if frame_idx % every_n == 0:
            out_path = os.path.join(output_dir, f"frame_{frame_idx:05d}.jpg")
            cv2.imwrite(out_path, frame)
            saved += 1

        frame_idx += 1

    cap.release()
    print(f"Done. Read {frame_idx} frames, saved {saved} to '{output_dir}'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract every Nth frame from a video.")
    parser.add_argument("video", help="Path to the input video file")
    parser.add_argument("--output", default="frames", help="Output folder (default: frames)")
    parser.add_argument("--every", type=int, default=30, help="Save every Nth frame (default: 30)")
    args = parser.parse_args()

    extract_frames(args.video, args.output, args.every)