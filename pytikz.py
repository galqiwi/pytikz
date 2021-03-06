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

	def midnode(self, begin = (0, 0), end = (1, 1), name = 'x', opt='black', nodeopt='midway, fill=white'):
		self.tex = self.tex + \
		'\\draw[' + opt + '] ' + str(begin) + ' -- ' + str(end) + ' node [' + str(nodeopt) + '] {' + str(name) + '};\n';

	def node(self, begin = (0, 0), name='O', opt='above'):
		self.tex = self.tex + \
		'\\draw[' + opt + '] node at ' + str(begin) + '  {' + str(name) + '};\n';


	def thick_node(self, begin = (0, 0), name='0', r=0.015, opt='above', opt_c='fill=black'):
		self.circle(begin, r, opt_c)
		self.node(begin, name, opt)

	def circle(self, begin = (0, 0), r=1, opt = 'black'):
		self.tex = self.tex + \
		'\\draw[' + opt + '] ' + str(begin) + ' circle (' + str(r) + ');\n'

	def print(self, file = open('fig.tex', 'w')):
		if not self.closed:
			self.close()
		print(self.tex, file=file)
