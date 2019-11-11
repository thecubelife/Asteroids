#ship.py
#ship class

import tkinter as tk
import time
import math
import random
#this is used to pass arguments to a button command which could not be done otherwise
from functools import partial


class ship:

	def draw_ship(self, canvas, width, height):
		
		self.points = self.a, self.b, self.c, self.d
		#this does actually create a triangle
		self.player_ship = canvas.create_polygon(self.points, fill = "#FFFFFF")


	def move_ship(master, self, canvas, x, y):
		#actually moves it, once it gets the player object tag or ID
		self.canvas.move(self.player_ship, x, y)


	def get_center(self):
		x = 1 / 3 * (self.a[0] + self.b[0] + self.c[0] + self.d[0])
		y = 1 / 3 * (self.a[1] + self.b[1] + self.c[1] + self.d[1])
		return x, y
		


	#Based on another persons code
	def rotate_ship(self, direction, event = None):
		tspeed = direction * self.turnspeed * math.pi / 180
		self.heading -= tspeed

		def _rotatec(x, y):
			x -= self.x			#center of the ship
			y -= self.y			#center of the ship

			newx = x * math.cos(tspeed) + y * math.sin(tspeed)
			newy = -x * math.sin(tspeed) + y * math.cos(tspeed)
			return newx + self.x, newy + self.y
		
		self.a[0], self.a[1] = _rotatec(self.a[0], self.a[1])
		self.b[0], self.b[1] = _rotatec(self.b[0], self.b[1])
		self.c[0], self.c[1] = _rotatec(self.c[0], self.c[1])
		self.d[0], self.d[1] = _rotatec(self.d[0], self.d[1])


		self.x, self.y = self.get_center()
		self.change_coords()

	#based on another persons code
	def change_coords(self):
		self.canvas.coords(self.player_ship, self.a, self.b, self.c, self.d)


	def check_ship(self, canvas, x, y, width, height):
		return self.a, self.b, self.c, self.d



	#Note to self parameters for classes are passed through __init__ not the class name
	def __init__(self, canvas, width, height, master = None):
		super(ship, self).__init__()

		#this sets the canvas the ship is on, the heading or bearing, and the turnspeed of the ship
		self.canvas = canvas
		self.heading = -math.pi / 2
		self.turnspeed = 10


		self.oX = width / 2		#origin
		self.oY = height / 2	#origin
		self.a = [self.oX, self.oY - 15]
		self.b = [self.oX + 10, self.oY - 10]
		self.c = [self.oX, self.oY - 30]		#this is the nose of the ship at start
		self.d = [self.oX - 10, self.oY - 10]

		#this gets the starting x and y of the center of the ship
		self.x, self.y = self.get_center()


		self.draw_ship(self.canvas, width, height)
