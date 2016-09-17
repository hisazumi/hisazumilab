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
print("# Books")
print("")
for e in books:
	if "jauthor" in e:
		str = '1. ' + e['author'] + '(著), ' + author(e['jauthor']) + '(訳)' + ':' + e['title'] + ',' + e['publisher'] + ',' + e['year'] + "."
	else:
		str = '1. ', e['author'],': ', e['title'], ',', e['publisher'], ',', e['year'], "."
	print(strip(str))
	print('')

# journals
print("# Journals")
print("")
for e in journals:
	print(strip('1. ' + author(e['author']) + ': ' + e['title'] + ',' + e['journal'] + ',' + e['year'] + "."))
	print('')

# conferences & workshops
print("# Conferences & Workshops")
print("")
for e in procs:
	#print(e)
	print(strip('1. ' + author(e['author']) + ': ' + e['title'] + ',' + e['booktitle'] + ',' + e['year'] + "."))
	print('')
