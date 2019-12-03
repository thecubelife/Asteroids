#asteroids.py
#asteroids game

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
#this imports the window class under which all other objects are created
from Window import Window


#this starts the whole game
#it creates the window class which everything is under
app = Window()

#this keeps the window open
#after everything runs and it is waiting for input from the user
app.root.mainloop()

#1,405 lines of code for this awesome game..this includes comments and white space