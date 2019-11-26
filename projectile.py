#projectile.py
#projectile class


try:
	import tkinter as tk
except ImportError:
	import Tkinter as tk
import time
import math
import random
#this is used to pass arguments to a button command which could not be done otherwise
from functools import partial


class Projectile:


	def draw_projectile(self):
		a = self.width + 200, self.height + 200
		c = self.width + 200, self.height + 200

		self.dirx = -1 * (a[0] - c[0])
		self.diry = -1 * (a[1] - c[1])

		self.tile = self.canvas.create_line(a, c, fill = "#FFFFFF", tags = 'projectile')


	def move_it(self):
		if self.freeze == False:
			self.ax = self.ax + self.dirx
			self.ay = self.ay + self.diry
			self.cx = self.cx + self.dirx
			self.cy = self.cy + self.diry

			self.canvas.coords(self.tile, self.ax, self.ay, self.cx, self.cy)

		self.check_it()

		self.check_pos()

	#to check if it has gone off screen if so then delete it
	def check_it(self):
		if self.ax <= 0 and self.cx <= 0:
			self.destroy_me()
		elif self.ax >= self.width and self.cx >= self.width:
			self.destroy_me()
		elif self.ay <= 0 and self.cy <= 0:
			self.destroy_me()
		elif self.ay >= self.height and self.cy >= self.height:
			self.destroy_me()
		else:
			self.canvas.after(50, self.move_it)

	def check_pos(self):
		for i in self.asteroids:
			x0, y0, x1, y1 = i.get_coords()
			if (self.ax > x0 and self.ax < x1) and (self.ay > y0 and self.ay < y1):
				#move asteroid and projectile
				self.destroy_me()
				i.undraw(self.asteroids)
			if (self.cx > x0 and self.cx < x1) and (self.cy > y0 and self.ay < y1):
				#move asteroid and projectile
				self.destroy_me()
				i.undraw(self.asteroids)

	def ship_start(self):
		#move it to ships start
		self.ax = self.ship.a[0]
		self.cx = self.ship.c[0]
		self.ay = self.ship.a[1]
		self.cy = self.ship.a[1]
		a = self.ship.a[0], self.ship.a[1]
		c = self.ship.c[0], self.ship.c[1]

		self.dirx = -1 * (a[0] - c[0])
		self.diry = -1 * (a[1] - c[1])

		self.canvas.coords(self.tile, self.ax, self.ay, self.cx, self.cy)

		self.move_it()

	def destroy_me(self):
		self.freeze = True
		#move off screen
		self.canvas.coords(self.tile, self.ax + self.width + 200, self.ay + self.height + 200, self.cx + self.width + 200, self.cy + self.height + 200)
		

	def __init__(self, player, canvas, width, height, asteroids):
		super(Projectile, self).__init__()
		self.ship = player
		self.canvas = canvas
		self.width = width
		self.height = height
		self.asteroids = asteroids

		self.freeze = True

		self.draw_projectile()
