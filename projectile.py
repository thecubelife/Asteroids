#projectile.py
#projectile class

#this properly imports tkinter whether you are using python 2 or 3
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

	def check_it(self):
		#to check if it has gone off screen if so then freeze it
		if self.ax <= 0 and self.cx <= 0:
			self.freeze_me()
		elif self.ax >= self.width and self.cx >= self.width:
			self.freeze_me()
		elif self.ay <= 0 and self.cy <= 0:
			self.freeze_me()
		elif self.ay >= self.height and self.cy >= self.height:
			self.freeze_me()
		else:
			#move it again after 50 milliseconds
			#this creates a loop until the projectile has been frozen
			#at that point the loop ends
			self.canvas.after(50, self.move_it)

	def check_pos(self):
		#checks to see if it has hit an asteroid
		for i in self.asteroids:
			#iterates through all asteroids
			x0, y0, x1, y1 = i.get_coords()
			if (self.ax > x0 and self.ax < x1) and (self.ay > y0 and self.ay < y1):
				#move asteroid and projectile offscreen and freeze them
				i.undraw(self.asteroids)
				self.freeze_me()
			if (self.cx > x0 and self.cx < x1) and (self.cy > y0 and self.ay < y1):
				#move asteroid and projectile offscreen and freeze them
				i.undraw(self.asteroids)
				self.freeze_me()

	def draw_projectile(self):
		#at the beginning of the game they are frozen and moved offscreen
		a = self.width + 200, self.height + 200
		c = self.width + 200, self.height + 200

		#creates the object on the screen, in this case though it is offscreen
		self.tile = self.canvas.create_line(a, c, fill = "#FFFFFF", tags = 'projectile')

	def freeze_me(self):
		#freezes the projectile
		self.freeze = True

		#move off screen
		self.canvas.coords(self.tile, self.ax + self.width + 200, self.ay + self.height + 200, self.cx + self.width + 200, self.cy + self.height + 200)
		self.dirx = 0
		self.diry = 0
		#iterates through all the asteroids and if they are all false then the 
		#player has won the game
		x = len(self.master.asteroids)
		for i in self.master.asteroids:
			i.check_onscreen()
			if i.freeze == True:
				if self.master.asteroids.index(i) + 1 == x:
					self.master.player.offscreen()
					self.master.restart2()
				else:
					#move on to next part...because there are more asteroids
					pass

			else:
				#one or more are still onscreen and so the user has not won
				break

	def move_it(self):
		#checks if the projectile is frozen or not
		if self.freeze == False:
			#moves the projectile the x and y direction from its current position
			self.ax = self.ax + self.dirx
			self.ay = self.ay + self.diry
			self.cx = self.cx + self.dirx
			self.cy = self.cy + self.diry

			#redraws it on screen
			self.canvas.coords(self.tile, self.ax, self.ay, self.cx, self.cy)

			#checks if it is offscreen
			self.check_it()

			#checks if it has hit an asteroid
			self.check_pos()

	def ship_start(self):
		#calls when the user has pressed the space bar

		if self.freeze == False:
			#sets the projectile's coords to the ship
			self.ax = self.ship.a[0]
			self.cx = self.ship.c[0]
			self.ay = self.ship.a[1]
			self.cy = self.ship.c[1]
			a = self.ship.a[0], self.ship.a[1]
			c = self.ship.c[0], self.ship.c[1]

			#gives the projectile a speed and a direction
			#it is negative because of the way the coords are on a computer
			self.dirx = -2 * (a[0] - c[0])
			self.diry = -2 * (a[1] - c[1])

			
			self.canvas.coords(self.tile, self.ax, self.ay, self.cx, self.cy)

			#moves the projectile
			self.move_it()


	def __init__(self, player, canvas, width, height, asteroids, master = None):
		super(Projectile, self).__init__()
		#this creates the object

		#this gives the object easily callable variables from anywhere without
		#needing to pass them...it also always one function to change the variable's value everywhere
		self.ship = player
		self.canvas = canvas
		self.width = width
		self.height = height
		self.asteroids = asteroids
		self.master = master

		#this sets the starting point of the projectile so that it can be changed elsewhere
		self.ax = 0
		self.ay = 0
		self.cx = 0
		self.cy = 0

		#this freezes the projectile
		self.freeze = True

		#this draws the projectile off the screeen
		self.draw_projectile()
