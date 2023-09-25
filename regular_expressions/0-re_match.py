#!/usr/bin/env python3
import re

# Using flags on re.match.
string = 'The quick brown fox jumps over the lazy dog.'
output = re.match(r'The', string, re.I)
if output:
    print('Match found: ', output)
else:
    print('Match not found.')
