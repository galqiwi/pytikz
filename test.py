from pytikz import Tikzmaker
import math
from math import sin, cos, pi

n = 1000
maker = Tikzmaker()
for i in range(0, n):
	maker.line((cos(i/n*pi), sin(i/n*pi)), (cos((i+1)/n*pi), sin((i+1)/n*pi)))
maker.print()