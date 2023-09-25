#!/usr/bin/env python3

# Re-use captured groups within the same regular expression pattern.

import re

text = 'This is a repeated string. That is that.'
pattern = r'\b(\w+)\b(?:.*\b\1\b)+'
match = re.findall(pattern, text)
print('Repeated words are: ', match)
