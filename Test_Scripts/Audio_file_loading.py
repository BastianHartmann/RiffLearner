# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 14:03:55 2022

@author: Bastian Hartmann
"""

#! python3

import librosa as lr
import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
import sounddevice as sd
import datetime

root = tk.Tk()
root.withdraw()

filePath = filedialog.askopenfilename()

AudioLoad, SampleRate = lr.load(filePath,sr=None,mono=True)

# Displaying of audio track
WavePlot = librosa.display.waveshow(AudioLoad[0:SampleRate*60],sr=SampleRate)


# Add time marker at 30 seconds
markerTime = 30
ax = plt.gca()



# Playing of audio track (first 10 seconds)
sd.play(AudioLoad[0:SampleRate*10],samplerate=SampleRate)
