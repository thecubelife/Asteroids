#ship.py
#ship class

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


class ship:

	def change_coords(self):
		#would have just said self.a, self.b,.....except it keeps coming back as a string instead of a number
		self.canvas.coords(self.player_ship, self.a[0], self.a[1], self.b[0], self.b[1], self.c[0], self.c[1], self.d[0], self.d[1])

	def check_ship(self):
		#check if ship is off screen
		w = self.bound_width
		h = self.bound_height

		#this is the extra space the ship is given before being moved to the other side of the screen
		ih = self.invhei
		iw = self.invwid

		#this saved me some space
		ax = self.a[0]
		ay = self.a[1]
		bx = self.b[0]
		by = self.b[1]
		cx = self.c[0]
		cy = self.c[1]
		dx = self.d[0]
		dy = self.d[1]

		#checks if the ship is not frozen
		if self.freeze == False:
			#height check

			if ay < -ih and by < -ih and cy < -ih and dy < -ih:
				#up check
				self.a[1] = h + ih - abs(ay - ih) + (14/6 * ih)
				self.b[1] = h + ih - abs(by - ih) + (14/6 * ih)
				self.c[1] = h + ih - abs(cy - ih) + (14/6 * ih)
				self.d[1] = h + ih - abs(dy - ih) + (14/6 * ih)
				self.canvas.coords(self.player_ship, self.a[0], self.a[1], self.b[0], self.b[1], self.c[0], self.c[1], self.d[0], self.d[1])
			
			elif ay > h + ih and by > h + ih and cy > h + ih and dy > h + ih:
				#down check

				#the following if statements check which point of the ship is fathest
				#from the origin and uses that value to move the ship to the other side of the screen
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

				#this is what physically moves it on the screen
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
				#right check

				##the following if statements check which point of the ship is fathest
				#from the origin and uses that value to move the ship to the other side of the screen
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

				#this physically moves the coords of the ship
				self.canvas.coords(self.player_ship, self.a[0], self.a[1], self.b[0], self.b[1], self.c[0], self.c[1], self.d[0], self.d[1])

	def decel(self, d):
		self.upcount = 0
		#this resets the check for whether the key has been released or not
		
		if self.freeze == False:
			#this checks if the ship is frozen or not
			if self.speed > 0:
				#while it has a speed greater than zero run this

				#based off someone else's code...since I don't understand trigonomotry
				
				#however what i do believe is happening is it is using the heading of the ship
				#to set the new position
				self.a[0] += self.speed * math.cos(self.heading)
				self.b[0] += self.speed * math.cos(self.heading)
				self.c[0] += self.speed * math.cos(self.heading)
				self.d[0] += self.speed * math.cos(self.heading)

				self.a[1] += self.speed * math.sin(self.heading)
				self.b[1] += self.speed * math.sin(self.heading)
				self.c[1] += self.speed * math.sin(self.heading)
				self.d[1] += self.speed * math.sin(self.heading)
				
				#this gets the new center which is essential for turning the ship
				self.x, self.y = self.get_center()

				#this physically moves the ship across the screen
				self.canvas.coords(self.player_ship, self.a[0], self.a[1], self.b[0], self.b[1], self.c[0], self.c[1], self.d[0], self.d[1])

				#this checks if the ship is off the screen or not
				self.check_ship()

				#this reduces the speed and if the speed is not zero yet
				#than it continues this function
				if self.speed != 0:
					self.speed -= (1/40 * self.acceleration *1/10 * (d))
					self.canvas.after(50, self.decel, d)

	def destroy_me(self):
		#this freezes the ship, projectiles, and asteroids
		#then it moves the ship off the screen

		self.freeze = True
		for i in self.master.projectiles:
			i.freeze_me()
		for i in self.master.asteroids:
			i.undraw()
		self.offscreen()

		#this restarts the game
		self.master.restart()

	def draw_ship(self, canvas, width, height):
		#this places all the points within a list
		self.points = self.a, self.b, self.c, self.d

		#this places the ship on the screen
		self.player_ship = canvas.create_polygon(self.points, fill = "#FFFFFF", tags = 'ship')

	def get_center(self):
		#this gets the center of the ship, which is essential to rotate it correctly
		x = 1 / 4 * (self.a[0] + self.b[0] + self.c[0] + self.d[0])
		y = 1 / 4 * (self.a[1] + self.b[1] + self.c[1] + self.d[1])
		return x, y

	def move_it(self, d):
		#check if it not frozen
		if self.freeze == False:
			#checks if the speed is less than max and if so then it increases it
			if self.speed < 1.5:
				self.speed += (self.acceleration * 1/10) * (d)

			#based off someone else's code...since i don't understand trigonomotry
			#However, from what i can tell it uses the heading and multiplies
			#the speed by it and then adds that to the coords of the ship
			self.a[0] += self.speed * math.cos(self.heading)
			self.b[0] += self.speed * math.cos(self.heading)
			self.c[0] += self.speed * math.cos(self.heading)
			self.d[0] += self.speed * math.cos(self.heading)

			self.a[1] += self.speed * math.sin(self.heading)
			self.b[1] += self.speed * math.sin(self.heading)
			self.c[1] += self.speed * math.sin(self.heading)
			self.d[1] += self.speed * math.sin(self.heading)
			
			#this gets the new center of the ship which is essential for rotating it
			self.x, self.y = self.get_center()

			#this physically moves it
			self.canvas.coords(self.player_ship, self.a[0], self.a[1], self.b[0], self.b[1], self.c[0], self.c[1], self.d[0], self.d[1])

			#this checks to see if the ship has gone off the screen
			self.check_ship()

			#this checks if the key is still being pressed and if so then it calls the move_it method
			if self.upcount != 0:
				#change this to the amount between repeating keys at the moment it is too fast
				self.canvas.after(100, self.move_it, d)

	def move_ship(master, self, canvas, mystate, upcount, d):
		#this variable is used so that i don't start multiple loops doing the same thing
		self.upcount = upcount
		if self.freeze == False:
			#this checks if the ship is not frozen

			#this checks if the key has been pressed or released and calls 
			#two different functions depending on the state
			if mystate == True:
				if self.upcount == 0:
					self.upcount += 1
					#this moves the ship
					self.move_it(d)
			else:
				#this slows down the ship
				self.decel(d)

	def offscreen(self):
		#sets the ship to fozen and moves it off the screen
		self.freeze = True
		self.a[0] = self.a[0] + self.bound_width + 400
		self.b[0] = self.b[0] + self.bound_width + 400
		self.c[0] = self.c[0] + self.bound_width + 400
		self.d[0] = self.d[0] + self.bound_width + 400

		self.a[1] = self.a[1] + self.bound_width + 400
		self.b[1] = self.b[1] + self.bound_width + 400
		self.c[1] = self.c[1] + self.bound_width + 400
		self.d[1] = self.d[1] + self.bound_width + 400

		#this physically moves the ship
		self.canvas.coords(self.player_ship, self.a[0], self.a[1], self.b[0], self.b[1], self.c[0], self.c[1], self.d[0], self.d[1])

	def restart_ship(self):
		#this sets the starting heading
		self.heading = -math.pi / 2
		self.freeze = False

		#this sets the starting points for the ship and creates its shape
		self.a = [self.oX, self.oY - 15]
		self.b = [self.oX + 10, self.oY - 10]
		self.c = [self.oX, self.oY - 30]		
		self.d = [self.oX - 10, self.oY - 10]

		#this gets the starting center value which is essential for rotating
		self.x, self.y = self.get_center()

		#this physically draws the ship on the screen
		self.draw_ship(self.canvas, self.bound_width, self.bound_height)

	def rotate(self, direction, event = None):
		#this rotates the ship
		#this is based off of someone else's code

		if self.freeze == False:
			#checks if the ship is not frozen

			#sets the turn distance based on the direction turn speed and radians
			tspeed = direction * self.turnspeed * math.pi / 180
			self.heading -= tspeed

			def _rotatec(x, y):
				#this is based on someone else's code
				x -= self.x			#center of the ship
				y -= self.y			#center of the ship

				#as far as i can tell this gets the new coords of the ship
				newx = x * math.cos(tspeed) + y * math.sin(tspeed)
				newy = -x * math.sin(tspeed) + y * math.cos(tspeed)
				return newx + self.x, newy + self.y
			
			#rotates each of the 4 points of the ship
			self.a[0], self.a[1] = _rotatec(self.a[0], self.a[1])
			self.b[0], self.b[1] = _rotatec(self.b[0], self.b[1])
			self.c[0], self.c[1] = _rotatec(self.c[0], self.c[1])
			self.d[0], self.d[1] = _rotatec(self.d[0], self.d[1])

			#gets the new center of the ship
			self.x, self.y = self.get_center()
			#this changes the coords of the ship to the new points
			self.change_coords()

			#this checks if the key is still pressed and if so then it calls itself
			if self.turncount != 0:
				self.canvas.after(100, self.rotate, direction)

	def rotate_ship(self, turnstate, turncount, direction, event = None):
		#this checks if one of the turning keys is being pressed
		#otherwise it stops the ship rotating
		self.turncount = turncount
		if self.freeze == False:
			if turnstate == True:
				if self.turncount == 0:
					self.turncount += 1
					self.rotate(direction)
			else:
				self.stop_turning()

	def stop_turning(self):
		#this stops the ships rotate loop
		self.turncount = 0


	def __init__(self, canvas, width, height, master = None):
		super(ship, self).__init__()


		#this gives the object easily callable variables from anywhere without
		#needing to pass them...it also always one function to change the variable's value everywhere

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

		#this sets the outside boundary of the screen
		self.invwid = 30
		self.invhei = 30

		#this sets the middle of the screen and ship points relative to it
		self.oX = width / 2		#origin
		self.oY = height / 2	#origin
		self.a = [self.oX, self.oY - 15]
		self.b = [self.oX + 10, self.oY - 10]
		self.c = [self.oX, self.oY - 30]		#this is the nose of the ship at start
		self.d = [self.oX - 10, self.oY - 10]

		#this gets the starting x and y of the center of the ship
		self.x, self.y = self.get_center()

		#this draws the ship on the screen
		self.draw_ship(self.canvas, width, height)
