import os
import tkinter as tk
from tkinter import filedialog, messagebox
from Yt_downloader import download_video, download_audio


def browse_directory():
    directory_path = filedialog.askdirectory()
    entry_location.delete(0, tk.END)
    entry_location.insert(0, directory_path)

def download():
    choice = var.get()
    location = entry_location.get()
    url = entry_url.get()
    video_quality = vid_quality.get()
    audio_quality = aud_quality.get()

    print(f"Downloading {choice} in {audio_quality if choice == 'Audio' else video_quality} quality to {location}")

    try:
        if choice == "Video":
            download_video(url, location, video_quality)
        elif choice == "Audio":
            download_audio(url, location, audio_quality)
    except:
        messagebox.showerror("Error", "Download Failed!")
    else:
        os.startfile(location)


# Create the main window
root = tk.Tk()
root.title("Youtube Downloader")

# Radio button for selecting 'video' or 'audio'
var = tk.StringVar()
var.set("Video")  # Default selection
radio_video = tk.Radiobutton(root, text="Video", variable=var, value="Video")
radio_video.pack(anchor=tk.W)
radio_audio = tk.Radiobutton(root, text="Audio", variable=var, value="Audio")
radio_audio.pack(anchor=tk.W)

# Dropdown for selecting video quality
video_qualities = ["1080p", "720p", "480p", "360p", "240p", "144p"]
vid_quality = tk.StringVar(root)
vid_quality.set("1080p")  # Default quality
label_video_quality = tk.Label(root, text="Video Quality:")
label_video_quality.pack(anchor=tk.W)
video_option_quality = tk.OptionMenu(root, vid_quality, *video_qualities)
video_option_quality.pack(anchor=tk.W)

# Dropdown for selecting audio quality
audio_qualities = ["M4A", "FLAC", "MP4", "MP3", "WAV", "WMA", "AAC"]
aud_quality = tk.StringVar(root)
aud_quality.set("MP4")  # Default quality
label_audio_quality = tk.Label(root, text="Audio Quality:")
label_audio_quality.pack(anchor=tk.W)
audio_option_quality = tk.OptionMenu(root, aud_quality, *audio_qualities)
audio_option_quality.pack(anchor=tk.W)

# Text field for URL
label_url = tk.Label(root, text="URL:")
label_url.pack(anchor=tk.W)
entry_url = tk.Entry(root, width=50)
entry_url.pack(anchor=tk.W, padx=10)

# Text field for download location
label_location = tk.Label(root, text="Download Location:")
label_location.pack(anchor=tk.W)
entry_location = tk.Entry(root, width=50)
# entry_location.insert(0,"C:/Users/kbakh/Downloads")
entry_location.pack(anchor=tk.W, padx=10)
button_browse = tk.Button(root, text="Browse", command=browse_directory)
button_browse.pack(anchor=tk.W, padx=10)

# Button to initiate download
button_download = tk.Button(root, text="Download", command=download)
button_download.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
