#!/usr/bin/python

from jinja2 import Template
from bibtex import read_bib, get_type_of_bib

bib = read_bib('/Users/nel/GD/tex/nel.bib')


def format_ym(e):
    if 'month' in e:
        return "'" + e['year'] + '-' + "{0:0>2}".format(e['month']) + '-01'
    else:
        return "'" + e['year'] + '-04-01'


journals = get_type_of_bib(bib, 'article')
procs = get_type_of_bib(bib, 'inproceedings')

tmpl = ",,{{e['title']}},,,,\"{{e['author']}}\""
tmpl += ",,,,,{{e['refs']}},{{e['ym']}}, 3"
template = Template(tmpl)

for e in journals:
    e['ym'] = format_ym(e)
    print(template.render(e=e))

print('\n')

for e in procs:
    e['ym'] = format_ym(e)
    print(template.render(e=e))
