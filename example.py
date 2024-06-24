from vseocr import save_subtitles_to_file

if __name__ == '__main__':
    save_subtitles_to_file(
        video_path='C7ez-29RMxU.mp4',
        file_path='example.srt',
        lang='en',
        sim_threshold=80,
        conf_threshold=50,
        use_fullframe=True,
        brightness_threshold=210,
        similar_image_threshold=1000,
        frames_to_skip=25
    )