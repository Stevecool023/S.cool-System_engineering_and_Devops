#!/usr/bin/env python3
import re

text = 'The cat, her mat and my hat are all in the flat'

pattern = r'\w+at'

matches = re.findall(pattern, text)

print(matches)
