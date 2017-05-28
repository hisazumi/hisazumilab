# an exporter for kaken tex

from bibtex import read_bib, get_type_of_bib
from jinja2 import Environment, FileSystemLoader

# read bibtex
bib = read_bib('/Users/nel/GD/tex/nel.bib')

# mark myself
mes = ['Kenji Hisazumi', '久住憲嗣']


def mark_myself(ls):
    for e in ls:
        for me in mes:
            e['author'] = e['author'].replace(
                me, '\\underline{\\underline{' + me + '}}')
    return ls


# emit markdown
env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
tpl = env.get_template('pub-tmpl.tex')
md = tpl.render({'journals': mark_myself(get_type_of_bib(bib, 'article')),
                 'procs': mark_myself(get_type_of_bib(bib, 'inproceedings')),
                 'years': ['2017', '2016', '2015', '2014']})
print(md)
