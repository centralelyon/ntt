from ntt.draw.polygone import draw_polygones
import cv2, json,os
from dotenv import load_dotenv
jsonfile = f"{os.environ.get('PATH_IN')}2023_CF_Rennes_freestyle_hommes_50_finaleA.json"


def extract_piscine(jsonfile):
    """This function finds the 4 edges of the swimming pool given the json file of a competition

    Args:
        jsonfile (json): path to the json file containing the competition annotation

    Returns:
        list[list]: list of the pixel coordinates of the four edges od the swimming pool
    """
    with open(jsonfile, "rb") as f:
        data = json.load(f)
    x0, y0 = map(int, data["videos"][1]["srcPts"][0])
    x1, y1 = map(int, data["videos"][1]["srcPts"][1])
    x2, y2 = map(int, data["videos"][1]["srcPts"][2])
    x3, y3 = map(int, data["videos"][1]["srcPts"][3])
    return [[y0, x0], [y1, x1], [y2, x2], [y3, x3]]

load_dotenv()
piscine = extract_piscine(jsonfile)
# dessin piscine avec ntt


# Ouvrir la vidéo
video = cv2.VideoCapture(
    f"{os.environ.get('VIDEO_PATH_IN')}2023_CF_Rennes_freestyle_hommes_50_finaleA_fixeDroite.mp4"
)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv2.CAP_PROP_FPS)

# Define the codec for the output video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output_video = cv2.VideoWriter(
    f"{os.environ.get('PATH_OUT')}output_piscine.mp4", fourcc, fps, (width, height)
)
while True:
    # Lire une image de la vidéo
    ret, frame = video.read()
    draw_polygones(frame, piscine, couleur=[0, 255, 0], epaisseur=3)

    # Write the processed frame to the output video
    output_video.write(frame)

    # Vérifier si la lecture de la vidéo est terminée
    if not ret:
        break

    # Wait for the 'q' key to quit
# Libérer les ressources
video.release()
output_video.release()
