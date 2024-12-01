import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3 as sq
import tkinter.messagebox as ms


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

    def toggle_password_visibility(self):
            if self.conceal_password_var.get():
                self.password_entry.config(show="*") 
            else:
                self.password_entry.config(show="")   


    def registrate_players (self):
        players_name = self.name_entry.get()
        players_password = self.password_entry.get()

        try:
            with sq.connect ("players_database") as con:
             cur = con.cursor()
             cur.execute ("""INSERT INTO players_database (name, password) VALUES (?, ?)""", (players_name, players_password))
        except:
            ms.showerror (title="Error", message="Some error until connection to db")
        else:
            ms.showinfo (title="Succes", message="Create a new players in datebase success")

    def join_player (self):
        self.players_name = self.name_entry.get()
        self.players_password = self.password_entry.get()

        try:
            with sq.connect ("players_database") as con:
                cur = con.cursor ()
                cur.execute ("""SELECT * FROM players_database""")
                self.data=cur.fetchall ()
        except:
            ms.showerror (title="Error", message="Some error until connection to db")
        else:
            name_data = []
            password_data = []
            for i in range (len(self.data)):
                name_data.append (self.data[i][0])
                password_data.append (self.data[i][1])

        if self.players_name in name_data and int (self.players_password) in password_data:
            self.proceed_to_prepare()
        else:
            ms.showwarning (title = "Error", message="Undefined players")
    def registration_widget (self):
        self.play_button.place_forget()
        
        self.name_label = tk.Label (text="Insert your name", font = "Arial 16 italic", background="#98FB98")
        self.name_label.place (relx=0.5, rely=0.35, anchor='center')

        self.name_entry = tk.Entry (background="#FFFAFA", font = "Arial 14", justify ="left")
        self.name_entry.place (relx=0.5, rely=0.4, anchor='center')
        
        self.password_name = tk.Label (text="Insert your password", font = "Arial 16 italic", background="#98FB98")
        self.password_name.place (relx=0.5, rely=0.55, anchor='center')

        self.conceal_password_var = tk.BooleanVar(value=False)  

        self.password_entry = tk.Entry (background="#FFFAFA", font = "Arial 14", justify ="left")
        self.password_entry.place (relx= 0.5, rely=0.6, anchor='center')

        self.conceal_password = ttk.Checkbutton (text="Conceal password", variable=self.conceal_password_var, command=self.toggle_password_visibility)
        self.conceal_password.place (relx=0.65, rely=0.575)

        self.registration_button_style = ttk.Style()
        self.registration_button_style.configure ("Registration.TButton", 
                                          font="Arial 14 italic",
                                          foreground="#2E8B57",
                                          background="#006400")


        self.join_button = ttk.Button (text="Join", style="Registration.TButton", command=self.join_player)
        self.join_button.place (relx=0.4, rely=0.7, anchor='center')

        self.registration_button = ttk.Button (text="Registration", style="Registration.TButton", command=self.registrate_players)
        self.registration_button.place (relx=0.6, rely=0.7, anchor='center')

    def create_db(self):
         with sq.connect ("players_database") as con:
              cur = con.cursor()
              cur.execute ("""CREATE TABLE IF NOT EXISTS players_database (
                           name TEXT,
                           password INTEGER
              )""")

    def create_play_widget (self):
    
        self.play_button_style = ttk.Style()
        self.play_button_style.configure ("Play.TButton", 
                                          font="Arial 18 italic",
                                          foreground="#2E8B57",
                                          background="#006400")
        
        self.play_button = ttk.Button (master=self.root, text='Play now', style= "Play.TButton",command = self.registration_widget)
        self.play_button.place (relx=0.5, rely=0.5, anchor='center')

        self.create_db()

    def proceed_to_prepare(self):
        self.name_label.place_forget()
        self.name_entry.place_forget()
        self.password_name.place_forget()
        self.password_entry.place_forget()
        self.join_button.place_forget()
        self.registration_button.place_forget()
        self.conceal_password.place_forget()
        

        self.image_prepare = Image.open("prerequisite.jpg")
        self.background_image_prepare = ImageTk.PhotoImage(self.image_prepare)
        self.background_label.configure (image=self.background_image_prepare)

        self.prepare_label_style = ttk.Style ()
        self.prepare_label_style.configure ("Prepare.TLabel", 
                                          font="Arial 14",
                                          foreground="#FAEBD7",
                                          background="#583206")

        self.prepare_label = ttk.Label (text=f"Welcome to oop final project {self.players_name},\nwhich was created by Artem. \nYour balance will be 1000 coins. \nEnjoy your game", style= "Prepare.TLabel")
        self.prepare_label.place (relx=0.10, rely=0.3)

        self.proceed_to_game_button = ttk.Button (text="Proceed to game", command= self.proceed_to_game)
        self.proceed_to_game_button.place (relx=0.10, rely=0.55)


    def proceed_to_game (self):

        self.proceed_to_game_button.place_forget()
        self.prepare_label.place_forget()

        self.image_game = Image.open("pngwing.com (4).png")
        self.background_image_game = ImageTk.PhotoImage(self.image_game)
        self.background_label.configure (image=self.background_image_game)

root = tk.Tk()
app = Main(root)
root.mainloop()