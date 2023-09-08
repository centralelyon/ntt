from ntt.draw.primitives import draw_bright_circle
import cv2, json

jsonfile = "./samples/2023_CF_Rennes_freestyle_hommes_50_finaleA.json"
def extract_flash(jsonfile):
    with open(jsonfile,'rb') as f:
        data=json.load(f)
    x0,y0=map(int,data['flash']['pts'][0])
    x1,y1=map(int,data['flash']['pts'][1])
    x2,y2=map(int,data['flash']['pts'][2])
    x3,y3=map(int,data['flash']['pts'][3])
    return([(x0,y0),(x1,y1),(x2,y2),(x3,y3)])
flash=extract_flash(jsonfile)
# Ouvrir la vidéo
video = cv2.VideoCapture(
    "./samples/2023_CF_Rennes_freestyle_hommes_50_finaleA_fixeDroite.mp4"
)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv2.CAP_PROP_FPS)

# Define the codec for the output video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output_video = cv2.VideoWriter(
    "./samples/output_flash.mp4", fourcc, fps, (width, height)
)
while True:
    # Lire une image de la vidéo
    ret, frame = video.read()
    if not ret:
        break
    for (x,y) in flash:
        draw_bright_circle(frame, (x,y),20,100)

    # Write the processed frame to the output video
    output_video.write(frame)

    # Vérifier si la lecture de la vidéo est terminée
    

    # Wait for the 'q' key to quit
# Libérer les ressources
video.release()
output_video.release()
