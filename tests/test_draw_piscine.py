from ntt.draw.polygone import draw_polygones
import cv2, json, os
from dotenv import load_dotenv

load_dotenv()


def extract_piscine(jsonfile):
    try:
        with open(jsonfile, "rb") as f:
            data = json.load(f)
        x0, y0 = map(int, data["videos"][1]["srcPts"][0])
        x1, y1 = map(int, data["videos"][1]["srcPts"][1])
        x2, y2 = map(int, data["videos"][1]["srcPts"][2])
        x3, y3 = map(int, data["videos"][1]["srcPts"][3])
        return [[y0, x0], [y1, x1], [y2, x2], [y3, x3]]
    except Exception as e:
        print("Execption", e)


# draw swimming pool with ntt


def test_draw_piscine():
    jsonfile = os.path.join(
        os.environ.get("PATH_IN"), "2023_CF_Rennes_freestyle_hommes_50_finaleA.json"
    )
    video_name = os.path.join(
        os.environ.get("VIDEO_PATH_IN"),
        "2023_CF_Rennes_freestyle_hommes_50_finaleA_fixeDroite.mp4",
    )
    # open video
    piscine = extract_piscine(jsonfile)
    try:
        video = cv2.VideoCapture(video_name)
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = video.get(cv2.CAP_PROP_FPS)
        for l in piscine:
            assert l[0] >= 0 and l[0] < height and l[1] >= 0 and l[1] < width
    except Exception as e:
        print("Exception", e)

    # Define the codec for the output video
    fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")
    output_video = cv2.VideoWriter(
        os.path.join(os.environ.get("PATH_OUT"), "output_piscine.mp4"),
        fourcc,
        fps,
        (width, height),
    )
    while True:
        # read frame from video
        ret, frame = video.read()
        draw_polygones(frame, piscine, couleur=[0, 255, 0], epaisseur=3)

        # Write the processed frame to the output video
        output_video.write(frame)

        # verify if video reading process is finished
        if not ret:
            break

        # Wait for the 'q' key to quit
    # liberate resources
    video.release()
    output_video.release()


if __name__ == "__main__":
    test_draw_piscine()
