#!/usr/bin/env python3

import re

text = "Date 1: 2023-12-04, Date 2: 09/12/2022, Date 3: 01-January-2019"

# Date formats: yyyy-mm-dd, mm/dd/yyyy or dd-Month-yyyy.
pattern = r'((\d{4})-(\d{2})-(\d{2}))|((\d{2})/(\d{2})/(\d{4}))|((\d{2})-(\w{3,9})-(\d{4}))'

matches = re.finditer(pattern, text)

for match in matches:
    print('\nFull date: ', match.group(0))
    if match.group(1):
        print('     Year: ', match.group(2))
        print('     Month: ', match.group(3))
        print('     Day: ', match.group(4))
    elif match.group(5):
        print('     Year: ', match.group(8))
        print('     Month: ', match.group(6))
        print('     Day: ', match.group(7))
    elif match.group(9):
        print('     Year: ', match.group(12))
        print('     Month: ', match.group(11))
        print('     Day: ', match.group(10))
    else:
        print('Date format not found.')
