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



class Window:

	def config_window(self):
		self.root.title("Asteroids")
		self.root.config(bg = "#000000")
		margin = 10
		startx = margin/2
		starty = margin/2
		self.width = self.root.winfo_screenwidth() - (margin * 2)
		self.height = self.root.winfo_screenheight() - (margin * 8)
		self.root.geometry("{0}x{1}+{2}+{3}".format(self.width, self.height, int(startx), int(starty)))

	def config_text(self):
		self.text = tk.Text(self.root, height = 1)
		self.text.config(borderwidth = 0, background = "#000000", font = ("Helvetica", 48))
		self.text.place(relx = 0.39, rely = 0.4)

		self.text.tag_add("game_over", "1.0", "1.9")
		self.text.tag_config("game_over", background = "#000000", foreground = "red")
		self.text.config(state = tk.DISABLED)

	def idleGame(self):

		self.startgame = tk.Button(self.root, text = "StartGame", height = 2, width = 8)
		self.startgame.config(bg = "#FFFFFF", command = partial(self.startGame))
		self.startgame.place(relx = 0.5, rely = 0.5)
	
	def restart_of_game(self):
		#self.Text    delete it
		self.startgame.config(text = "Start Game", width = 10, command = partial(self.hold))
		self.startgame.place(relx = 0.5, rely = 0.5)

	def hold(self):
		self.text.config(state = tk.NORMAL)
		self.text.insert(tk.INSERT, "")
		self.text.config(state = tk.DISABLED)
		

		self.player = None
		self.a1 = None
		self.a2 = None
		self.a3 = None
		self.a4 = None
		self.a5 = None
		self.a6 = None

		self.startGame()

	def startGame(self):
		self.startgame.config(text = "Pause Game", width = 10,  command = partial(self.pause))
		self.startgame.place(relx = 0.5, rely = 0.0035)
		self.start_of_game()

	def idleRunning(self):
		self.startgame.config(text = "Pause Game", width = 10, command = partial(self.pause))
		self.startgame.place(relx = 0.5, rely = 0.0035)
		self.unfreeze_all()

	def pause(self):
		self.startgame.config(text = "Resume", width = 8, command = partial(self.idleRunning))
		self.startgame.place(relx = 0.5, rely = 0.5)
		self.freeze_all()

	def freeze_all(self):
		self.player.freeze = True
		self.a1.freeze = True
		self.a2.freeze = True
		self.a3.freeze = True
		self.a4.freeze = True
		self.a5.freeze = True
		self.a6.freeze = True
		self.pro1.freeze = True
		self.pro2.freeze = True
		self.pro3.freeze = True
		self.pro4.freeze = True
		self.pro5.freeze = True
		self.pro6.freeze = True
		self.pro7.freeze = True
		self.pro8.freeze = True
		self.pro9.freeze = True
		self.pro10.freeze = True

		self.freeze = True

	def unfreeze_all(self):
		self.player.freeze = False
		self.a1.freeze = False
		self.a2.freeze = False
		self.a3.freeze = False
		self.a4.freeze = False
		self.a5.freeze = False
		self.a6.freeze = False

		self.freeze = False

	def start_of_game(self):
		#want 5 total asteroids for each of the 6...large....medium & small....small & small
		self.player = ship(self.canvas, self.width, self.height, master = self)
		self.a1 = asteroids(self, self.canvas, self.width, self.height, self.player)
		self.a2 = asteroids(self, self.canvas, self.width, self.height, self.player)
		self.a3 = asteroids(self, self.canvas, self.width, self.height, self.player)
		self.a4 = asteroids(self, self.canvas, self.width, self.height, self.player)
		self.a5 = asteroids(self, self.canvas, self.width, self.height, self.player)
		self.a6 = asteroids(self, self.canvas, self.width, self.height, self.player)


		self.asteroids = []
		self.asteroids.append(self.a1)
		self.asteroids.append(self.a2)
		self.asteroids.append(self.a3)
		self.asteroids.append(self.a4)
		self.asteroids.append(self.a5)
		self.asteroids.append(self.a6)

		self.pro1 = Projectile(self.player, self.canvas, self.width, self.height, self.asteroids)
		self.pro2 = Projectile(self.player, self.canvas, self.width, self.height, self.asteroids)
		self.pro3 = Projectile(self.player, self.canvas, self.width, self.height, self.asteroids)
		self.pro4 = Projectile(self.player, self.canvas, self.width, self.height, self.asteroids)
		self.pro5 = Projectile(self.player, self.canvas, self.width, self.height, self.asteroids)
		self.pro6 = Projectile(self.player, self.canvas, self.width, self.height, self.asteroids)
		self.pro7 = Projectile(self.player, self.canvas, self.width, self.height, self.asteroids)
		self.pro8 = Projectile(self.player, self.canvas, self.width, self.height, self.asteroids)
		self.pro9 = Projectile(self.player, self.canvas, self.width, self.height, self.asteroids)
		self.pro10 = Projectile(self.player, self.canvas, self.width, self.height, self.asteroids)


		self.projectiles = []
		self.projectiles.append(self.pro1)
		self.projectiles.append(self.pro2)
		self.projectiles.append(self.pro3)
		self.projectiles.append(self.pro4)
		self.projectiles.append(self.pro5)
		self.projectiles.append(self.pro6)
		self.projectiles.append(self.pro7)
		self.projectiles.append(self.pro8)
		self.projectiles.append(self.pro9)
		self.projectiles.append(self.pro10)



		self.root.bind('<Up>', self.moveup)
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
		d = 1
		self.player.move_ship(self.player, self.canvas, d)

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
		#check if they are frozen if so then use...otherwise don't and check next
		for i in self.projectiles:
			if self.freeze == False:
				if i.freeze == True:
					i.freeze = False
					i.ship_start()
					break

	def restart(self):
		#reset everything
		self.gameOver()
		self.restart_of_game()

	def gameOver(self):
		self.text.config(state = tk.NORMAL)
		self.text.insert(tk.INSERT, "GAME OVER")
		self.text.config(state = tk.DISABLED)



	def __init__(self, master = None):
		super(Window, self).__init__()

		self.freeze = False

		self.root = tk.Tk()

		self.config_window()

		self.config_text()

		self.canvas = tk.Canvas(self.root, height = self.height, width = self.width, bg = "#000000")

		self.canvas.pack()

		self.idleGame()
