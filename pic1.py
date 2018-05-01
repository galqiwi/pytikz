from pytikz import Tikzmaker
import math
from math import sin, cos, pi

n = 10
maker = Tikzmaker(1)

map = [[(i > k) for i in range(0, n)] for k in range(0, n)]

#map[4][4] = True

def valid(x):
	return x >= 0 and x < n

for x in range(0, n):
	for y in range(0, n):
		if not map[x][y]:
			continue
		maker.circle((x, y), 0.03, 'fill=black')
		if (valid(x + 1)):
			if map[x+1][y]:
				maker.line((x + 0.1, y), (x + 0.9, y))
			else:
				maker.line_crossed((x + 0.1, y), (x + 0.9, y))

		if (valid(y - 1)):
			if (map[x][y-1]):
				maker.line((x, y - 0.1), (x, y - 0.9))
			else:
				maker.line_crossed((x, y - 0.1), (x, y - 0.9))

maker.print()