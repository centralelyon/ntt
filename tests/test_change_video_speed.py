import os
from ntt.videos.change_speed import change_video_speed
from moviepy.editor import VideoFileClip
from dotenv import load_dotenv

load_dotenv()


def test_change_video_speed():
    video_file_in = os.path.join(os.environ.get("VIDEO_PATH_IN"), "ping.mp4")
    video_file_out = os.path.join(os.environ.get("PATH_OUT"), "ping_speed.mp4")

    if not os.path.exists(os.environ.get("PATH_OUT")):
        os.makedirs(os.environ.get("PATH_OUT"))

    change_video_speed(video_file_in, video_file_out, 1)

    video_in = VideoFileClip(video_file_in)
    video_out = VideoFileClip(video_file_out)

    # info video_in.reader.nframes does not give the sama values of nb frames
    nb_frames_video_in = video_in.fps * video_in.duration
    nb_frames_video_out = video_out.fps * video_out.duration

    # change of speed 1x does not change videos
    assert nb_frames_video_in == nb_frames_video_out

    change_video_speed(video_file_in, video_file_out, 2)
    video_in = VideoFileClip(video_file_in)
    video_out = VideoFileClip(video_file_out)

    nb_frames_video_in = video_in.fps * video_in.duration
    nb_frames_video_out = video_out.fps * video_out.duration

    # change of speed 2x has less frames
    assert nb_frames_video_in > nb_frames_video_out

    change_video_speed(video_file_in, video_file_out, 0.5)
    video_in = VideoFileClip(video_file_in)
    video_out = VideoFileClip(video_file_out)

    nb_frames_video_in = video_in.fps * video_in.duration
    nb_frames_video_out = video_out.fps * video_out.duration

    # change of speed .5x has more frames
    assert nb_frames_video_in < nb_frames_video_out


if __name__ == "__main__":
    test_change_video_speed()
