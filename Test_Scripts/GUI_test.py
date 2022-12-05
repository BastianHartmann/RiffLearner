# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 17:03:04 2022

@author: Bastian Hartmann
"""

#! python3

import pafy
from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
#from pygame import mixer
import os
import librosa as lr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import librosa.display
import sounddevice as sd
import time

root = tk.Tk()
root.title('First Try')
root.geometry("920x670+290+85")
root.configure(bg="#0f1a2b")
root.resizable(False, False)

imageIcon = PhotoImage(file="simple-gray-default-button-hi.png") # will be changed later!!!
root.iconphoto(False,imageIcon)

# button
play_button = PhotoImage(file="fancy_play_button.png")
Button(root,image=play_button,bg="#0f1a2b",bd=0).place(x=100,y=400)

root.mainloop()