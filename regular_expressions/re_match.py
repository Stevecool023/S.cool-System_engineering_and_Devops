#!/usr/bin/env python3
import re

# Implementation of re.match. Finds patterns only at the beggining of a string.

print()
print('Find pattern at the beggining of a string')
string = 'The quick brown fox jumps over the lazy dog'
pattern = r'The'
match = re.match(pattern, string)
if match:
    print('Match found: ', match)
else:
    print('Match not found.')
