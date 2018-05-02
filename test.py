from pytikz import Tikzmaker
import math
from math import sin, cos, pi, sqrt

def sind(x):
	return sin(x/180*pi)
def cosd(x):
	return cos(x/180*pi)

r = 1/3

maker = Tikzmaker(4)

maker.circle((0, 0), 1, 'yscale=0.5')
maker.circle((0, 0), 1)

p0 = ()
p1 = ()
p2 = ()



maker.print()