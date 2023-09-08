from ntt.videos.overlay_videos import video_fusion_image
if __name__=="__main__":
    path_videos="./samples"
    name_video1="point_0.mp4"
    name_video2="point_1.mp4"
    video_out="overlayed_points.mp4"
    video_fusion_image(path_videos,name_video1,name_video2,video_out)