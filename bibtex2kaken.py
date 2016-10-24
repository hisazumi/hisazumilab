# an exporter for hexo

import datetime
import bibtexparser
import unicodedata
import re

# some utilities

def is_japanese(string):
    for ch in string:
        name = unicodedata.name(ch) 
        if "CJK UNIFIED" in name \
        or "HIRAGANA" in name \
        or "KATAKANA" in name:
            return True
    return False

def remove_commna_in_japanese(string):
	if is_japanese(string):
		return string.replace(',', '')
	else:
		return string

def strip_space(string):
	return re.sub(r' +', ' ', string)

def authors(string):
	return ",".join([apply_underline(abbrev_in_english(item)) for item in string.split('and')])

def abbrev_in_english(string):
	comma_n = string.find(',')
	if comma_n < 0:
		return string
	else:
		return string[comma_n+1:] + " " + string[0:comma_n]

def apply_underline(author):
	if 'Hisazumi' in author:
		return '\\underline{\\underline{'+author+'}}'
	else:
		return author

def strip(str):
	return strip_space(str).replace(' ,', ',').replace(',', ',').replace(' .', '.')

def author(str):
	return authors(remove_commna_in_japanese(str))

def emit_author(e):
	if "jauthor" in e:
		return e['author'] + '(著), ' + author(e['jauthor']) + '(訳)' + ': '
	else:
		return author(e['author']) + ': '

def emit_pages(e):
	if "pages" in e:
		return ", pp." + e['pages']
	else:
		return ""	

# read bibtex

with open('/Users/nel/Documents/tex/nel.bib') as f:
    bibdb = bibtexparser.loads(f.read())

def get_type_of(type):
	return [e for e in bibdb.entries if e['ENTRYTYPE'] == type]

books    = get_type_of('book')
journals = get_type_of('article')
procs    = get_type_of('inproceedings')

# emit markdown

# journals
def emit_journal(e):
	return '\\KLbibitem ' + strip(emit_author(e) + e['title'] + ',' + e['journal'] + ',' + e['publisher'] + emit_pages(e) + ',' + e['year'] + ".")

def emit_proc(e):
	return '\\KLbibitem ' + strip(emit_author(e) + e['title'] + ',' + e['booktitle'] + emit_pages(e) + ',' + e['year'] + ".")

years=[2016, 2015, 2014, 2013, 2012]

for y in years:
	print('\hline')
	print(str(y) + '\\\\')
	for e in [j for j in journals if int(j['year']) == y]:
		print(emit_journal(e) + '\\\\')

	for e in [p for p in procs if int(p['year']) == y]:
		print(emit_proc(e) + '\\\\')

print("")


