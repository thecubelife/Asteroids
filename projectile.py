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
		a = self.a
		c = self.c

		self.dirx = -1 * (a[0] - c[0])
		self.diry = -1 * (a[1] - c[1])

		self.tile = self.canvas.create_line(a, c, fill = "#FFFFFF", tags = 'projectile')
		self.move_it()

	def move_it(self):
		self.a[0] = self.a[0] + self.dirx
		self.a[1] = self.a[1] + self.diry
		self.c[0] = self.c[0] + self.dirx
		self.c[1] = self.c[1] + self.diry

		self.canvas.coords(self.tile, self.a[0], self.a[1], self.c[0], self.c[1])

		self.check_it()

	#to check if it has gone off screen if so then delete it
	def check_it(self):
		if self.a[0] <= 0 and self.c[0] <= 0:
			self.destroy_me()
		elif self.a[0] >= self.width and self.c[0] >= self.width:
			self.destroy_me()
		elif self.a[1] <= 0 and self.c[1] <= 0:
			self.destroy_me()
		elif self.a[1] >= self.height and self.c[1] >= self.height:
			self.destroy_me()
		else:
			self.canvas.after(50, self.move_it)

	def destroy_me(self):
		self.canvas.delete()
		self = None
		

	def __init__(self, player, canvas, width, height):
		super(Projectile, self).__init__()
		self.ship = player
		self.canvas = canvas
		self.width = width
		self.height = height
		self.a = self.ship.a
		self.b = self.ship.b
		self.c = self.ship.c
		self.d = self.ship.d

		self.draw_projectile()
