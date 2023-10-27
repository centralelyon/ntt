import cv2


def show_video(video_path, window_name="Video"):
    """Show a video in a window

    Args:
        video_path (_type_): _description_
    """
    if True:
        cap_output = cv2.VideoCapture(video_path)
        while cap_output.isOpened():
            ret, frame_output = cap_output.read()
            if not ret:
                break
            cv2.imshow(window_name, frame_output)
            if cv2.waitKey(30) & 0xFF == 27:
                break
        cap_output.release()
        cv2.destroyAllWindows()
