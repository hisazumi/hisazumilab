HPATH=$(HOME)/Documents/Web
HEXO=$(HPATH)/node_modules/hexo/bin/hexo
BIB=$(HOME)/Documents/tex/nel.bib

bib: bibtex2md.py
	python3 bibtex2md.py > source/_posts/Publications.md

server: bib
	$(HEXO) server

deploy: bib
	$(HEXO) deploy 

