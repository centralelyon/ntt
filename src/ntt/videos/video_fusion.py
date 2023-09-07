from moviepy.editor import VideoFileClip, CompositeVideoClip
def video_fusion_image(list_videos_path,video_out):
    
    video_clips = [VideoFileClip(path) for path in list_videos_path]
    opacities = [0.5 for i in range(len(list_videos_path))]  # Opacity values for each video
    overlayed_clips = []

    for clip, opacity in zip(video_clips, opacities):
        overlayed_clip = clip.copy().set_opacity(opacity)
        overlayed_clips.append(overlayed_clip)

    final_clip = CompositeVideoClip(overlayed_clips)
    final_clip.write_videofile(video_out, codec="libx264")
    for clip in video_clips:
        clip.close()
