#asteroids.py
#asteroids game

try:
	import tkinter as tk
except ImportError:
	import Tkinter as tk
import time
import math
import random
#this is used to pass arguments to a button command which could not be done otherwise
from functools import partial
from Window import Window



#put loop in here for restarting it over and over again
app = Window()

app.root.mainloop()


#bug....can do all three inputs at once....but works best when you hold down the forward key 
#the whole time and add other keys



#restart is still buggy

#game over is below the canvas and you cannot see it
