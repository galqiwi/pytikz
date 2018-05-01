import math
from math import sin, cos, pi

class Tikzmaker:
	def __init__(self, scale = 1):
		self.tex = '\
		\\begin{figure}[h] \
		\centering \
		\\begin{tikzpicture}\n'
		self.closed = False
	def close(self):
		self.closed = True
		self.tex = self.tex + '\
		\\end{tikzpicture}\
		\end{figure}'
