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

	def freeze_text(self):
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
		self.text.place(relx = 2.0, rely = 2.0)
		self.text.config(state = tk.DISABLED)		

		self.start_Game2()

	def start_Game2(self):
		self.startgame.config(text = "Pause Game", width = 10,  command = partial(self.pause))
		self.startgame.place(relx = 0.5, rely = 0.0035)
		self.restarting_of_game()

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

		for i in self.asteroids:
			x0, y0, x1, y1 = i.get_coords()
			if (x0 >= 0 and x0 <= self.width) or (x1 >= 0 and x1 <= self.width):
				i.freeze = True


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

		for i in self.asteroids:
			x0, y0, x1, y1 = i.get_coords()
			if (x0 >= 0 and x0 <= self.width) or (x1 >= 0 and x1 <= self.width):
				i.freeze = False
				i.hold()

		self.freeze = False

	def start_of_game(self):
		#want 5 total asteroids for each of the 6...large....medium & small....small & small
		self.player = ship(self.canvas, self.width, self.height, master = self)
		
		self.make_asteroids()

		#get random number which decides which 6 asteroids to start with
		#loop through a list of different sized asteroids
		for i in range(6):
			x = self.get_random_size()
			if x == 1:
				for i in self.small_asteroids:
					if i.freeze == True:
						i.freeze = False
						break

			elif x == 2:
				for i in self.medium_asteroids:
					if i.freeze == True:
						i.freeze = False
						break

			else:
				for i in self.large_asteroids:
					if i.freeze == True:
						i.freeze = False
						break



		self.pro1 = Projectile(self.player, self.canvas, self.width, self.height, self.asteroids, self)
		self.pro2 = Projectile(self.player, self.canvas, self.width, self.height, self.asteroids, self)
		self.pro3 = Projectile(self.player, self.canvas, self.width, self.height, self.asteroids, self)
		self.pro4 = Projectile(self.player, self.canvas, self.width, self.height, self.asteroids, self)
		self.pro5 = Projectile(self.player, self.canvas, self.width, self.height, self.asteroids, self)
		self.pro6 = Projectile(self.player, self.canvas, self.width, self.height, self.asteroids, self)
		self.pro7 = Projectile(self.player, self.canvas, self.width, self.height, self.asteroids, self)
		self.pro8 = Projectile(self.player, self.canvas, self.width, self.height, self.asteroids, self)
		self.pro9 = Projectile(self.player, self.canvas, self.width, self.height, self.asteroids, self)
		self.pro10 = Projectile(self.player, self.canvas, self.width, self.height, self.asteroids, self)


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


		self.setup_bindings()


		for i in self.asteroids:
			i.hold()

	def make_asteroids(self):
		#get random number....random numbers choose the starting asteroids


		#5 large asteroids
		self.L1 = asteroids(self, self.canvas, self.width, self.height, size = 3, ship = self.player)
		self.L2 = asteroids(self, self.canvas, self.width, self.height, size = 3, ship = self.player)
		self.L3 = asteroids(self, self.canvas, self.width, self.height, size = 3, ship = self.player)
		self.L4 = asteroids(self, self.canvas, self.width, self.height, size = 3, ship = self.player)
		self.L5 = asteroids(self, self.canvas, self.width, self.height, size = 3, ship = self.player)


		self.large_asteroids = []
		self.large_asteroids.append(self.L1)
		self.large_asteroids.append(self.L2)
		self.large_asteroids.append(self.L3)
		self.large_asteroids.append(self.L4)
		self.large_asteroids.append(self.L5)

		#10 medium asteroids
		self.m1 = asteroids(self, self.canvas, self.width, self.height, size = 2, ship = self.player)
		self.m2 = asteroids(self, self.canvas, self.width, self.height, size = 2, ship = self.player)
		self.m3 = asteroids(self, self.canvas, self.width, self.height, size = 2, ship = self.player)
		self.m4 = asteroids(self, self.canvas, self.width, self.height, size = 2, ship = self.player)
		self.m5 = asteroids(self, self.canvas, self.width, self.height, size = 2, ship = self.player)
		self.m6 = asteroids(self, self.canvas, self.width, self.height, size = 2, ship = self.player)
		self.m7 = asteroids(self, self.canvas, self.width, self.height, size = 2, ship = self.player)
		self.m8 = asteroids(self, self.canvas, self.width, self.height, size = 2, ship = self.player)
		self.m9 = asteroids(self, self.canvas, self.width, self.height, size = 2, ship = self.player)
		self.m10 = asteroids(self, self.canvas, self.width, self.height, size = 2, ship = self.player)


		self.medium_asteroids = []
		self.medium_asteroids.append(self.m1)
		self.medium_asteroids.append(self.m2)
		self.medium_asteroids.append(self.m3)
		self.medium_asteroids.append(self.m4)
		self.medium_asteroids.append(self.m5)
		self.medium_asteroids.append(self.m6)
		self.medium_asteroids.append(self.m7)
		self.medium_asteroids.append(self.m8)
		self.medium_asteroids.append(self.m9)
		self.medium_asteroids.append(self.m10)


		#20 small asteroids
		self.s1 = asteroids(self, self.canvas, self.width, self.height, size = 1, ship = self.player)
		self.s2 = asteroids(self, self.canvas, self.width, self.height, size = 1, ship = self.player)
		self.s3 = asteroids(self, self.canvas, self.width, self.height, size = 1, ship = self.player)
		self.s4 = asteroids(self, self.canvas, self.width, self.height, size = 1, ship = self.player)
		self.s5 = asteroids(self, self.canvas, self.width, self.height, size = 1, ship = self.player)
		self.s6 = asteroids(self, self.canvas, self.width, self.height, size = 1, ship = self.player)
		self.s7 = asteroids(self, self.canvas, self.width, self.height, size = 1, ship = self.player)
		self.s8 = asteroids(self, self.canvas, self.width, self.height, size = 1, ship = self.player)
		self.s9 = asteroids(self, self.canvas, self.width, self.height, size = 1, ship = self.player)
		self.s10 = asteroids(self, self.canvas, self.width, self.height, size = 1, ship = self.player)
		self.s11 = asteroids(self, self.canvas, self.width, self.height, size = 1, ship = self.player)
		self.s12 = asteroids(self, self.canvas, self.width, self.height, size = 1, ship = self.player)
		self.s13 = asteroids(self, self.canvas, self.width, self.height, size = 1, ship = self.player)
		self.s14 = asteroids(self, self.canvas, self.width, self.height, size = 1, ship = self.player)
		self.s15 = asteroids(self, self.canvas, self.width, self.height, size = 1, ship = self.player)
		self.s16 = asteroids(self, self.canvas, self.width, self.height, size = 1, ship = self.player)
		self.s17 = asteroids(self, self.canvas, self.width, self.height, size = 1, ship = self.player)
		self.s18 = asteroids(self, self.canvas, self.width, self.height, size = 1, ship = self.player)
		self.s19 = asteroids(self, self.canvas, self.width, self.height, size = 1, ship = self.player)
		self.s20 = asteroids(self, self.canvas, self.width, self.height, size = 1, ship = self.player)


		self.small_asteroids = []
		self.small_asteroids.append(self.s1)
		self.small_asteroids.append(self.s2)
		self.small_asteroids.append(self.s3)
		self.small_asteroids.append(self.s4)
		self.small_asteroids.append(self.s5)
		self.small_asteroids.append(self.s6)
		self.small_asteroids.append(self.s7)
		self.small_asteroids.append(self.s8)
		self.small_asteroids.append(self.s9)
		self.small_asteroids.append(self.s10)
		self.small_asteroids.append(self.s11)
		self.small_asteroids.append(self.s12)
		self.small_asteroids.append(self.s13)
		self.small_asteroids.append(self.s14)
		self.small_asteroids.append(self.s15)
		self.small_asteroids.append(self.s16)
		self.small_asteroids.append(self.s17)
		self.small_asteroids.append(self.s18)
		self.small_asteroids.append(self.s19)
		self.small_asteroids.append(self.s20)

		#35 total asteroids
		self.asteroids = []
		for i  in self.large_asteroids:
			self.asteroids.append(i)
		for i in self.medium_asteroids:
			self.asteroids.append(i)
		for i in self.small_asteroids:
			self.asteroids.append(i)


	def restarting_of_game(self):
		self.freeze = False
		self.player.restart_ship()

		#get random number which decides which 6 asteroids to start with
		#loop through a list of different sized asteroids
		for i in range(6):
			x = self.get_random_size()
			if x == 1:
				for i in self.small_asteroids:
					if i.freeze == True:
						i.freeze = False
						break

			elif x == 2:
				for i in self.medium_asteroids:
					if i.freeze == True:
						i.freeze = False
						break

			else:
				for i in self.large_asteroids:
					if i.freeze == True:
						i.freeze = False
						break


		for i in self.asteroids:
			i.redraw_asteroid()
			i.hold()


	def get_random_size(self):
		x = random.randint(1, 3)
		return x

	def setup_bindings(self):
		self.root.bind('<KeyPress-Up>', partial(self.moveup, True))
		self.root.bind('<KeyRelease-Up>', partial(self.moveup, False))

		self.root.bind('<KeyPress-Left>', partial(self.rotateleft, True))
		self.root.bind('<KeyRelease-Left>', partial(self.rotateleft, False))

		self.root.bind('<KeyPress-Right>', partial(self.rotateright, True))
		self.root.bind('<KeyRelease-Right>', partial(self.rotateright, False))

		self.root.bind('<space>', self.fire_projectile)


	def moveup(self, mystate, event):
		d = 1
		self.player.move_ship(self.player, self.canvas, mystate, self.upcount, d)


	def rotateleft(self, turnstate, event):
		a = 0
		d = 1		#the direction
		self.player.rotate_ship(turnstate, self.turncount, direction = d)
		#player canvas d

	def rotateright(self, turnstate, event):
		a = 0
		d = -1 		#the direction
		self.player.rotate_ship(turnstate, self.turncount, direction = d)

	def fire_projectile(self, event):
		#check if they are frozen if so then use...otherwise don't and check next
		for i in self.projectiles:
			if self.freeze == False:
				if i.freeze == True:
					i.freeze = False
					i.ship_start()
					break


	#called after removing the objects from the screen
	def restart(self):
		#reset everything
		self.gameOver()
		self.restart_of_game()

	def restart2(self):
		self.win_game()
		self.restart_of_game()

	def make_text(self):
		self.text = tk.Text(self.root, height = 1)
		self.text.config(borderwidth = 0, background = "#000000", font = ("Helvetica", 48))
		self.text.config(foreground = "red")
		self.text.place(relx = 2.0, rely = 2.0)
		self.text.config(state = tk.NORMAL)

	def gameOver(self):
		self.freeze = True
		self.text.config(state = tk.NORMAL)

		self.text.delete("1.0", tk.END)
		self.text.insert(tk.INSERT, "GAME OVER")
		self.text.place(relx = 0.39, rely = 0.4)

		self.text.config(state = tk.DISABLED)

	def win_game(self):
		self.freeze = True
		self.text.config(state = tk.NORMAL)

		self.text.delete("1.0", tk.END)
		self.text.insert(tk.INSERT, "YOU WIN")
		self.text.place(relx = 0.43, rely = 0.4)

		self.text.config(state = tk.DISABLED)

	def __init__(self, master = None):
		super(Window, self).__init__()

		self.freeze = False

		self.root = tk.Tk()

		self.upcount = 0
		self.turncount = 0
		self.firecount = 0

		self.config_window()

		self.canvas = tk.Canvas(self.root, height = self.height, width = self.width, bg = "#000000")

		self.canvas.pack()

		self.make_text()

		self.idleGame()
