#!/usr/bin/python

import sys
import csv
from bibtex import read_bib, get_type_of_bib


bib = read_bib('/Users/nel/GD/tex/nel.bib')

journals = get_type_of_bib(bib, 'article')
procs = get_type_of_bib(bib, 'inproceedings')

w = csv.DictWriter(sys.stdout, fieldnames=['author', 'title', 'refs', 'year'])
w.writeheader()
for e in journals:
    w.writerow(e)
for e in procs:
    w.writerow(e)
