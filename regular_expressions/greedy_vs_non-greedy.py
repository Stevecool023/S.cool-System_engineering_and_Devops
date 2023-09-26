#!/usr/bin/env python3
# Naturally, regexes are greedy. They capture everything between specified patterns.
import re

html = '<h1>Title</h1><p>Paragraph</p>'

# Greedy matching.
pattern_greedy = r'<.*>'

matches_greedy = re.findall(pattern_greedy, html)

print('\nGreedy matches:',matches_greedy)



# One can use '*?', '+?', or '??' after a quantifier to make it non-greedy.
# Non-greedy (lazy) matching.
pattern_non_greedy = r'<.*?>'

matches_non_greedy = re.findall(pattern_non_greedy, html)

print('\nNon-Greedy Matches:', matches_non_greedy)
print()
