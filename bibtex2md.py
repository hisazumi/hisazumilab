import bibtexparser

with open('/Users/nel/Documents/tex/nel.bib') as f:
    bibdb = bibtexparser.loads(f.read())


print("---")
print("title: Publications")
print("date: 2016-09-16 14:08:18")
print("permalink: pub")
print("---")
print("")

#print(bibdb.entries)

print("# Journal")
for e in bibdb.entries:
	#print(e)
	print('1. ', e['author'], ':', e['title'], ',', e['journal'], ',', e['year'], ".")
	print('')


