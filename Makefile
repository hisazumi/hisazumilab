HEXO=hexo
BIB=$(HOME)/Documents/tex/nel.bib

all:

source/_posts/Publications.md: bibtex2md.py $(BIB)
	python3 bibtex2md.py > source/_posts/Publications.md

server: source/_posts/Publications.md
	$(HEXO) server

deploy: source/_posts/Publications.md
	hexo generate
	$(HEXO) deploy 

