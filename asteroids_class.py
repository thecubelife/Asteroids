#asteroids_class.py
#asteroids class

try:
	import tkinter as tk
except ImportError:
	import Tkinter as tk
import time
import math
import random
#this is used to pass arguments to a button command which could not be done otherwise
from functools import partial


class asteroids:

	def draw_asteroid(self, canvas, width, height):
		ranx = self.get_random_x(width)
		rany = self.get_random_y(height)
		self.x = ranx
		self.y = rany
		rans = self.get_random_size()
		#rans = 3
		if rans == 1:
			self.small(width, height, self.x, self.y)
		elif rans == 2:
			self.medium(width, height, self.x, self.y)
		else:
			self.large(width, height, self.x, self.y)

	
	def small(self, width, height, x, y):
		self.size = 3
		center_x =  width / 2
		center_y = height / 2
		r = 10
		self.x0 = x - r
		self.y0 = y - r
		self.x1 = x + r
		self.y1 = y + r


			#quadrant 1		quadrant 2
			#quadrant 3		quadrant 4
		
		if self.x0 <= center_x and self.y0 <= center_y:
			#quadrant 1
			self.dirx = 1 * self.get_random_x(5)
			self.diry = 1 * self.get_random_y(5)
			#move to outside of view within quadrant
		elif self.x0 <= center_x and self.y0 >= center_y:
			#quadrant 3
			self.dirx = 1 * self.get_random_x(5)
			self.diry = -1 * self.get_random_y(5)
			#move to outside of view within quadrant
		elif self.x0 >= center_x and self.y0 <= center_y:
			#quadrant 2
			self.dirx = -1 * self.get_random_x(5)
			self.diry = 1 * self.get_random_y(5)
			#move to outside of view within quadrant
		elif self.x0 >= center_x and self.y0 >= center_y:
			#quadrant 4
			self.dirx = -1 * self.get_random_x(5)
			self.diry = -1 * self.get_random_y(5)
			#move to outside of view within quadrant
			



		self.aster = self.canvas.create_oval(self.x0, self.y0, self.x1, self.y1, outline = "#FFFFFF", tags = 'asteroid')
		

	def medium(self, width, height, x, y):
		self.size = 2
		center_x =  width / 2
		center_y = height / 2
		r = 30
		self.x0 = x - r
		self.y0 = y - r
		self.x1 = x + r
		self.y1 = y + r

			#quadrant 1		quadrant 2
			#quadrant 3		quadrant 4


		if self.x0 <= center_x and self.y0 <= center_y:
			#quadrant 1
			self.dirx = 1 * self.get_random_x(5)
			self.diry = 1 * self.get_random_y(5)
			#move to outside of view within quadrant
		elif self.x0 <= center_x and self.y0 >= center_y:
			#quadrant 3
			self.dirx = 1 * self.get_random_x(5)
			self.diry = -1 * self.get_random_y(5)
			#move to outside of view within quadrant
		elif self.x0 >= center_x and self.y0 <= center_y:
			#quadrant 2
			self.dirx = -1 * self.get_random_x(5)
			self.diry = 1 * self.get_random_y(5)
			#move to outside of view within quadrant
		elif self.x0 >= center_x and self.y0 >= center_y:
			#quadrant 4
			self.dirx = -1 * self.get_random_x(5)
			self.diry = -1 * self.get_random_y(5)
			#move to outside of view within quadrant
			


		self.aster = self.canvas.create_oval(self.x0, self.y0, self.x1, self.y1, outline = "#FFFFFF", tags = 'asteroid')
		

	def large(self, width, height, x, y):
		self.size = 1
		center_x =  width / 2
		center_y = height / 2
		r = 60
		self.x0 = x - r
		self.y0 = y - r
		self.x1 = x + r
		self.y1 = y + r

			#quadrant 1		quadrant 2
			#quadrant 3		quadrant 4


		if self.x0 <= center_x and self.y0 <= center_y:
			#quadrant 1
			self.dirx = 1 * self.get_random_x(5)
			self.diry = 1 * self.get_random_y(5)
			#move to outside of view within quadrant
		elif self.x0 <= center_x and self.y0 >= center_y:
			#quadrant 3
			self.dirx = 1 * self.get_random_x(5)
			self.diry = -1 * self.get_random_y(5)
			#move to outside of view within quadrant
		elif self.x0 >= center_x and self.y0 <= center_y:
			#quadrant 2
			self.dirx = -1 * self.get_random_x(5)
			self.diry = 1 * self.get_random_y(5)
			#move to outside of view within quadrant
		elif self.x0 >= center_x and self.y0 >= center_y:
			#quadrant 4
			self.dirx = -1 * self.get_random_x(5)
			self.diry = -1 * self.get_random_y(5)
			#move to outside of view within quadrant

			

		self.aster = self.canvas.create_oval(self.x0, self.y0, self.x1, self.y1, outline = "#FFFFFF", tags = 'asteroid')
		

	def get_random_x(self, width):
		x  = random.randint(1, width)
		return x


	def get_random_y(self, height):
		y = random.randint(1, height)
		return y


	def get_random_size(self):
		x = random.randint(1, 3)
		return x


	def get_coords(self):
		return self.x0, self.y0, self.x1, self.y1

	def hold(master, self):
		self.move_asteroid()


	def move_asteroid(self):
		#get starting position pass through if statement to make the asteroid go 
		#toward the middle of the screen

		#Tkinter comes built in with a move() method but for some reason it doesn't 
		#change the objects coords just their location on screen
		if self.x0 <= 0:
			self.dirx = self.dirx * -1
			
		elif self.x1 <= 0:
			self.dirx = self.dirx * -1
			

		if self.x0 >= self.window_width:
			self.dirx = self.dirx * -1
			
		elif self.x1 >= self.window_width:
			self.dirx = self.dirx * -1
			

		if self.y0 <= 0:
			self.diry = self.diry * -1

		elif self.y1 <= 0:
			self.diry = self.diry * -1

		#in here is the problem
		if self.y0 >= self.window_height:
			self.diry = self.diry * -1

		elif self.y1 >= self.window_height:
			self.diry = self.diry * -1


		
		self.move_it()
		self.check_asteroid()
		self.canvas.after(50, self.move_asteroid)


	def move_it(self):
		self.x0 = self.x0 + self.dirx
		self.x1 = self.x1 + self.dirx
		self.y0 = self.y0 + self.diry
		self.y1 = self.y1 + self.diry

		self.canvas.coords(self.aster, self.x0, self.y0, self.x1, self.y1)


	def check_asteroid(self):
		#check for collision

		if (self.ship.a[0] > self.x0 and self.ship.a[0] < self.x1) and (self.ship.a[1] > self.y0 and self.ship.a[1] < self.y1):
			self.ship.destroy_me()
		if (self.ship.b[0] > self.x0 and self.ship.b[0] < self.x1) and (self.ship.b[1] > self.y0 and self.ship.b[1] < self.y1):
			self.ship.destroy_me()
		if (self.ship.c[0] > self.x0 and self.ship.c[0] < self.x1) and (self.ship.c[1] > self.y0 and self.ship.c[1] < self.y1):
			self.ship.destroy_me()
		if (self.ship.d[0] > self.x0 and self.ship.d[0] < self.x1) and (self.ship.d[1] > self.y0 and self.ship.d[1] < self.y1):
			self.ship.destroy_me()

	def undraw(self):
		self.canvas.delete(self)
		self = None





	def __init__(self, master, canvas, width, height, ship = None):
		super(asteroids, self).__init__()

		self.master = master
		self.canvas = canvas
		self.window_width = width
		self.window_height = height

		self.ship = ship

		self.draw_asteroid(self.canvas, width, height)
