import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class Main():
    def __init__(self, root):
        self.root = root
        self.configurate_main_window()

    def configurate_main_window(self):
        self.root.geometry("800x500+500+300")
        self.root.resizable(False, False)

        self.root.title("BLACKJACK")
        self.icon = tk.PhotoImage(file="png-transparent-card-game-blackjack-gambling-face-card-an-autumn-outing-game-gambling-blackjack.png")
        self.root.iconphoto(False, self.icon)

        self.image = Image.open("main_bg.png")
        self.background_image = ImageTk.PhotoImage(self.image)

        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.create_play_widget ()

    def registration_widget (self):
        self.play_button.place_forget()
        
        

    def create_play_widget (self):
    
        self.play_button_style = ttk.Style()
        self.play_button_style.configure ("Play.TButton", 
                                          font="Arial 18 italic",
                                          foreground="#2E8B57",
                                          background="#006400")
        
        self.play_button = ttk.Button (master=self.root, text='Play now', style= "Play.TButton",command = self.registration_widget)
        self.play_button.place (relx=0.5, rely=0.5, anchor='center')



root = tk.Tk()
app = Main(root)
root.mainloop()