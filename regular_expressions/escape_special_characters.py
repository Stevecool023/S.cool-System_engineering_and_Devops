#!/usr/bin/env python3
# Escaping special characters to print them literary.
import re

text = 'File names: file1.txt, file2.txt, file3txt'

pattern = r'file\d\.txt'

matches = re.finditer(pattern, text)

for match in matches:
    print('Matches:', match.group(0))
