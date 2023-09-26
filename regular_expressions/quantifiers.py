#!/usr/bin/env python3
# User quantifiers to group or capture patterns.
import re

text = 'I see a blue sky and a beautiful rainbow.'

# Quantifiers to match vowels.
pattern = r'\w*[aeiou]{3,5}\w*'

matches = re.finditer(pattern, text)

for match in matches:
    print('\nMatch:',match.group(0))
