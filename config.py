
class Config:

	def __init__(self):

		#GAME CONFIG
		self.title = "Battleship War"
		self.row = 5
		self.column = 5


		#WINDOW CONFIG
		base = 200
		ratio = 5
		self.side = base * ratio
		self.screen = f"{self.side}x{self.side}+500+500"

		#IMG PATH
		self.init_img = "img/init_img.png"
		self.final_img = "img/final_img.png"
		self.win_img = "img/win_img.png"

	def login(self, username, password):
		if username == "username" and password == "password":
			return True
		else:
			return False