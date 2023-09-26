#!/usr/bin/env python3
# Naturally, regexes are greedy. They capture everything between specified patterns.
import re

html = '<h1>Title</h1><p>Paragraph</p>'

pattern_greedy = r'<.*>'

matches_greedy = re.findall(pattern_greedy, html)

print('Greedy matches:',matches_greedy)
