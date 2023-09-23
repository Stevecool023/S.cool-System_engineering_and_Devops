#!/usr/bin/env python3
import re

text = 'The cat, her mat and my bag are all in the flat'

pattern = r'\b\w+at\b'

matches = re.findall(pattern, text)

for match in matches:
    print(match)
