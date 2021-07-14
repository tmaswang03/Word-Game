import random
import time
from tkinter import *
import math
from PIL import ImageTk, Image
import base64
import urllib
import urllib.request
import os
from main import player
from main import generateLetters
from time import strftime

window = Tk()
window.resizable(0, 0)
window.config(padx=10, pady=10, bg="SlateGray1")

LIVES_URL = ["https://i.ibb.co/RHw4WG2/die.png", "https://i.ibb.co/gwCDRrM/oneHeart.png", "https://i.ibb.co/Btc25cf/two-Hearts.png",\
             "https://i.ibb.co/sFb9wx3/three-Hearts.png"] # Order of lives: 0, 1, 2, 3
LIVES_PNG = ["die.png", "oneHeart.png", "twoHearts.png", "threeHearts.png"]
ICONS_URL = ["https://i.ibb.co/NtdyHdm/OinkOink.png", "https://i.ibb.co/fD03XyB/MooMoo.png", "https://i.ibb.co/gvY7h9L/BeeIcon.png", \
             "https://i.ibb.co/3fsJqjN/BakBak.png", "https://i.ibb.co/2sSQ1bS/BarkBark.png"]
ICONS_PNG = ["pig.png", "cow.png", "bee.png", "chicken.png", "dog.png"]

tmp = player("Thomas")
endTime = time.time() + tmp.inc

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
    img2 = img1.resize((150, 150))
    img3 = ImageTk.PhotoImage(img2)
    return img3

def submitWord(*args):
    char = letterLabel['text']
    word = inputBox.get()
    inputBox.delete(0, END)
    if(tmp.wordExist(char, word) == False):
        return
    global endTime
    endTime = time.time() + tmp.inc
    tmp.useWord(word)
    nxt = generateLetters()
    while(nxt == letterLabel['text']):
        nxt = generateLetters()
    letterLabel.config(text = nxt.lower())
    scoreLabel.config(text = tmp.score)

def timer():
    global endTime
    timeLabel.config(text = str(round(endTime - time.time(), 2)) + " s")
    if(endTime <= time.time()):
        endTime = time.time() + tmp.inc
        tmp.lives-=1
        if (tmp.lives <= 0):
            endGame()
        nxt = generateLetters()
        while (nxt == letterLabel['text']):
            nxt = generateLetters()
        letterLabel.config(text = nxt.lower())
        print(tmp.lives)
        newLives = displayLives(tmp.lives)
        livesLabel.config(image=newLives)
        livesLabel.image = newLives

    timeLabel.after(50, timer)

def endGame():
    timeLabel.config(text='0 s')

    

# ========================================================== GUI INTERFACE ==========================================================


titleLabel = Label(window, width=10, text="Wurd Game", font="Courier 45 bold", bg="seashell")
img = displayLives(3)
livesLabel = Label(window, width=180, image=img, bg="SlateGray1", anchor="center", height = 30)
img2 = displayIcons()
iconLabel = Label(window, width=150, height=150, image=img2, bg="SlateGray1", anchor="center")
letterLabel = Label(window, width=5, height=2, text=generateLetters(), borderwidth=2, relief='ridge', font = "Courier 30 bold", bg="SlateGray2")
scoreLabel = Label(window, width=10, text=0, font = "Courier 20 bold", bg="SlateGray2")
scoreLabel2 = Label(window, width=10, text="Score", font = "Courier 20 underline", bg="SlateGray2")
inputBox = Entry(window, width=21, text="input your text here", justify='center', font="Courier 20")
timeLabel = Label(window, width=10, text=0, font="Courier 20 bold", bg="SlateGray2")
timeLabel2 = Label(window, width=10, text="Timer", font="Courier 20 underline", bg="SlateGray2")
restartButton = Button(window, width=11, text='Restart', font='Courier 19 bold', justify="center", bg="SlateGray2")
exitButton = Button(window, width=11, text="Exit", font="Courier 19 bold", justify="center", bg="SlateGray2", command=lambda:window.destroy())

inputBox.bind('<Return>', submitWord)

titleLabel.grid(row=1, column=1, columnspan=2, pady=(0, 10))
livesLabel.grid(row=2, column=1, columnspan=2)
iconLabel.grid(row=3, column=1, columnspan=2, pady=(0, 10))
letterLabel.grid(row=4, column=1, columnspan=2, pady=(0, 10))
inputBox.grid(row=5, column=1, columnspan=2, pady=(0, 10))
scoreLabel2.grid(row=6, column=1, pady=(0, 10))
timeLabel2.grid(row=6, column=2, pady=(0, 10))
scoreLabel.grid(row=7, column=1, pady=(0, 10))
timeLabel.grid(row=7, column=2, pady=(0, 10))
restartButton.grid(row=8, column=1, padx=(0, 0))
exitButton.grid(row=8, column=2)

timer()

window.mainloop()
