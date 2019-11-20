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

app = Window()

app.root.mainloop()



#bug....can't rotate and go forward at the same time
#when trying to do above sometime the ship rapidly changes position by rotating and moving forward in an instance


#bug....can't go forwards...once ship is rotated 180 degrees
#bug....can't go backwards