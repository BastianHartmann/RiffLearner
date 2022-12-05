# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 14:03:55 2022

@author: Bastian Hartmann
"""

#! python3

#%matplotlib notebook

import librosa as lr
import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import librosa.display
import sounddevice as sd
import time

root = tk.Tk()
root.withdraw()

filePath = filedialog.askopenfilename()

AudioLoad, SampleRate = lr.load(filePath,sr=None,mono=True)

# Displaying of audio track
#WavePlot = librosa.display.waveshow(AudioLoad[0:SampleRate*60],sr=SampleRate)


# Other way of displaying the track
xPlot = np.linspace(0,len(AudioLoad),len(AudioLoad)+1)
xPlotTime = xPlot / SampleRate
Seconds = 60
SoundFig, SoundAx = plt.subplots()
SoundAx.plot(xPlotTime[0:int(SampleRate*Seconds)],AudioLoad[0:int(SampleRate*Seconds)])
SoundAx.set_xlabel("Time [s]")
SoundAx.set_ylabel("Normalized Audio Signal")
SoundAx.set_ylim((-1.2,1.2))


# Add time markers at 10,30 and 50 seconds with annotation
MarkerPos = np.array([10,30,50])
for i in MarkerPos:
    SoundAx.axvline(i,c='orange',label=i)
    annText = "Time : %d s "%i
    SoundAx.text(i,1.17,annText,color='orange',ha='right',va='top', rotation=90, fontweight='bold', fontsize=8)


# Playing of audio track (first 10 seconds)

TimeStart = 0
TimeEnd = 30
sd.play(AudioLoad[int(SampleRate*TimeStart):SampleRate*TimeEnd],samplerate=SampleRate)

# And draw a time indicator updated every second
StartTime = time.time()
interval = 1
PlayBar = SoundAx.axvline(TimeStart,color='red')

for i in range(TimeStart+1,TimeEnd+1):
    time.sleep(StartTime + i*interval - time.time())
    SoundAx.lines[-1].remove()
    SoundAx.axvline(i,color='red')
#     PlayBar.set_xdata(i)
    plt.gcf().canvas.draw()
    plt.gcf().canvas.flush_events()
#     #display(SoundFig)
#     #clear_output(wait = True)
    print(i,' s')
#     plt.pause(1)

plt.show()

# interval = 1
# PlayBar = SoundAx.axvline(TimeStart,color='red')
# def updatePlayBar(pos):
#     PlayBar.set_xdata(pos)
#     return PlayBar


# PlayAnimation = animation.FuncAnimation(SoundFig,updatePlayBar,frames = range(TimeStart+1,TimeEnd+1), interval=1)
# PlayBar = SoundAx.axvline(TimeStart,color='red')
#plt.show()