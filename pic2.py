from pytikz import Tikzmaker
import math
from math import sin, cos, pi

def sind(x):
	return sin(x/180*pi)
def cosd(x):
	return cos(x/180*pi)

maker = Tikzmaker(4)

maker.circle((0, 0), 1,'thick')

alp = 40

r = 1 / cosd(alp)

a0 = 55
old = (cosd(a0), sind(a0))
for i in range(0, 2):
	new = (cosd(a0 + (1 + 2 * i) * alp) * r, sind(a0 + (1 + 2 * i) * alp) * r)
	maker.line(old, new, 'red, thick')
	old = new

maker.line(old, (-1, 0), 'red, thick')

old = (cosd(a0), sind(a0))
for i in range(0, 2):
	new = (cosd(a0 + (1 + 2 * i) * alp) * r, sind(a0 + (1 + 2 * i) * alp) * r)
	maker.circle(new, 0.03, 'fill=black')
	maker.node(new, '$S_' + str(i) + '$', 'above')
	old = new

new = (cosd(a0), sind(a0))

maker.circle(new, 0.03, 'fill=black')
maker.node(new, 'Q', 'above right')

new = (-1, 0)

maker.circle(new, 0.03, 'fill=black')
maker.node(new, '$P$', 'below right')

new = (0, 0)

maker.circle(new, 0.03, 'fill=black')
maker.node(new, '$O$', 'right')

maker.line((0, 0), (-1, 0), 'thick')
maker.line((0, 0), (cosd(a0), sind(a0)),'thick')
maker.line((0, 0), (cosd(a0 + alp) * r, sind(a0 + alp) * r),'thick')
maker.line((0, 0), (cosd(a0 + alp * 3) * r, sind(a0 + alp * 3) * r),'thick')

maker.print()