test:
	python3 test.py

tex:
	pdflatex main.tex

png:
	convert -density 1000 main.pdf -quality 100 output.jpeg

clean:
	rm -f {main,head,fig,main}.{aux,log,out} fig.tex
	rm -rf __pycache__
	rm main.synctex.gz
