# Library

import time, random, msvcrt, os

def capitalize(word):
	word = list(word)
	word[0] = word[0].upper()
	return ''.join(word)

def spinner(anim=0, speed=.1, loops=100, reverse=False):
	anims = [
		[
			'-',
			'/',
			'|',
			'\\'      
		],
		[
			'-  ',
			' - ',
			'  -',
			'  -',
			' - ',
			'-  '     
		],
		[
			'{',
			'(',
			'|',
			')',
			'}',
			')',
			'|',
			'('
		],
		[
			'👈',
			'👇',
			'👉',
			'👆'
		]
	]

	loop = anims[anim]
	if reverse == False:
		for i in range(loops):
			for x in range(0, len(loop)):
				print(loop[x], end='\r')
				time.sleep(speed)
		else:
			for i in range(0, len(loop)):
				for x in range(len(loop)-1, 0, -1):
					print(loop[x], end='\r')
					time.sleep(speed)

def selection(opt):
	selected = 0
	print('Options:\n' + ', '.join(opt))
	menu = True
	while menu:
		key = msvcrt.getch()
		if key == b'P': # if down arrow
			selected += 1
			if selected > len(opt) - 1:
				selected = 0
			print('[' + opt[selected] + ']' + ' ' * 100, end='\r')
		if key == b'H': # if up arrow
			selected -= 1
			if selected < 0:
				selected = len(opt) - 1
			print('[' + opt[selected] + ']' + ' ' * 100, end='\r')
		if key == b'\x1b': # if esc
			exit()
		if key == b'\r': # if enter
			menu = False
			for x in range(20):
				print('You have selected ' + opt[selected] + ' ' * 100, end='\r')
				time.sleep(1)
