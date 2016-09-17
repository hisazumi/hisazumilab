# an exporter for hexo

import datetime
import bibtexparser

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
	#print(e)
	if "jauthor" in e:
		print('1. ', e['author'],'(著)', e['jauthor'], '(訳)', ':', e['title'], ',', e['publisher'], ',', e['year'], ".")
	else:
		print('1. ', e['author'],':', e['title'], ',', e['publisher'], ',', e['year'], ".")
	print('')

# journals
print("# Journals")
print("")
for e in journals:
	#print(e)
	print('1. ', e['author'], ':', e['title'], ',', e['journal'], ',', e['year'], ".")
	print('')

# conferences & workshops
print("# Conferences & Workshops")
print("")
for e in procs:
	#print(e)
	print('1. ', e['author'], ':', e['title'], ',', e['booktitle'], ',', e['year'], ".")
	print('')
