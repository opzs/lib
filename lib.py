# Library


import time
import msvcrt


def capitalize(txt):
	""" Capitalize The First Letter Of The Given Word(s) """


	txt = txt.split()

	for word in txt:
		a = list(word)

		a[0] = a[0].upper()

		txt[txt.index(word)] = "".join(a)

	return " ".join(txt)


def spinner(anim=0, interval=.1, loops=100):
	"""
	Spinner/Loading Animation
	Returns a list with all the animation sets.

	Parameters:
	anim - The index of the animation set.
	interval - The interval between each frame.
	loops - The amount of times to loop a spinner.
	"""


	anims = [
		[
			"-",
			"/",
			"|",
			"\\"      
		],
		[
			"-  ",
			" - ",
			"  -",
			"  -",
			" - ",
			"-  "     
		],
		[
			"{",
			"(",
			"|",
			")",
			"}",
			")",
			"|",
			"("
		],
		[
			"👈",
			"👇",
			"👉",
			"👆"
		],
		[
			"Loading   ",
			"Loading.  ",
			"Loading.. ",
			"Loading...",
		]
	]

	loop = anims[anim]

	for i in range(loops):
		for x in range(0, len(loop)):
			print(loop[x], end="\r")
			time.sleep(interval)


def menu(options, msg_start="Selected: [ ", msg_end=" ]", selected_start="You have selected [ ", selected_end=" ]."):
	"""
	Selection Menu
	Returns the selected option.

	Parameters:
	options - A list of options to choose from.
	msg - The message shown before showing the currently selected option.
	selected_start - The message shown before showing the selected option.
	selected_end - The message shown after showing the selected option.
	"""


	if list(options) != options:
		err = "\"opt\" must be a list"

		raise ValueError(err)
	elif len(options) == 0:
		err = "List \"opt\" is empty"

		raise ValueError(err)
	
	if str(msg_start) != msg_start:
		err = "\"msg_start\" must be a string"

		raise ValueError(err)

	if str(msg_end) != msg_end:
		err = "\"msg_end\" must be a string"

		raise ValueError(err)

	if str(selected_start) != selected_start:
		err = "\"selected_start\" must be a string"

		raise ValueError(err)

	if str(selected_end) != selected_end:
		err = "\"selected_end\" must be a string"

		raise ValueError(err)
		

	opt = []

	for option in options:
		opt.append(str(option))


	selected = 0

	print("Options: " + ", ".join(opt))

	menu = True

	print(f"{msg_start}{opt[selected]}{msg_end}", end="\r")

	while menu:
		key = msvcrt.ord(msvcrt.getch())

		if key == 39: # Right Arrow Key
			selected += 1

			if selected > len(opt) - 1:
				selected = 0

			print(f"{msg_start}{opt[selected]}{msg_end}" + " " * 100, end="\r")
		elif key == 37: # Left Arrow Key
			selected -= 1

			if selected < 0:
				selected = len(opt) - 1

			print(f"{msg_start}{opt[selected]}{msg_end}" + " " * 100, end="\r")
		elif key == 13: # Enter Key
			menu = False

			print(selected_start + opt[selected]  + selected_end + " " * 100)


	return options[selected]


class Grid:
	"""
	A Grid (A Nested List)

	Parameters:
	x - The size of the grid by X.
	y - The size of the grid by Y.
	blank - The empty spaces in a grid.
	fill - The filled spaces in a grid.

	Variables:
	raw - The raw nested list.
	blank - The empty spaces in a grid.
	fill - The filled spaces in a grid.
	size - A tuple of the X and Y parameters.
	"""


	def __init__(self, x=7, y=7, blank="░░", fill="██"):
		raw = []
		tmp = []

		for i in range(y):
			for j in range(x):
				tmp.append(blank)

			raw.append(tmp)
			tmp = []


		self.raw = raw
		self.fill = fill
		self.blank = blank
		self.size = (x, y)



	def grid(self):
		"""
		Get the grid as a string.
		"""


		result = ""

		for y in self.raw:
			tmp = "".join(y)
			result += tmp + "\n"

		return result


	def draw(self, x, y, pxl="██"):
		"""
		Draw a pixel.

		Parameters:
		x - The position of X of where you want to draw.
		y - The position of Y of where you want to draw.
		pxl - The pixel that will be drawn.
		"""


		self.raw[y][x] = self.fill

	
	def erase(self, x, y):
		"""
		Erase a pixel.

		Parameters:
		x - The position of X of where you want to erase.
		y - The position of Y of where you want to erase.
		"""


		self.raw[y][x] = self.blank

	
	def get(self, x, y):
		"""
		Get a pixel.

		Parameters:
		x - The position of X of the pixel you want to get.
		y - The position of Y of the pixel you want to get.
		"""


		return self.raw[y][x]
