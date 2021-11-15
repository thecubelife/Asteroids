This is a remake of the original game Asteroids by Stephen Chase Robinson
for my Fall 2019 Intro to Programming Project

To run this file you will need:

	- Python 2 or later
	- the time library
			which always the use of sleep
	- the functools library
			which allows me to set a command for the buttons and pass parameters with the commands
	- the math library
			which is used for its trigonometry functions
	- the random library
			which is used for getting random numbers...to make the program less predictive
These libraries should come standard with python 3 or greater

Then you will need each of the code's own libraries inlcuding:
	- asteroids.py
		which is the game itself
	- Window.py
		which houses the window and is the parent object of all objects
	-  ship.py
		which is the class for creating the ship and its movement
	- asteroids_class.py
		which houses the asteroid objects and their methods
	- projectile.py
		which holds the objects which are fired from the ship
	- init.py
		this is an empty file but it allows the libraries to be used in another program
These libraries will need to be in the same folder


To run the program simply use either IDLE or any other command window to open asteroids.py
	For example in Git Bash, once in the directory of the file this would be........ python asteroids.py
Another alternative would be to just double click the location of asteroids.py within your folder directories...just make sure you are opening it with python and not another program.
