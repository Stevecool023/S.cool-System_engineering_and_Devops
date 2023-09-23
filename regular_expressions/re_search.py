#!/usr/bin/env python3
import re

text = 'The cat, her bag and my hat are all in the flat'

pattern = r'\b\w+at\b'

match = re.search(pattern, text)

if match:
    print(match.group())
