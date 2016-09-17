# an exporter for hexo

import datetime
import bibtexparser
import unicodedata

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

def strip(str):
	return str.replace(' ,', ',').replace(',', ', ').replace(' .', '.')

def author(str):
	return remove_commna_in_japanese(str)

def emit_author(e):
	if "jauthor" in e:
		return '1. ' + e['author'] + '(著), ' + author(e['jauthor']) + '(訳)' + ': '
	else:
		return '1. ' + author(e['author']) + ': '

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

print("---")
print("title: Publications")
print("date: ", datetime.datetime.today())
print("permalink: pub")
print("---")
print("")

# books
def emit_book(e):
	return strip(emit_author(e) + e['title'] + ',' + e['publisher'] + emit_pages(e) + ',' + e['year'] + ".")

print("# Books")
print("")
for e in books:
	print(emit_book(e))
	print('')

# journals
def emit_journal(e):
	return strip(emit_author(e) + e['title'] + ',' + e['journal'] + ',' + e['publisher'] + emit_pages(e) + ',' + e['year'] + ".")

print("# Journals")
print("")
for e in journals:
	print(emit_journal(e))
	print('')

# conferences & workshops
def emit_proc(e):
	return strip(emit_author(e) + e['title'] + ',' + e['booktitle'] + emit_pages(e) + ',' + e['year'] + ".")

print("# Conferences & Workshops")
print("")
for e in procs:
	print(emit_proc(e))
	print('')
