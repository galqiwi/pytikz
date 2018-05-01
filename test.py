from pytikz import Tikzmaker
import math
from math import sin, cos, pi

def sind(x):
	return sin(x/180*pi)
def cosd(x):
	return cos(x/180*pi)

maker = Tikzmaker(4)

maker.print()