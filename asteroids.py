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


#bug....can't rotate and go forward at the same time

#some asteroids still starting off screen
#possibly fixed

#bug....backwards is sort of buggy

#bug when going outside of screen...specifically through the bottom
#side and up work....a little weird because ship just appears




#game over is below the canvas and you cannot see it
