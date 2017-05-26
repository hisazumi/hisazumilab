---
title: Publications
date: 2222-02-22 22:22:22
permalink: pub
---

# Books
1. Wayne Wolf(著), 中西恒夫, 北須賀輝明, 久住憲嗣, 室山真徳, 田頭茂明(訳): 組込みシステム設計の基礎, 日経BP社, 2009.

# Journals
{% for e in journals %}
1. {{e['author']}}: {{e['title']}}, {{e['refs']}}, {{e['year']}}.
{% endfor %}

# Conferences & Workshops
{% for e in procs %}
1. {{e['author']}}: {{e['title']}}, {{e['refs']}}, {{e['year']}}.
{% endfor %}

