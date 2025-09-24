from ntt.videos.video_generation import random_video


def test_random_video():

    video = random_video(320, 240, 10, 2)
    assert len(video) == 20
    assert video[0].shape == (320, 240, 3)


if __name__ == "__main__":
    test_random_video()
