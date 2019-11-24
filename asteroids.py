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


#bug some asteroids still start off screen and bounc against wall


#bug....can't rotate and go forward at the same time



#bug....backwards is sort of buggy

#bug when going outside of screen...specifically through the bottom

#bug can't fire more than 10 times
#removes projectiles and asteroids from the screen, but doesn't remove them from the game...ie..ship still dies



#bug deletes game over and then glitches and ends the game again
#game over stays on the screen
#may be fixed....unsure...it's not, but for some reason it worked once
