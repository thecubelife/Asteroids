#ship.py
#ship class

try:
	import tkinter as tk
except ImportError:
	import Tkinter as tk
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
		#actually moves it
		#will have to replace with my own move...
		self.move_it(x, y)
		

	def move_it(self, x, y):
		self.a[0] = int(self.a[0] + x)
		self.a[1] = int(self.a[1] + y)
		
		self.b[0] = int(self.b[0] + x)
		self.b[1] = int(self.b[1] + y)
		
		self.c[0] = int(self.c[0] + x)
		self.c[1] = int(self.c[1] + y)
		
		self.d[0] = int(self.d[0] + x)
		self.d[1] = int(self.d[1] + y)

		#would have just said self.a, self.b,.....except it kept coming back as a string instead of a number
		self.canvas.coords(self.player_ship, self.a[0], self.a[1], self.b[0], self.b[1], self.c[0], self.c[1], self.d[0], self.d[1])

		self.check_ship()

	def get_center(self):
		x = 1 / 4 * (self.a[0] + self.b[0] + self.c[0] + self.d[0])
		y = 1 / 4 * (self.a[1] + self.b[1] + self.c[1] + self.d[1])
		return x, y
		

	#problem doesn't rotate in place...rotates around some distance away from ship
	#until ship is off screen
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
		#would have just said self.a, self.b,.....except it keeps coming back as a string instead of a number
		self.canvas.coords(self.player_ship, self.a[0], self.a[1], self.b[0], self.b[1], self.c[0], self.c[1], self.d[0], self.d[1])


	def check_ship(self):
		w = self.bound_width
		h = self.bound_height

		ax = self.a[0]
		ay = self.a[1]
		bx = self.b[0]
		by = self.b[1]
		cx = self.c[0]
		cy = self.c[1]
		dx = self.d[0]
		dy = self.d[1]

		#height check
		if ay < 0 and by < 0 and cy < 0 and dy < 0:
			self.a[1] = h + abs(ay) + 1
			self.b[1] = h + abs(by) + 1
			self.c[1] = h + abs(cy) + 1
			self.d[1] = h + abs(dy) + 1
			self.canvas.coords(self.player_ship, self.a[0], self.a[1], self.b[0], self.b[1], self.c[0], self.c[1], self.d[0], self.d[1])
		elif ay > h and by > h and cy > h and dy > h:
			#problem here
			self.a[1] = -15
			self.d[1] = -10
			self.c[1] = -30
			self.d[1] = -10
			self.canvas.coords(self.player_ship, self.a[0], self.a[1], self.b[0], self.b[1], self.c[0], self.c[1], self.d[0], self.d[1])



	def destroy_me(self):
		#will destroy ship
		d = 0
		


	#Note to self parameters for classes are passed through __init__ not the class name
	def __init__(self, canvas, width, height, master = None):
		super(ship, self).__init__()

		#this sets the canvas the ship is on, the heading or bearing, and the turnspeed of the ship
		self.canvas = canvas
		self.heading = -math.pi / 2
		self.turnspeed = 10
		self.bound_width = width
		self.bound_height = height


		self.oX = width / 2		#origin
		self.oY = height / 2	#origin
		self.a = [self.oX, self.oY - 15]
		self.b = [self.oX + 10, self.oY - 10]
		self.c = [self.oX, self.oY - 30]		#this is the nose of the ship at start
		self.d = [self.oX - 10, self.oY - 10]

		#this gets the starting x and y of the center of the ship
		self.x, self.y = self.get_center()


		self.draw_ship(self.canvas, width, height)
