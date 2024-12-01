import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3 as sq
import tkinter.messagebox as ms
import random


root = tk.Tk()
root.geometry ("800x500+400+300")
root.resizable (False, False)


image_game = Image.open("pngwing.com (4).png")
background_image_game = ImageTk.PhotoImage(image_game)

background_label = tk.Label(image=background_image_game)
background_label.place(relwidth=1, relheight=1)

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    return deck

deck = create_deck()

random.shuffle(deck)  

root.mainloop()
