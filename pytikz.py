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
	def line(self, begin = (0, 0), end = (1, 1)):
		self.tex = self.tex + \
		'\\draw ' + str(begin) + ' -- ' + str(end) + ';\n';
		
	def print(self, file = open('fig.tex', 'w')):
		if not self.closed:
			self.close()
		print(self.tex, file=file)
