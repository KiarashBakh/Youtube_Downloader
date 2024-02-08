from pytube import YouTube

def download_video(url:str, save_path:str, resolution:str) -> bool:
    """
    url: audio url
    save_path: download path
    """
    youtube = YouTube(url)
    video = youtube.streams.get_by_resolution(resolution)
    try:
        video.download(save_path)
    except:
        return False

    return True

def download_audio(url:str, save_path:str, subtype:str = None):
    """
    url: audio url
    save_path: download path
    """
    youtube = YouTube(url)
    audio = youtube.streams.get_audio_only(subtype=subtype)
    try:
        audio.download(save_path)
    except:
        return False

    return True

def main():
    file_url = "https://youtu.be/5kGpohEpuTE?si=7C7TDQFSKOVbq07z"
    download_path = "Downloads"
    download_audio(file_url, download_path)
    print("done")

if __name__ == main:
    main()
