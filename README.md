# bibtex2md.py bibtex2csv.py bibtex2kaken.py

bibtex形式で記述している自分のpublication listを以下の形式に変換するスクリプトです:
* bibtex2md.py: markdownというかhexoで作成しているページのpublication list
* bibtex2csv.py: 九州大学の大学評価システムに入力する前データとしてのCSV
* bibtex2kaken.py: 科研TeXテンプレートの業績リスト

全くユーザフレンドリーではないですが:
> bib = read_bib('/Users/nel/GD/tex/nel.bib')

を自分の文献リストのbibファイルのパスに変更したり，すると使えるようになるかもしれません．
