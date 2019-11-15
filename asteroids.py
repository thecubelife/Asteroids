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



#how to get mouse motion
"""root.bind('<Motion>', motion)
		def motion(event):
"""