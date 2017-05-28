import unicodedata
import bibtexparser


def format_authors(authors):
    def is_japanese(string):
        try:
            for ch in string:
                name = unicodedata.name(ch)
                if "CJK UNIFIED" in name \
                        or "HIRAGANA" in name \
                        or "KATAKANA" in name:
                    return True
        except ValueError:
            print(string)
            return False
        return False

    def format_in_japanese(author):
        return author.replace(',', '')

    def format_in_english(author):
        if ',' in author:
            sirname, givenname = author.split(',')
            return givenname + ' ' + sirname
        else:
            return author

    def format(author):
        if is_japanese(author):
            return format_in_japanese(author)
        else:
            return format_in_english(author)

    al = authors.split('and')
    return ', '.join([format(s.replace(' ', '')) for s in al])


def format_pages(pages):
    return "pp. " + pages


def format_refs(e):
    transforms = [['journal', ''],
                  ['booktitle', ''],
                  ['volume', 'Vol. '],
                  ['number', 'No. '],
                  ['publisher', ''],
                  ['pages', 'pp.']]
    firstp = True
    refs = ''
    for t in transforms:
        if t[0] in e:
            if firstp:
                refs += t[1] + e[t[0]]
                firstp = False
            else:
                refs += ', ' + t[1] + e[t[0]]

    return refs


def format_identity(e):
    return e


def read_bib(filename):
    with open(filename) as f:
        return bibtexparser.loads(f.read())


def get_type_of_bib(bibdb, type):
    transforms = {'author': format_authors,
                  'title': format_identity,
                  'month': format_identity,
                  'year': format_identity}
    entries = [e for e in bibdb.entries if e['ENTRYTYPE'] == type]
    result = []
    for e in entries:
        r = {}
        for key, func in transforms.items():
            if key in e:
                r[key] = func(e[key])
        r['refs'] = format_refs(e)
        result.append(r)

    return result
