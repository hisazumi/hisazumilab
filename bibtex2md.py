# an exporter for hexo

from bibtex import read_bib, get_type_of_bib
from jinja2 import Environment, FileSystemLoader

# read bibtex
bib = read_bib('/Users/nel/GD/tex/nel.bib')

# emit markdown
env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
tpl = env.get_template('pub-tmpl.md')
md = tpl.render({'journals': get_type_of_bib(bib, 'article'),
                 'procs': get_type_of_bib(bib, 'inproceedings')})
print(md)
