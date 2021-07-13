import random
import time
from tkinter import *
import math
from PIL import ImageTk, Image
import base64
import urllib
import urllib.request
import os

window = Tk()
window.resizable(0, 0)
window.config(padx=10, pady=10, bg="SlateGray1")

LIVES_URL = ["https://i.ibb.co/RHw4WG2/die.png", "https://i.ibb.co/gwCDRrM/oneHeart.png", "https://i.ibb.co/Btc25cf/two-Hearts.png",\
             "https://i.ibb.co/sFb9wx3/three-Hearts.png"] # Order of lives: 0, 1, 2, 3
LIVES_PNG = ["die.png", "oneHeart.png", "twoHearts.png", "threeHearts.png"]
ICONS_URL = ["https://i.ibb.co/pPRbw8q/OinkOink.png", "https://i.ibb.co/ggg6g8C/MooMoo.png", "https://i.ibb.co/K0H5J3H/BeeIcon.png", \
             "https://i.ibb.co/tHMckNz/BakBak.png", "https://i.ibb.co/G5hkRNz/chicken.png"]
ICONS_PNG = ["pig.png", "cow.png", "bee.png", "chicken.png", "dog.png"]

# ============================================================= METHODS =============================================================

def requestURLs():
    for idx in range(0, 4):
        urllib.request.urlretrieve(LIVES_URL[idx], LIVES_PNG[idx])
    for idx in range(0, 5):
        urllib.request.urlretrieve(ICONS_URL[idx], ICONS_PNG[idx])
requestURLs()

def displayLives(lives):
    img = Image.open(LIVES_PNG[lives])
    img1 = img.resize((120, 30))
    img2 = ImageTk.PhotoImage(img1)
    return img2

def displayIcons():
    idx1 = random.randint(0, 4)
    idx1 = 3
    img1 = Image.open(ICONS_PNG[idx1])
    img2 = img1.resize((180, 180))
    img3 = ImageTk.PhotoImage(img2)
    return img3

# ========================================================== GUI INTERFACE ==========================================================

titleLabel = Label(window, width=10, text="Wurd Game", font="Courier 80 bold", bg="seashell")
img = displayLives(3)
livesLabel = Label(window, width=180, image=img, bg="SlateGray1", anchor="center", height = 30)
img2 = displayIcons()
iconLabel = Label(window, width=180, height = 0, image=img2, bg="SlateGray2", anchor="center")

titleLabel.grid(row=1, column=1, padx=(0, 10), pady=(0, 10))
livesLabel.grid(row=4, column=1, padx=(0, 10), pady=(0, 10))
iconLabel.grid(row=5, column=1, padx=(0, 10), pady=(0, 10))





window.mainloop()

"A prompt will appear on your screen. \
Think of a word with those letters (consecutively) in them and \ntype it in the text box on your side of the screen before \
the timer runs out! Each player gets three lives. \n Win by being the only player remaining or by using all the letters\
on the left. Have fun!"

