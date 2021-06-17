import tkinter as tk
import sys

from config import Config
from game_stat import Game_Stat
from ship import Ship
from player import Player
from board import Board
from loginPage import LoginPage

class Window(tk.Tk):

	def __init__(self, Game):
		self.game = Game # battleship
		self.config = Game.config

		super().__init__()
		self.title(self.config.title)
		self.geometry(self.config.screen)

		self.create_container()

		self.pages = {}
		self.create_board()
		self.create_loginPage()


	def create_container(self):
		self.container = tk.Frame(self, bg="white")
		self.container.pack(fill="both", expand=True)

	def create_loginPage(self):
		self.pages['loginPage'] = LoginPage(self.container, self)	

	def create_board(self):
		self.pages["board"] = Board(self.container, self.game)

	def change_page(self, page):
		page = self.pages[page]
		page.tkraise()	

	def auth_login(self):
		username = self.pages['loginPage'].var_username.get()
		password = self.pages['loginPage'].var_password.get()

		granted = self.config.login(username, password)
		if granted:
			self.change_page('board')
		else:
			showinfo("Window", "Failed login")
			self.clear_text()


class Battleship:

	def __init__(self):
		self.config = Config()
		self.game_stat = Game_Stat()
		self.ship = Ship(self)
		self.player = Player()
		self.window = Window(self)

	def check_location(self):
		ship = self.ship.location
		player = self.player.location
		if ship == player:
			return True
		return False

	def window_button_clicked(self, pos_x, pos_y):
		#print(pos_x, pos_y)
		self.player.current_location(pos_x, pos_y)
		win = self.check_location()
		self.window.pages['board'].change_image_btn(pos_x, pos_y, win)
		if win:
			print("You Win")
			#self.window.destroy()
			sys.exit()
		

	def run(self):
		self.window.mainloop()


if __name__ == '__main__':
	my_battleship = Battleship()
	my_battleship.run()