# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pafy
import tkinter as tk
from tkinter import filedialog

test_url = "https://www.youtube.com/watch?v=8myCGlhkrJg"

pafy_obj = pafy.new(test_url)
audio_Stream = pafy_obj.getbestaudio(preftype="m4a")

root = tk.Tk()
root.withdraw()

filePath = filedialog.asksaveasfilename()
print(filePath)
audio_Stream.download(filePath)