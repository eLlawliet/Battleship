from random import randint


class Ship:

	def __init__(self, Game):
		self.config = Game.config
		self.setup_location()
		# print(self.location)


	def setup_location(self):
		x = randint(0, self.config.row-1) # 0-4
		y = randint(0, self.config.column-1)
		self.location = (x,y)