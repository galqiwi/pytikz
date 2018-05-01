test:
	python3 test.py

tex:
	pdflatex main.tex

png:
	convert -density 1000 main.pdf -quality 100 output.jpeg