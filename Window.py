#Window.py
#Window Class

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

#this imports all the other classes that create the other objects
from ship import ship
from asteroids_class import asteroids
from projectile import Projectile


#this is the class that creates the window
#it also is the parent of every other object
class Window:

	def config_window(self):
		#this sets all the settings for the window itself
		self.root.title("Asteroids")
		self.root.config(bg = "#000000")
		margin = 10
		startx = margin/2
		starty = margin/2
		self.width = self.root.winfo_screenwidth() - (margin * 2)
		self.height = self.root.winfo_screenheight() - (margin * 8)
		self.root.geometry("{0}x{1}+{2}+{3}".format(self.width, self.height, int(startx), int(starty)))

	def fire_projectile(self, event):
		#this is called by the space bar
		#check if they are frozen if so then use...otherwise don't and check next
		for i in self.projectiles:
			if self.freeze == False:
				if i.freeze == True:
					i.freeze = False
					i.ship_start()
					break

	def freeze_all(self):
		#this freezes everything...primarily used for pausing the game
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

	def gameOver(self):
		#this replaces the text with "GAME OVER" and places it near the center of the screen
		self.freeze = True
		self.text.config(state = tk.NORMAL)

		self.text.delete("1.0", tk.END)
		self.text.insert(tk.INSERT, "GAME OVER")
		self.text.place(relx = 0.39, rely = 0.4)

		self.text.config(state = tk.DISABLED)
	
	def get_random_size(self):
		#gets a random size for the asteroids
		x = random.randint(1, 3)
		return x

	def hold(self):
		#this moves the text off screen when it is not needed
		
		self.text.config(state = tk.NORMAL)
		self.text.place(relx = 2.0, rely = 2.0)
		self.text.config(state = tk.DISABLED)		

		#this restarts the game
		self.start_Game2()

	def idleGame(self):
		#this creates a button and then gives it a command to execute when pressed
		#in this case...startGame
		self.startgame = tk.Button(self.root, text = "StartGame", height = 2, width = 8)
		self.startgame.config(bg = "#FFFFFF", command = partial(self.startGame))
		self.startgame.place(relx = 0.5, rely = 0.5)
	
	def idleRunning(self):
		#this reconfigures the button to say pause game, and reconfigures it to execute
		#pause()
		self.startgame.config(text = "Pause Game", width = 10, command = partial(self.pause))
		self.startgame.place(relx = 0.5, rely = 0.0035)

		#this unfreezes the game, ship, and certain asteroids
		self.unfreeze_all()

	def make_asteroids(self):
		#this makes all the asteroids that may be needed
		#it also appends them to a list for each size
		#and a list holding all asteroids


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

	def make_text(self):
		#this makes the text widget initially and moves it off the screen 
		#until it is needed
		self.text = tk.Text(self.root, height = 1)
		self.text.config(borderwidth = 0, background = "#000000", font = ("Helvetica", 48))
		self.text.config(foreground = "red")
		self.text.place(relx = 2.0, rely = 2.0)
		self.text.config(state = tk.NORMAL)

	def moveup(self, mystate, event):
		#this is called by the up arrow and it calls the ships move_ship() method
		d = 1
		self.player.move_ship(self.player, self.canvas, mystate, self.upcount, d)

	def pause(self):
		#this reconfigures the button to say "resume", and sets the command to idleRunning()
		self.startgame.config(text = "Resume", width = 8, command = partial(self.idleRunning))
		self.startgame.place(relx = 0.5, rely = 0.5)

		#this freezes everything and stops it from moving
		self.freeze_all()

	def restart(self):

		#this reconfigures the text for game over
		self.gameOver()

		#this reconfigures the button for a restart
		self.restart_of_game()

	def restart2(self):

		#this reconfigures the text for win game
		self.win_game()

		#this reconfigures the button for a restart
		self.restart_of_game()

	def restart_of_game(self):
		#this reconfigures the button's text to "start game", and sets the command to hold() 
		self.startgame.config(text = "Start Game", width = 10, command = partial(self.hold))
		self.startgame.place(relx = 0.5, rely = 0.5)

	def restarting_of_game(self):
		#this restarts the game by unfreezing the window and ship and 
		#choosing 6 random asteroids to start
		self.freeze = False
		self.player.restart_ship()

		#get random number which decides which 6 asteroids to start with
		#loop through a list of different sized asteroids
		for i in range(6):
			#this random number decides what size to get
			x = self.get_random_size()
			if x == 1:
				for i in self.small_asteroids:
					if i.freeze == True:
						#if it is frozen then unfreeze it and break from the loop for the next asteroid
						i.freeze = False
						break

			elif x == 2:
				for i in self.medium_asteroids:
					if i.freeze == True:
						#if it is frozen then unfreeze it and break from the loop for the next asteroid
						i.freeze = False
						break

			else:
				for i in self.large_asteroids:
					if i.freeze == True:
						#if it is frozen then unfreeze it and break from the loop for the next asteroid
						i.freeze = False
						break


		for i in self.asteroids:
			#gets all the asteroids that are not frozen
			#redraws them on the screen and starts their movement loops
			i.redraw_asteroid()
			i.hold()

	def rotateleft(self, turnstate, event):
		#called by the left button
		a = 0
		d = 1		#the direction
		self.player.rotate_ship(turnstate, self.turncount, direction = d)

	def rotateright(self, turnstate, event):
		#called by the right button
		a = 0
		d = -1 		#the direction
		self.player.rotate_ship(turnstate, self.turncount, direction = d)

	def setup_bindings(self):
		#this sets up all the key event's bindings and gives them commands to execute when called

		self.root.bind('<KeyPress-Up>', partial(self.moveup, True))
		self.root.bind('<KeyRelease-Up>', partial(self.moveup, False))

		self.root.bind('<KeyPress-Left>', partial(self.rotateleft, True))
		self.root.bind('<KeyRelease-Left>', partial(self.rotateleft, False))

		self.root.bind('<KeyPress-Right>', partial(self.rotateright, True))
		self.root.bind('<KeyRelease-Right>', partial(self.rotateright, False))

		self.root.bind('<space>', self.fire_projectile)

	def start_Game2(self):
		#this reconfigures the button to say "pause game", and sets the command to pause()
		self.startgame.config(text = "Pause Game", width = 10,  command = partial(self.pause))
		self.startgame.place(relx = 0.5, rely = 0.0035)

		#this restarts the game..unfreezing the ship and certain asteroids
		self.restarting_of_game()

	def start_of_game(self):
		#this is the start of the game

		#this creates the player object
		self.player = ship(self.canvas, self.width, self.height, master = self)
		
		#this starts the creation of all asteroids
		self.make_asteroids()

		#get random number which decides which 6 asteroids to start with
		#loop through a list of different sized asteroids
		for i in range(6):
			x = self.get_random_size()
			if x == 1:
				for i in self.small_asteroids:
					#if it is frozen then unfreeze it and break from the loop for the next asteroid
					if i.freeze == True:
						i.freeze = False
						break

			elif x == 2:
				for i in self.medium_asteroids:
					if i.freeze == True:
						#if it is frozen then unfreeze it and break from the loop for the next asteroid
						i.freeze = False
						break

			else:
				for i in self.large_asteroids:
					if i.freeze == True:
						#if it is frozen then unfreeze it and break from the loop for the next asteroid
						i.freeze = False
						break


		#this creates all the projectiles
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

		#this creates a list of all the projectiles
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

		#this calls the setup_bindings() method
		self.setup_bindings()

		#this starts the asteroids movement loop
		for i in self.asteroids:
			i.hold()

	def startGame(self):
		#this reconfigures the button text to say "pause game", and sets the command to pause()
		self.startgame.config(text = "Pause Game", width = 10,  command = partial(self.pause))
		self.startgame.place(relx = 0.5, rely = 0.0035)

		#this starts the game
		self.start_of_game()

	def unfreeze_all(self):
		#this unfreezes everything needed

		#this unfreezes the player
		self.player.freeze = False

		#this unfreezes only the asteroids on the screen and restarts their movement loop
		for i in self.asteroids:
			x0, y0, x1, y1 = i.get_coords()
			if (x0 >= 0 and x0 <= self.width) or (x1 >= 0 and x1 <= self.width):
				i.freeze = False
				i.hold()
		#this unfreezes the window
		self.freeze = False

	def win_game(self):
		#this sets the "YOU WIN" text and moves it near the middle of the screen
		
		#this freezes the window
		self.freeze = True
		self.text.config(state = tk.NORMAL)

		self.text.delete("1.0", tk.END)
		self.text.insert(tk.INSERT, "YOU WIN")
		self.text.place(relx = 0.43, rely = 0.4)

		self.text.config(state = tk.DISABLED)


	def __init__(self, master = None):
		super(Window, self).__init__()



		#this gives the object easily callable variables from anywhere without
		#needing to pass them...it also always one function to change the variable's value everywhere
		self.freeze = False

		#this creates the window itself
		self.root = tk.Tk()

		self.upcount = 0
		self.turncount = 0
		self.firecount = 0

		#this configures the window to look correct
		self.config_window()

		#this creates the canvas which everything is drawn onto
		self.canvas = tk.Canvas(self.root, height = self.height, width = self.width, bg = "#000000")

		#this makes the canvas take up the whole screen
		self.canvas.pack()

		#this makes the text widget after the canvas widget so that the text is on top
		#within here it also moves it off the screen as well
		self.make_text()

		#this calls the idleGame() method which creates the start button
		self.idleGame()