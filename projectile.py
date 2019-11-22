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
		a = self.ax, self.ay
		c = self.cx, self.cy

		self.dirx = -1 * (a[0] - c[0])
		self.diry = -1 * (a[1] - c[1])

		self.tile = self.canvas.create_line(a, c, fill = "#FFFFFF", tags = 'projectile')
		self.move_it()

	def move_it(self):
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
				#destroy asteroid and projectile
				self.destroy_me()
				i.undraw()
			if (self.cx > x0 and self.cx < x1) and (self.cy > y0 and self.ay < y1):
				#destroy asteroid and projectile
				self.destroy_me()
				i.undraw(self.asteroids)


	def destroy_me(self):
		self.canvas.delete(self.tile)
		self = None
		

	def __init__(self, player, canvas, width, height, asteroids):
		super(Projectile, self).__init__()
		self.ship = player
		self.canvas = canvas
		self.width = width
		self.height = height
		self.asteroids = asteroids
		self.ax = self.ship.a[0]
		self.ay = self.ship.a[1]
		self.bx = self.ship.b[0]
		self.by = self.ship.b[1]
		self.cx = self.ship.c[0]
		self.cy = self.ship.c[1]
		self.dx = self.ship.d[0]
		self.dy = self.ship.d[1]

		self.draw_projectile()
