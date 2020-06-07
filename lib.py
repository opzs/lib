import os, time
	
def capitalize(word):
	capitalized = ''
	for x in word.split():
		l = list(x)
		capitalized += l[0].upper()
		l.pop(0)
		capitalized += ''.join(l) + ' '
	return capitalized
	
def timer(h=0, m=0, s=10, end=''):
	while True:
		s -= 1
		if s < 0:
			m -= 1
			s = 59
			if m < 0:
				h -= 1
				m = 59
				if h < 0:
					print('\n' + end)
					break
				else:
					print(h, 'hours', m, 'minutes', s, 'seconds', end='\r')
			else:
				print(h, 'hours', m, 'minutes', s, 'seconds', end='\r')
		else:
			print(h, 'hours', m, 'minutes', s, 'seconds', end='\r')
		time.sleep(1)
		
def spinner(txt='', endtxt='', loops=5, delay=.1, set=0):
	sets = [
		[
			'\\',
			'|',
			'/',
			'—'
		],
		[
			',',
			'·',
			'\'',
			'·'
		],
		[
			'👈',
			'👇',
			'👉',
			'👆'
		]
	]

	for loop in range(loops):
		for spinner in sets[set]:
			print(txt + spinner + endtxt, end='\r')
			time.sleep(delay)
	
