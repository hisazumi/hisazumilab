# an exporter for hexo

# read bibtex

import bibtexparser

with open('/Users/nel/Documents/tex/nel.bib') as f:
    bibdb = bibtexparser.loads(f.read())

def get_type_of(type):
	return [e for e in bibdb.entries if e['ENTRYTYPE'] == type]

journals = get_type_of('article')
procs    = get_type_of('inproceedings')

# emit markdown

print("---")
print("title: Publications")
print("date: 2016-09-16 14:08:18")
print("permalink: pub")
print("---")
print("")

# journals
print("# Journal")
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
