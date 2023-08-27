import tkinter as tk
from tkinter import filedialog

def get_srt_file():
    file_path = filedialog.askopenfilename(
        title="Select SRT File",
        filetypes=[("SRT Files", "*.srt"), ("Text Files", "*.txt")]
    )
    if file_path:
        return file_path
    else:
        return None

def Saveـpath():
    path = filedialog.askdirectory()
    if path:
        return path
    else:
        return None


