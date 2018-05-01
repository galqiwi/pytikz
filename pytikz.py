import math
from math import sin, cos, pi

class Tikzmaker:
	def __init__(self, scale = 1):
		self.tex = '\
		\\begin{figure}[h] \
		\centering \
		\\begin{tikzpicture}[scale=' + str(scale) + ']\n'
		self.closed = False
	def close(self):
		self.closed = True
		self.tex = self.tex + '\
		\\end{tikzpicture}\
		\end{figure}'
	def line(self, begin = (0, 0), end = (1, 1), opt='black'):
		self.tex = self.tex + \
		'\\draw[' + opt + '] ' + str(begin) + ' -- ' + str(end) + ';\n';

	def line_crossed(self, begin = (0, 0), end = (1, 1), opt='black'):
		self.tex = self.tex + \
		'\\draw[' + opt + '] ' + str(begin) + ' -- ' + str(end) + ' node [midway, fill=white] {x};\n';

	def node(self, begin = (0, 0), name='O', opt='black'):
		self.tex = self.tex + \
		'\\draw[' + opt + '] node at ' + str(begin) + '  {' + str(name) + '};\n';
	def circle(self, begin = (0, 0), r=1, opt = 'black'):
		self.tex = self.tex + \
		'\\draw[' + opt + '] ' + str(begin) + ' circle (' + str(r) + ');'
	def print(self, file = open('fig.tex', 'w')):
		if not self.closed:
			self.close()
		print(self.tex, file=file)
