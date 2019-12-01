#asteroids_class.py
#asteroids class

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


class asteroids:

	def break_apart(self, x0, y0, x1, y1):
		#this is called when the asteroid is hit by a projectile

		#this checks the size and then creates two smaller asteroids
		if self.size == 3:
			#create a medium asteroid
			for i in self.master.medium_asteroids:
				#gets the first asteroid not being used
				if i.freeze == True:
					i.freeze = False
					ox0, oy0, ox1, oy1 = i.get_coords()
					nx = abs(x0 - ox0)
					ny = abs(y0 - oy0)
					#gets the difference between the asteroids 
					#and then moves the new asteroid that far across the screen
					i.x0 = i.x0 + nx
					i.x1 = i.x1 + nx
					i.y0 = i.y0 + ny
					i.y1 = i.y1 + ny
					
					i.canvas.coords(i.aster, i.x0, i.y0, i.x1, i.y1)

					#gets a random direction for the asteroid to go
					i.dirx, i.diry = i.get_direction(self.window_width / 2, self.window_height / 2)
					#this starts the asteroids movement loop
					i.hold()

					break
					#this makes sure it only grabs one asteroid

			#creates a medium asteroid
			for i in self.master.medium_asteroids:
				#gets the next asteroid not being used
				if i.freeze == True:
					i.freeze = False
					ox0, oy0, ox1, oy1 = i.get_coords()
					nx = abs(x1 - ox1)
					ny = abs(y1 - oy1)
					#gets the difference between the asteroids
					#and then moves the new asteroid that far across the screen
					i.x0 = i.x0 + nx
					i.x1 = i.x1 + nx
					i.y0 = i.y0 + ny
					i.y1 = i.y1 + ny
					
					i.canvas.coords(i.aster, i.x0, i.y0, i.x1, i.y1)

					#gets a random direction for the asteroid to go
					i.dirx, i.diry = i.get_direction(self.window_width / 2, self.window_height / 2)
					#this start the asteroids movement loop
					i.hold()

					break
					#this makes sure it only grabs one asteroid


		#this executes if the destroyed asteroid was medium
		elif self.size == 2:
			#creates a small asteroid
			for i in self.master.small_asteroids:
				#gets the next asteroid not being used
				if i.freeze == True:
					i.freeze = False
					ox0, oy0, ox1, oy1 = i.get_coords()
					nx = abs(x0 - ox0)
					ny = abs(y0 - oy0)
					#gets the difference between the asteroids
					#and then moves the new asteroid that far across the screen
					i.x0 = i.x0 + nx
					i.x1 = i.x1 + nx
					i.y0 = i.y0 + ny
					i.y1 = i.y1 + ny
					
					i.canvas.coords(i.aster, i.x0, i.y0, i.x1, i.y1)

					#gets a random direction for the asteroid to go
					i.dirx, i.diry = i.get_direction(self.window_width / 2, self.window_height / 2)
					#this starts the asteroids movement loop
					i.hold()

					break
					#this makes sure it only grabs one asteroid

			for i in self.master.small_asteroids:
				#gets the next asteroid not being used
				if i.freeze == True:
					i.freeze = False
					ox0, oy0, ox1, oy1 = i.get_coords()
					nx = abs(x1 - ox1)
					ny = abs(y1 - oy1)
					#gets the difference between the asteroids
					#and then moves the new asteroid that far across the screen
					i.x0 = i.x0 + nx
					i.x1 = i.x1 + nx
					i.y0 = i.y0 + ny
					i.y1 = i.y1 + ny
					
					i.canvas.coords(i.aster, i.x0, i.y0, i.x1, i.y1)
					#gets a random direction for the asteroid to go
					i.dirx, i.diry = i.get_direction(self.window_width / 2, self.window_height / 2)
					#this starts the asteroids movement loop
					i.hold()
					
					break
					#this makes sure it only grabs one asteroid
		#else it is a small asteroid so it is ignored

	def check_asteroid(self):
		#check for collision and if it has hit a ship then destroy it

		if (self.ship.a[0] > self.x0 and self.ship.a[0] < self.x1) and (self.ship.a[1] > self.y0 and self.ship.a[1] < self.y1):
			self.ship.destroy_me()
		if (self.ship.b[0] > self.x0 and self.ship.b[0] < self.x1) and (self.ship.b[1] > self.y0 and self.ship.b[1] < self.y1):
			self.ship.destroy_me()
		if (self.ship.c[0] > self.x0 and self.ship.c[0] < self.x1) and (self.ship.c[1] > self.y0 and self.ship.c[1] < self.y1):
			self.ship.destroy_me()
		if (self.ship.d[0] > self.x0 and self.ship.d[0] < self.x1) and (self.ship.d[1] > self.y0 and self.ship.d[1] < self.y1):
			self.ship.destroy_me()

	def check_onscreen(self):
		#checks if the asteroid is onscreen
		x0, y0, x1, y1 = self.get_coords()
		if (x0 >= 0 and x0 <= self.window_width) or (x1 >= 0 and x1 <= self.window_width):
			if (y0 >= 0 and y0 <= self.window_height) or (y1 >= 0 and y1 <= self.window_height):
				#makes sure the asteroid is not frozen
				self.freeze = False
			else:
				#freezes the asteroid if not already frozen
				self.freeze = True
		else:
			#freezes the asteroid if not already frozen
			self.freeze = True

	def draw_asteroid(self, canvas, width, height):
		#draws the asteroid

		#gets a random coordinate on the screen
		ranx = self.get_random_x(width)
		rany = self.get_random_y(height)
		self.x = ranx
		self.y = rany
		#makes the asteroid depending on the size
		if self.size == 1:
			self.small(width, height, self.x, self.y)
		elif self.size == 2:
			self.medium(width, height, self.x, self.y)
		elif self.size == 3:
			self.large(width, height, self.x, self.y)
		else:
			#if for some reason it is not one of those three than make it large
			self.large(width, height, self.x, self.y)

	def freeze_it(self):
		self.freeze = True

		self.x0 = self.x0 - self.window_width - 200
		self.y0 = self.y0 - self.window_height - 200
		self.x1 = self.x1 - self.window_width - 200
		self.y1 = self.y1 - self.window_height - 200

		self.dirx = 0
		self.diry = 0


		self.canvas.coords(self.aster, self.x0 - self.window_width - 200, self.y0 - self.window_height - 200, self.x1 - self.window_width - 200, self.y1 - self.window_height - 200)

	def get_coords(self):
		return self.x0, self.y0, self.x1, self.y1

	def get_direction(self, x, y):
		center_x = x
		center_y = y
			#quadrant 1		quadrant 2
			#quadrant 3		quadrant 4
		
		if self.x0 <= center_x and self.y0 <= center_y:
			#quadrant 1
			dirx = 1 * self.get_random_speed(5)
			diry = 1 * self.get_random_speed(5)
			#move to outside of view within quadrant
		elif self.x0 <= center_x and self.y0 >= center_y:
			#quadrant 3
			dirx = 1 * self.get_random_speed(5)
			diry = -1 * self.get_random_speed(5)
			#move to outside of view within quadrant
		elif self.x0 >= center_x and self.y0 <= center_y:
			#quadrant 2
			dirx = -1 * self.get_random_speed(5)
			diry = 1 * self.get_random_speed(5)
			#move to outside of view within quadrant
		elif self.x0 >= center_x and self.y0 >= center_y:
			#quadrant 4
			dirx = -1 * self.get_random_speed(5)
			diry = -1 * self.get_random_speed(5)
			#move to outside of view within quadrant

		return dirx, diry

	def get_random_speed(self, width):
		x = random.randint(1, width)
		return x

	def get_random_x(self, width):
		x  = random.randint(1, width)
		if x < 40:
			x = x + 40
		if x > width - 40:
			x = x - 40
		return x

	def get_random_y(self, height):
		y = random.randint(1, height)
		if y < 40:
			y = y + 40
		if y > height - 40:
			y = y - 40
		return y

	def hold(self):
		if self.freeze == False:
			self.move_asteroid()
		else:
			self.freeze_it()

	def large(self, width, height, x, y):
		center_x =  width / 2
		center_y = height / 2
		r = 60
		self.x0 = x - r
		self.y0 = y - r
		self.x1 = x + r
		self.y1 = y + r

		self.dirx, self.diry = self.get_direction(center_x, center_y)

			

		self.aster = self.canvas.create_oval(self.x0, self.y0, self.x1, self.y1, outline = "#FFFFFF", tags = 'asteroid')
	
	def medium(self, width, height, x, y):
		center_x =  width / 2
		center_y = height / 2
		r = 30
		self.x0 = x - r
		self.y0 = y - r
		self.x1 = x + r
		self.y1 = y + r

		self.dirx, self.diry = self.get_direction(center_x, center_y)
			


		self.aster = self.canvas.create_oval(self.x0, self.y0, self.x1, self.y1, outline = "#FFFFFF", tags = 'asteroid')
		
	def move_asteroid(self):
		#get starting position pass through if statement to make the asteroid go 
		#toward the middle of the screen
		if self.freeze == False:
			if self.count == 10:
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
			else:
				self.count += 1

		
			self.move_it()
			self.check_asteroid()
			self.canvas.after(50, self.move_asteroid)
	
	def move_it(self):
		if self.freeze == False:
			self.x0 = self.x0 + self.dirx
			self.x1 = self.x1 + self.dirx
			self.y0 = self.y0 + self.diry
			self.y1 = self.y1 + self.diry

			self.canvas.coords(self.aster, self.x0, self.y0, self.x1, self.y1)

	def redraw_asteroid(self):
		ranx = self.get_random_x(self.window_width)
		rany = self.get_random_y(self.window_height)
		self.x = ranx
		self.y = rany
		if self.size == 1:
			self.small(self.window_width, self.window_height, self.x, self.y)
		elif self.size == 2:
			self.medium(self.window_width, self.window_height, self.x, self.y)
		else:
			self.large(self.window_width, self.window_height, self.x, self.y)

	def small(self, width, height, x, y):
		center_x =  width / 2
		center_y = height / 2
		r = 10
		self.x0 = x - r
		self.y0 = y - r
		self.x1 = x + r
		self.y1 = y + r


		self.dirx, self.diry = self.get_direction(center_x, center_y)


		self.aster = self.canvas.create_oval(self.x0, self.y0, self.x1, self.y1, outline = "#FFFFFF", tags = 'asteroid')
	
	def undraw(self, asteroids = None):
		self.freeze = True
		x0 = self.x0
		y0 = self.y0
		x1 = self.x1
		y1 = self.y1


		self.x0 = self.x0 - self.window_width - 200
		self.y0 = self.y0 - self.window_height - 200
		self.x1 = self.x1 - self.window_width - 200
		self.y1 = self.y1 - self.window_height - 200


		self.canvas.coords(self.aster, self.x0 - self.window_width - 200, self.y0 - self.window_height - 200, self.x1 - self.window_width - 200, self.y1 - self.window_height - 200)


		self.break_apart(x0, y0, x1, y1)


	def __init__(self, master, canvas, width, height, size = None, ship = None):
		super(asteroids, self).__init__()
		#this creates the asteroid object

		#this gives the object easily callable variables from anywhere without
		#needing to pass them...it also always one function to change the variable's value everywhere
		self.master = master
		self.canvas = canvas
		self.window_width = width
		self.window_height = height
		self.ship = ship

		#the size determines whether it is large, medium, or small
		self.size = size

		#this freezes the asteroid
		self.freeze = True

		#this is used to help make sure no asteroids are stuck on the edge of the screen
		self.count = 0

		#this draws the asteroid
		self.draw_asteroid(self.canvas, width, height)