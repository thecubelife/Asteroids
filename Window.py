#Window.py
#Window Class

try:
	import tkinter as tk
except ImportError:
	import Tkinter as tk
import time
import math
import random
#this is used to pass arguments to a button command which could not be done otherwise
from functools import partial

from ship import ship
from asteroids_class import asteroids
from projectile import Projectile



class Window(tk.Frame):

	def config_window(self):
		self.root.title("Asteroids")
		self.root.config(bg = "#000000")
		margin = 10
		startx = margin/2
		starty = margin/2
		self.width = self.root.winfo_screenwidth() - (margin * 2)
		self.height = self.root.winfo_screenheight() - (margin * 8)
		self.root.geometry("{0}x{1}+{2}+{3}".format(self.width, self.height, int(startx), int(starty)))


	def idleGame(self):

		self.startgame = tk.Button(self.root, text = "StartGame", height = 2, width = 8)
		self.startgame.config(bg = "#FFFFFF", command = partial(self.startGame))
		self.startgame.place(relx = 0.5, rely = 0.5)
		

	def startGame(self):
		self.startgame.config(text = "Pause Game", width = 10,  command = partial(self.pause))
		self.startgame.place(relx = 0.5, rely = 0.0035)
		self.start_of_game()

	def idleRunning(self):
		self.startgame.config(text = "Pause Game", width = 10, command = partial(self.pause))
		self.startgame.place(relx = 0.5, rely = 0.0035)


	def pause(self):
		self.startgame.config(text = "Resume", width = 8, command = partial(self.idleRunning))
		self.startgame.place(relx = 0.5, rely = 0.5)



	def start_of_game(self):

		self.player = ship(self.canvas, self.width, self.height)
		self.a1 = asteroids(self.canvas, self.width, self.height, self.player)
		self.a2 = asteroids(self.canvas, self.width, self.height, self.player)
		self.a3 = asteroids(self.canvas, self.width, self.height, self.player)
		self.a4 = asteroids(self.canvas, self.width, self.height, self.player)
		self.a5 = asteroids(self.canvas, self.width, self.height, self.player)
		self.a6 = asteroids(self.canvas, self.width, self.height, self.player)

		self.pro1 = None
		self.pro2 = None
		self.pro3 = None
		self.pro4 = None
		self.pro5 = None
		self.pro6 = None
		self.pro7 = None
		self.pro8 = None
		self.pro9 = None
		self.pro10 = None

		self.asteroids = []
		self.asteroids.append(self.a1)
		self.asteroids.append(self.a2)
		self.asteroids.append(self.a3)
		self.asteroids.append(self.a4)
		self.asteroids.append(self.a5)
		self.asteroids.append(self.a6)

		self.root.bind('<Up>', self.moveup)
		self.root.bind('<Down>', self.movedown)
		self.root.bind('<Left>', self.rotateleft)
		self.root.bind('<Right>', self.rotateright)
		self.root.bind('<space>', self.fire_projectile)

		self.a1.hold(self.a1)
		self.a2.hold(self.a2)
		self.a3.hold(self.a3)
		self.a4.hold(self.a4)
		self.a5.hold(self.a5)
		self.a6.hold(self.a6)



	def moveup(self, event):
		x = 0
		y = -1
		self.player.move_ship(self.player, self.canvas, x, y)

	def movedown(self, event):
		x = 0
		y = 1
		self.player.move_ship(self.player, self.canvas, x, y)

	def rotateleft(self, event):
		a = 0
		d = 1		#the direction
		self.player.rotate_ship(direction = d)
		#player canvas d

	def rotateright(self, event):
		a = 0
		d = -1 		#the direction
		self.player.rotate_ship(direction = d)


	def fire_projectile(self, event):
		if self.pro1 == None:
			self.pro1 = Projectile(self.player, self.canvas, self.width, self.height) #also have to get x, y direction
			return
		elif self.pro2 == None:
			self.pro2 = Projectile(self.player, self.canvas, self.width, self.height) #also have to get x, y direction
			return
		elif self.pro3 == None:
			self.pro3 = Projectile(self.player, self.canvas, self.width, self.height) #also have to get x, y direction
			return
		elif self.pro4 == None:
			self.pro4 = Projectile(self.player, self.canvas, self.width, self.height) #also have to get x, y direction
			return
		elif self.pro5 == None:
			self.pro5 = Projectile(self.player, self.canvas, self.width, self.height) #also have to get x, y direction
			return
		elif self.pro6 == None:
			self.pro6 = Projectile(self.player, self.canvas, self.width, self.height) #also have to get x, y direction
			return
		elif self.pro7 == None:
			self.pro7 = Projectile(self.player, self.canvas, self.width, self.height) #also have to get x, y direction
			return
		elif self.pro8 == None:
			self.pro8 = Projectile(self.player, self.canvas, self.width, self.height) #also have to get x, y direction
			return
		elif self.pro9 == None:
			self.pro9 = Projectile(self.player, self.canvas, self.width, self.height) #also have to get x, y direction
			return
		elif self.pro10 == None:
			self.pro10 = Projectile(self.player, self.canvas, self.width, self.height) #also have to get x, y direction
			return
			




	def __init__(self, master = None):
		super(Window, self).__init__()

		self.root = tk.Tk()

		self.config_window()

		self.canvas = tk.Canvas(self.root, height = self.height, width = self.width, bg = "#000000")

		self.canvas.pack()

		self.idleGame()
