#!/usr/bin/env python3
# Using regular expressions flags.
# re.I ==> case-insensitive matching.
# re.M ==> Multiline: Changes '^' and '$' to match the start and end of the input string rather than just the start and end of the intire string.
# re.S ==> Dot-All: Makes the '.' character match any characters including a newline, '\n'.
# re.U ==> Unicode: Enables unicode matching, allowing you to work with non-ASCII character.
# re.X ==> Extended: Allows you to write more readable regular expressions by ignoring whitespace and allowing comments.

import re

text = 'Email: user @ example.com, Contact: info@company.org'

# Use re.X to find email with appended whitespace.
pattern = r'''
    (\w+)       # Match the username.
    \s*         # Match optional whitespace.
    \@          # Match the '@' symbol.
    \s*         # Match optional whitespace.
    (\w+.\w+)   # Match the domain.
    '''

matches = re.finditer(pattern, text, re.X)

for match in matches:
    print('\n', match.group(0))
    print('     Username:', match.group(1))
    print('     Domain:',match.group(2))
