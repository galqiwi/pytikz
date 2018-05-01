from pytikz import Tikzmaker
import math
from math import sin, cos, pi

def sind(x):
	return sin(x/180*pi)
def cosd(x):
	return cos(x/180*pi)

maker = Tikzmaker(4)

maker.thick_node((0, 0), 'S')
maker.thick_node((1, 0), 'R')
maker.thick_node((0.5, 0), 'M')

maker.line((0, 0), (0.5, 0), '->')
maker.line((1, 0), (0.5, 0), '->')

maker.node((0.25, 0), '10')
maker.node((0.75, 0), '10')

maker.print()