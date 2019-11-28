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
		self.player_ship = canvas.create_polygon(self.points, fill = "#FFFFFF", tags = 'ship')


	def move_ship(master, self, canvas, mystate, upcount, d):
		self.upcount = upcount
		if self.freeze == False:
			if mystate == True:
				if self.upcount == 0:
					self.upcount += 1
					self.move_it(d)
			else:
				self.decel(d)
			
		

	def move_it(self, d):
		#figure out how to reset speed and keep it moving until the ship stops
		#acceleration
		if self.speed < 1:
			self.speed += (self.acceleration * 1/10) * (d)

		#based off someone else's code...since i don't understand trigonomotry
		self.a[0] += self.speed * math.cos(self.heading)
		self.b[0] += self.speed * math.cos(self.heading)
		self.c[0] += self.speed * math.cos(self.heading)
		self.d[0] += self.speed * math.cos(self.heading)

		self.a[1] += self.speed * math.sin(self.heading)
		self.b[1] += self.speed * math.sin(self.heading)
		self.c[1] += self.speed * math.sin(self.heading)
		self.d[1] += self.speed * math.sin(self.heading)
		
		self.x, self.y = self.get_center()


		self.canvas.coords(self.player_ship, self.a[0], self.a[1], self.b[0], self.b[1], self.c[0], self.c[1], self.d[0], self.d[1])

		self.check_ship()

		
		if self.upcount != 0:
			#change this to the amount between repeating keys at the moment it is too fast
			self.canvas.after(100, self.move_it, d)


	
	def decel(self, d):
		self.upcount = 0

		if self.speed > 0:
			#based off someone else's code...since i don't understand trigonomotry
			self.a[0] += self.speed * math.cos(self.heading)
			self.b[0] += self.speed * math.cos(self.heading)
			self.c[0] += self.speed * math.cos(self.heading)
			self.d[0] += self.speed * math.cos(self.heading)

			self.a[1] += self.speed * math.sin(self.heading)
			self.b[1] += self.speed * math.sin(self.heading)
			self.c[1] += self.speed * math.sin(self.heading)
			self.d[1] += self.speed * math.sin(self.heading)
			
			self.x, self.y = self.get_center()


			self.canvas.coords(self.player_ship, self.a[0], self.a[1], self.b[0], self.b[1], self.c[0], self.c[1], self.d[0], self.d[1])

			self.check_ship()

			if self.speed != 0:
				self.speed -= (1/40 * self.acceleration *1/10 * (d))
				self.canvas.after(50, self.decel, d)


	def get_center(self):
		x = 1 / 4 * (self.a[0] + self.b[0] + self.c[0] + self.d[0])
		y = 1 / 4 * (self.a[1] + self.b[1] + self.c[1] + self.d[1])
		return x, y
		

	#Based on another person's code
	def rotate_ship(self, turnstate, turncount, direction, event = None):
		self.turncount = turncount
		if self.freeze == False:
			if turnstate == True:
				if self.turncount == 0:
					self.turncount += 1
					self.rotate(direction)
			else:
				self.stop_turning()

	def stop_turning(self):
		self.turncount = 0

	def rotate(self, direction, event = None):
		if self.freeze == False:
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

			if self.turncount != 0:
				self.canvas.after(100, self.rotate, direction)


	#based on another person's code
	def change_coords(self):
		#would have just said self.a, self.b,.....except it keeps coming back as a string instead of a number
		self.canvas.coords(self.player_ship, self.a[0], self.a[1], self.b[0], self.b[1], self.c[0], self.c[1], self.d[0], self.d[1])

	
		#bug in here
	
	def check_ship(self):
		#check if ship is off screen
		w = self.bound_width
		h = self.bound_height

		ih = self.invhei
		iw = self.invwid

		ax = self.a[0]
		ay = self.a[1]
		bx = self.b[0]
		by = self.b[1]
		cx = self.c[0]
		cy = self.c[1]
		dx = self.d[0]
		dy = self.d[1]

		#height check
		if ay < -ih and by < -ih and cy < -ih and dy < -ih:
			#up check
			self.a[1] = h + ih - abs(ay - ih) + (14/6 * ih)
			self.b[1] = h + ih - abs(by - ih) + (14/6 * ih)
			self.c[1] = h + ih - abs(cy - ih) + (14/6 * ih)
			self.d[1] = h + ih - abs(dy - ih) + (14/6 * ih)
			self.canvas.coords(self.player_ship, self.a[0], self.a[1], self.b[0], self.b[1], self.c[0], self.c[1], self.d[0], self.d[1])
		elif ay > h + ih and by > h + ih and cy > h + ih and dy > h + ih:
			#problem here..ship warps
			#down check

			if (ay > by) and (ay > cy) and (ay > dy):
				self.a[1] = ay - ay - (1/2 * ih)
				self.b[1] = by - ay - (1/2 * ih)
				self.c[1] = cy - ay - (1/2 * ih)
				self.d[1] = dy - ay - (1/2 * ih)

			elif (by > ay) and (by > cy):
				self.a[1] = ay - by - (1/2 * ih)
				self.b[1] = by - by - (1/2 * ih)
				self.c[1] = cy - by - (1/2 * ih)
				self.d[1] = dy - by - (1/2 * ih)
				
			elif (cy > ay) and (cy > by) and (cy > dy):
				self.a[1] = ay - cy - (1/2 * ih)
				self.b[1] = by - cy - (1/2 * ih)
				self.c[1] = cy - cy - (1/2 * ih)
				self.d[1] = dy - cy - (1/2 * ih)


			elif (dy > ay) and (dy > cy):
				self.a[1] = ay - dy - (1/2 * ih)
				self.b[1] = by - dy - (1/2 * ih)
				self.c[1] = cy - dy - (1/2 * ih)
				self.d[1] = dy - dy - (1/2 * ih)

			self.canvas.coords(self.player_ship, self.a[0], self.a[1], self.b[0], self.b[1], self.c[0], self.c[1], self.d[0], self.d[1])

		#width check
		if ax < -iw and bx < -iw and cx < -iw and dx < -iw:
			#left check
			self.a[0] = w + iw - abs(ax - iw) + (14/6 * iw)
			self.b[0] = w + iw - abs(bx - iw) + (14/6 * iw)
			self.c[0] = w + iw - abs(cx - iw) + (14/6 * iw)
			self.d[0] = w + iw - abs(dx - iw) + (14/6 * iw)
			self.canvas.coords(self.player_ship, self.a[0], self.a[1], self.b[0], self.b[1], self.c[0], self.c[1], self.d[0], self.d[1])

		elif ax > w + iw and bx > w + iw and cx > w + iw and dx > w + iw:
			#problem here...ship warps
			#right check

			if (ax > bx) and (ax > cx) and (ax > dx):
				self.a[0] = ax - ax - (1/2 * iw)
				self.b[0] = bx - ax - (1/2 * iw)
				self.c[0] = cx - ax - (1/2 * iw)
				self.d[0] = dx - ax - (1/2 * iw)

			elif (bx > ax) and (bx > cx):
				self.a[0] = ax - bx - (1/2 * iw)
				self.b[0] = bx - bx - (1/2 * iw)
				self.c[0] = cx - bx - (1/2 * iw)
				self.d[0] = dx - bx - (1/2 * iw)
				
			elif (cx > ax) and (cx > bx) and (cx > dx):
				self.a[0] = ax - cx - (1/2 * iw)
				self.b[0] = bx - cx - (1/2 * iw)
				self.c[0] = cx - cx - (1/2 * iw)
				self.d[0] = dx - cx - (1/2 * iw)

			elif (dx > ax) and (dx > cx):
				self.a[0] = ax - dx - (1/2 * iw)
				self.b[0] = bx - dx - (1/2 * iw)
				self.c[0] = cx - dx - (1/2 * iw)
				self.d[0] = dx - dx - (1/2 * iw)


			self.canvas.coords(self.player_ship, self.a[0], self.a[1], self.b[0], self.b[1], self.c[0], self.c[1], self.d[0], self.d[1])


	def destroy_me(self):
		self.canvas.delete('ship')
		self.canvas.delete('asteroid')
		self.canvas.delete('projectile')


		#put them off screen		


		self.master.restart()

	#Note to self parameters for classes are passed through __init__ not the class name
	def __init__(self, canvas, width, height, master = None):
		super(ship, self).__init__()

		#this sets the canvas the ship is on, the heading or bearing, and the turnspeed of the ship
		self.master = master
		self.canvas = canvas
		self.heading = -math.pi / 2
		self.speed = 0
		self.acceleration = 1
		self.turnspeed = 10
		self.bound_width = width
		self.bound_height = height

		self.freeze = False

		self.invwid = 30
		self.invhei = 30


		self.oX = width / 2		#origin
		self.oY = height / 2	#origin
		self.a = [self.oX, self.oY - 15]
		self.b = [self.oX + 10, self.oY - 10]
		self.c = [self.oX, self.oY - 30]		#this is the nose of the ship at start
		self.d = [self.oX - 10, self.oY - 10]

		#this gets the starting x and y of the center of the ship
		self.x, self.y = self.get_center()


		self.draw_ship(self.canvas, width, height)
