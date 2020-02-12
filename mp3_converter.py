# coding: utf8
import os
import subprocess
from modules.pymediainfo.pymediainfo import MediaInfo
import tkinter as tk
from tkinter import filedialog

ASK_DLL_LOCATION = False


def ask_directory(window_title):
    """
    Display the file explorer, and ask user to select a folder to process
    """
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory(title=window_title)


def ask_file(window_title):
    """
    Display the file explorer, and ask user to select a file
    """
    root = tk.Tk()
    root.withdraw()
    media_info_path = os.path.join(os.path.realpath(__file__))
    if ASK_DLL_LOCATION:
        return filedialog.askopenfile(title=window_title).name
    else:
        return os.path.join(os.path.dirname(__file__), 'modules', 'pymediainfo', 'pymediainfo', 'MediaInfo.dll')


def list_files_to_convert():
    """
    Generate a hot file list (with its path)
    Get all files with a bit_rate information, which confirm that it is a
    yield return a result and forget it (less memory eating)
    """
    for root, dirs, files in os.walk(video_dir):
        file_list = [name for name in files if not name.endswith('.mp3')]
        for name in file_list:
            filepath = os.path.join(root, name)
            media_info = MediaInfo.parse(filepath, library_file=dll_path)
            for track in media_info.tracks:
                if 'Audio' in track.track_type:
                    # print(track.track_type, track.bit_rate)
                    # print(filepath, "Is an Audio/Video file, and should be converted")
                    yield dict(path=filepath, info=media_info)


# Path where the MediaInfo.dll is located
dll_path = ask_file("Select the MediaInfo.dll location")
# Path where the videos are located
video_dir = ask_directory("Select your music folder to be processed recursively")

# A generator object to be read one time
my_list = list_files_to_convert()
# Then convert
for file in my_list:
    path = file['path']
    info = file['info']
    if os.path.exists(path):
        file_dir = info.tracks[0].folder_name
        filename = info.tracks[0].file_name
        mp3_file_dir = os.path.join(file_dir, 'mp3')
        mp3_file_name = os.path.splitext(filename)[0] + '.mp3'
        if not os.path.exists(mp3_file_dir):
            os.mkdir(mp3_file_dir)
        mp3_converted_filepath = os.path.join(mp3_file_dir, mp3_file_name)
        if not os.path.isfile(mp3_converted_filepath):
            try:
                # Subprocess the conversion with ffmpeg, don't overwrite if exists with '-n' argument
                subprocess.check_call(['ffmpeg', '-i', path, '-vcodec', 'copy', '-codec:a', 'libmp3lame', mp3_converted_filepath, '-n'])
            except subprocess.CalledProcessError as e:
                print("ERROR: ", e.output)
        else:
            print("[INFO] The file {} already exists".format(mp3_converted_filepath))

