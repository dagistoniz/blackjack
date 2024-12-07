import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3 as sq
import tkinter.messagebox as ms
import time
import random
import os

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
                cur.execute("""UPDATE players_database SET score = 1000 WHERE name LIKE ?""", (players_name,))
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
                                          background="#4e2c26")

        self.prepare_label = ttk.Label (text=f"Welcome to oop final project {self.players_name},\nwhich was created by Artem. \nYour balance will be 1000 coins. \nEnjoy your game", style= "Prepare.TLabel")
        self.prepare_label.place (relx=0.10, rely=0.3)

        self.prepare_label_style_v2 = ttk.Style ()
        self.prepare_label_style_v2.configure ("Prepare2.TLabel",
                                          font="Arial 14",
                                          foreground="#FAEBD7",
                                          background="#8f6544")

        self.proceed_to_game_button = ttk.Button (text="Preess to proceed the game", style="Prepare2.TLabel",command= self.proceed_to_game)
        self.proceed_to_game_button.place (relx=0.10, rely=0.55)


    def proceed_to_game (self):
        for widget in root.winfo_children():

            widget.destroy()
        # self.proceed_to_game_button.place_forget()
        # self.prepare_label.place_forget()
        self.image_game = Image.open("pngwing.com (4).png")
        self.background_image_game = ImageTk.PhotoImage(self.image_game)
        self.background_label = tk.Label(self.root, image=self.background_image_game)
        self.background_label.place(relwidth=1, relheight=1)

        # self.background_label.configure (image=self.background_image_game)
        # with sq.connect ("game_data") as con:
        #     cur = con.cursor ()
        #     cur.execute ("""CREATE TABLE IF NOT EXISTS game_data (
        #                  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        #                  score INTEGER DEFAULT 1000
        #     )""")
        #     cur.execute ("""INSERT INTO game_data""")
        # with sq.connect ("game_data") as con:
        #     cur = con.cursor ()
        #     cur.execute ("""SELECT * FROM game_data""")
        #     game_data = cur.fetchall ()

        # with sq.connect ("players_database") as con:
        #     cur = con.cursor ()
        #     cur.execute ("""ALTER TABLE players_database ADD COLUMN score INTEGER;""")

        with sq.connect ("players_database") as con:
            cur = con.cursor ()
            cur.execute ("""SELECT score FROM players_database WHERE name LIKE ?""", (self.players_name,))
            data = cur.fetchall ()
        
        self.temp_balance = float (data[0][0])
        print (self.temp_balance)

        self.balance = tk.StringVar (value=self.temp_balance)

        self.balance_label = tk.Label (font =("Arial 16"),foreground="#FAEBD7",background="#0A3D18",textvariable=self.balance)
        self.balance_label.place (relx=0.1, rely=0.9)

        self.text = tk.Label (text="Your balance", foreground="#FAEBD7",font=("Arial 14"), background="#0A3D18")
        self.text.place (relx=0.1, rely=0.85)

        self.style_start_label = ttk.Style ()
        self.style_start_label.configure ("Start.TLabel",
                                          font = "Arial 14 italic",
                                          foreground = "#ffebae",
                                          background = "#006400")


        self.strart_label = ttk.Label (style="Start.TLabel",text="For strat game entry your bet \nand press on card")
        self.strart_label.place (relx=0.5 ,rely=0.4,anchor='center')

        self.entry_bet = tk.Entry (master=root, font=("Arial 14 bold"))
        self.entry_bet.place (relx=0.5, rely=0.57, anchor='center')

        self.image_card= Image.open("1_2420-64x64.png")
        self.image_cards = ImageTk.PhotoImage(self.image_card)


        self.cards = tk.Button (image = self.image_cards, command=self.create_desk)
        self.cards.place (relx=0.17, rely=0.34)

    def create_desk(self):
        flag = True
        self.value_bet=self.entry_bet.get()
        if not self.value_bet:
            ms.showinfo (title="Rules", message="Entry your bet")
            flag = False
        try:
            if int(self.value_bet) > self.temp_balance:
                ms.showinfo (title="Rules", message= "Bet exceed balance")
                flag = False
        except ValueError:
            pass
        if flag:
            self.strart_label.place_forget ()
            self.cards.place_forget()
            self.entry_bet.place_forget()

            # time.sleep(0.5)
            bet = tk.StringVar (value=self.value_bet)
            self.bet_label = tk.Label (textvariable=bet)
            self.bet_label.place (relx=0.3, rely=0.3)
            self.temp_balance = float (self.temp_balance)-float (self.value_bet)
            self.balance.set (self.temp_balance)

            with sq.connect ("players_database") as con:
                cur = con.cursor ()
                cur.execute ("""UPDATE players_database
                             SET score = ?
                             WHERE name = ?""", (self.temp_balance, self.players_name))

            self.get_players_hand ()
            self.players_score = tk.Label (root, text=self.count_player_hand)
            self.players_score.place (relx=0.37, rely=0.58)
            self.get_dealer_hand ()
            self.dealer_score = tk.Label (root, text=self.count_hand_dealer(self.dealer_hand)[0])
            self.dealer_score.place (relx=0.37, rely=0.18)
            self.get_game_widget ()

    def create_deck(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        deck = [f'{rank} of {suit}' for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def count_hand_player (self, hand):
        result = 0
        for i in range (len(hand)):
            card_rank = hand[i].split()[0]
            if card_rank in ["Jack", "Queen", "King", "Ace"]:
                result += 10
                continue
            result += int (card_rank)
        return result

    def count_hand_dealer (self, hand):
        result = 0
        result_for_show = 0
        for i in range (len(hand)):
            if i == 1:
                result_for_show = result
            card_rank = hand[i].split()[0]
            if card_rank in ["Jack", "Queen", "King", "Ace"]:
                result += 10
                continue
            result += int (card_rank)

        return result_for_show , result

    def get_players_hand(self):
        self.main_deck = self.create_deck()
        self.player_hand = []
        for i in range (2):
            self.player_hand.append (self.main_deck.pop())
        self.count_player_hand = self.count_hand_player (self.player_hand)
        print  (self.player_hand)
        print (self.count_player_hand)

        temp_image = []
        for i in range (len (self.player_hand)):
            temp = self.convert_to_png (self.player_hand[i])
            temp_image.append (temp)
        print (temp_image)
        path = os.getcwd()
        temp_image[0] = path + "\\" + "cards_zip" + "\\" + str (temp_image[0])
        temp_image[1] = path + "\\" + "cards_zip" + "\\" + temp_image[1]
        self.image_first_card= Image.open(temp_image[0])
        self.image_second_card= Image.open(temp_image[1])
        self.image_first_cards = ImageTk.PhotoImage(self.image_first_card)
        self.image_second_card = ImageTk.PhotoImage(self.image_second_card)
        self.first_card_label = tk.Label (image=self.image_first_cards)
        self.second_card_label = tk.Label (image = self.image_second_card)
        # .place (relx=0.40, rely=0.58)
        # place (relx=0.5, rely=0.58)
        self.first_card_label.place(relx=0.35, rely=0.58)
        self.second_card_label.place(relx=0.35, rely=0.58)
        self.animate_cards()

        #temp
    def animate_cards(self):

        first_card_x = self.first_card_label.winfo_x()
        second_card_x = self.second_card_label.winfo_x()

        if first_card_x < self.root.winfo_width() * 0.40:
            self.first_card_label.place(relx=(first_card_x + 15) / self.root.winfo_width(), rely=0.58)

        if second_card_x < self.root.winfo_width() * 0.50:
            self.second_card_label.place(relx=(second_card_x + 20) / self.root.winfo_width(), rely=0.58)


        if first_card_x < self.root.winfo_width() * 0.40 or second_card_x < self.root.winfo_width() * 0.50:
            self.root.after(50, self.animate_cards)

    def get_dealer_hand(self):
        # time.sleep(0.5)
        self.dealer_hand = []
        for i in range (2):
            self.dealer_hand.append (self.main_deck.pop())
        self.count_dealer_hand = self.count_hand_dealer (self.dealer_hand)
        print (self.dealer_hand)
        print (self.count_dealer_hand)
        temp_image_dealer = []
        for i in range (len (self.dealer_hand)):
            temp = self.convert_to_png (self.dealer_hand[i])
            temp_image_dealer.append (temp)
        print (temp_image_dealer)
        path = os.getcwd()
        temp_image_dealer[0] = path + "\\" + "cards_zip" + "\\" + str (temp_image_dealer[0])
        self.future = path + "\\" + "cards_zip" + "\\" + str (temp_image_dealer[1])
        temp_image_dealer[1] = path + "\\" + "cards_zip" + "\\" + "Reverse.png"
        self.image_first_card_v2 = Image.open(temp_image_dealer[0])
        self.image_second_card_v2= Image.open(temp_image_dealer[1])
        self.future = Image.open(self.future)
        self.image_first_cards_v2 = ImageTk.PhotoImage(self.image_first_card_v2)
        self.image_second_card_v2 = ImageTk.PhotoImage(self.image_second_card_v2)
        self.future = ImageTk.PhotoImage(self.future)
        self.first_card_label_v2 = tk.Label(root, image=self.image_first_cards_v2)
        self.second_card_label_v2 = tk.Label(root, image=self.image_second_card_v2)
        self.first_card_label_v2.place(relx=-0.1, rely=0.18)
        self.second_card_label_v2.place(relx=1.1, rely=0.18)
        self.animate_cards_v2()

    def animate_cards_v2(self):

        first_card_v2_x = self.first_card_label_v2.winfo_x()
        second_card_v2_x = self.second_card_label_v2.winfo_x()


        if first_card_v2_x < self.root.winfo_width() * 0.40:
            self.first_card_label_v2.place(relx=(first_card_v2_x + 20) / self.root.winfo_width(), rely=0.18)

        if second_card_v2_x > self.root.winfo_width() * 0.50:
            self.second_card_label_v2.place(relx=(second_card_v2_x - 25) / self.root.winfo_width(), rely=0.18)


        if first_card_v2_x < self.root.winfo_width() * 0.40 or second_card_v2_x > self.root.winfo_width() * 0.50:
            self.root.after(50, self.animate_cards_v2)


    def convert_to_png (self, card):
        card = card.split()
        return card[0].lower() + "_" + card[1] + "_" + card[2].lower() + ".png"

    def add_card (self):
        # time.sleep(0.5)
        if len(self.player_hand) < 5:
            if len(self.player_hand) ==2:
                self.player_hand.append(self.main_deck.pop())
                new_count = self.count_hand_player(self.player_hand)

                temp = self.convert_to_png (self.player_hand[2])
                path = os.getcwd()
                temp = path + "\\" + "cards_zip" + "\\" + str (temp)
                self.image_new_card= Image.open(temp)
                self.image_new_card = ImageTk.PhotoImage(self.image_new_card)
                self.new_card_label = tk.Label (image=self.image_new_card).place (relx=0.60, rely=0.58)
                self.players_score.configure (text=new_count)
                if new_count > 21:

                    ms.showinfo (title="Rules", message="You are exceed limit")
                    

                    with sq.connect ("players_database") as con:
                        cur = con.cursor ()
                        cur.execute ("""UPDATE players_database
                                     SET score = ?
                                     WHERE name = ?""",(self.temp_balance, self.players_name))
                    self.proceed_to_game()
            elif len(self.player_hand) == 3:

                self.player_hand.append(self.main_deck.pop())
                new_count = self.count_hand_player(self.player_hand)
                temp_v2 = self.convert_to_png (self.player_hand[3])
                path = os.getcwd()
                temp_v2 = path + "\\" + "cards_zip" + "\\" + str (temp_v2)
                self.image_new_card_v4 = Image.open(temp_v2)
                self.image_new_card_v4 = ImageTk.PhotoImage(self.image_new_card_v4)
                self.new_card_label_v4 = tk.Label (image=self.image_new_card_v4).place (relx=0.7, rely=0.58)
                self.players_score.configure (text=new_count)
                if new_count > 21:
                    ms.showinfo (title="Rules", message="You are exceed limit")

                    with sq.connect ("players_database") as con:
                        cur = con.cursor ()
                        cur.execute ("""UPDATE players_database
                                     SET score = ?
                                     WHERE name = ?""",(self.temp_balance, self.players_name))
                    self.proceed_to_game()

    def add_card_dealer(self):

        if len(self.dealer_hand) < 5:
            if len(self.dealer_hand) ==2:
                self.dealer_hand.append(self.main_deck.pop())
                new_count = self.count_hand_dealer(self.dealer_hand)

                temp = self.convert_to_png (self.dealer_hand[2])
                path = os.getcwd()
                temp = path + "\\" + "cards_zip" + "\\" + str (temp)
                self.image_new_card_dealer = Image.open(temp)
                self.image_new_card_dealer = ImageTk.PhotoImage(self.image_new_card_dealer)
                self.new_card_label_dealer = tk.Label (image=self.image_new_card_dealer).place (relx=0.60, rely=0.18)
                self.dealer_score.configure (text=self.count_hand_dealer(self.dealer_hand)[1])
            
                if new_count[1] > 21:

                    ms.showinfo (title="Rules", message="Dealer is exceed the limit")
                    self.temp_balance = float(self.temp_balance) + float(self.value_bet) * 2
                    self.balance.set(self.temp_balance)
                    with sq.connect ("players_database") as con:
                        cur = con.cursor ()
                        cur.execute ("""UPDATE players_database
                                     SET score = ?
                                     WHERE name = ?""",(self.temp_balance, self.players_name))
                    self.proceed_to_game()

            elif len(self.dealer_hand) == 3:

                self.dealer_hand.append(self.main_deck.pop())
                new_count = self.count_hand_dealer(self.dealer_hand)
                temp_v2 = self.convert_to_png (self.dealer_hand[3])
                path = os.getcwd()
                temp_v2 = path + "\\" + "cards_zip" + "\\" + str (temp_v2)
                self.image_new_card_dealer_v2 = Image.open(temp_v2)
                self.image_new_card_dealer_v2 = ImageTk.PhotoImage(self.image_new_card_dealer_v2)
                self.image_new_card_dealer_v2 = tk.Label (image=self.image_new_card_dealer_v2).place (relx=0.7, rely=0.18)
                self.dealer_score.configure (text=self.count_hand_dealer(self.dealer_hand)[1])
            
                if new_count[1] > 21:
                    ms.showinfo (title="Rules", message="You are exceed limit")
                    self.temp_balance = float(self.temp_balance) + float(self.value_bet) * 2
                    self.balance.set(self.temp_balance)
                    
                    with sq.connect ("players_database") as con:
                        cur = con.cursor ()
                        cur.execute ("""UPDATE players_database
                                     SET score = ?
                                     WHERE name = ?""",(self.temp_balance, self.players_name))
                    self.proceed_to_game()

    def get_result (self):

        try:
            self.dealer_score.configure (text=self.count_hand_dealer(self.dealer_hand)[1])
            if 21-self.count_hand_player(self.player_hand) < 21 - self.count_hand_dealer(self.dealer_hand)[1]:
                ms.showinfo (title="Reules", message="Player win!")
                self.temp_balance = float (self.temp_balance)+float (self.value_bet) * 2
                self.balance.set (self.temp_balance)
                
                with sq.connect ("players_database") as con:
                    cur = con.cursor ()
                    cur.execute ("""UPDATE players_database
                                 SET score = ?
                                 WHERE name = ?""",(self.temp_balance, self.players_name))
            elif 21-self.count_hand_player(self.player_hand) == 21 - self.count_hand_dealer(self.dealer_hand)[1]:
                ms.showinfo (title="Reules", message="Draw!")
                self.temp_balance = float (self.temp_balance)+float (self.value_bet)
                self.balance.set (self.temp_balance)
                with sq.connect ("players_database") as con:
                    cur = con.cursor ()
                    cur.execute ("""UPDATE players_database
                                 SET score = ?
                                 WHERE name = ?""",(self.temp_balance, self.players_name))
            else:
                ms.showinfo (title="Reules",message="Dealer win!")
                with sq.connect ("players_database") as con:
                    cur = con.cursor ()
                    cur.execute ("""UPDATE players_database
                                 SET score = ?
                                 WHERE name = ?""",(self.temp_balance, self.players_name))
            self.proceed_to_game()
        except Exception:
            pass

        # elif 21-self.count_hand_player(self.player_hand) == 21 - self.count_hand_dealer(self.dealer_hand)[1]:
        #     ms.showinfo (title="Reules", message="Draw!")
        #     self.temp_balance = float (self.temp_balance)+float (self.value_bet)
        #     self.balance.set (self.temp_balance)
        #     with sq.connect ("game_data") as con:
        #         cur = con.cursor ()
        #         cur.execute ("""UPDATE game_data
        #                      SET score = ?
        #                      WHERE user_id = ?""",(self.temp_balance, 1))
        # else:
        #     ms.showinfo (title="Reules",message="Dealer win!")
        #     with sq.connect ("game_data") as con:
        #         cur = con.cursor ()
        #         cur.execute ("""UPDATE game_data
        #                      SET score = ?
        #                      WHERE user_id = ?""",(self.temp_balance, 1))
        # self.proceed_to_game()

    def stop_take (self):
        self.second_card_label_v2.configure (image=self.future)
        if (self.count_hand_dealer(self.dealer_hand)[1]) < 17:
            self.add_card_dealer()

        self.get_result()

    def get_game_widget (self):
        add_card_bt = tk.Button (text="Take one more card", command = self.add_card)
        add_card_bt.place (relx=0.5, rely=0.5)

        add_stop_bt = tk.Button (text="Enough card", command=self.stop_take)
        add_stop_bt.place (relx=0.35, rely=0.5)

root = tk.Tk()
app = Main(root)
root.mainloop()
