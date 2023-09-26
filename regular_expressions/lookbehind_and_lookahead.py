#!/usr/bin/env python3
# There is positive lookahead and negative lookahead as well as positive lookbehind and negative lookbehind.
# Illustrating the use of positive lookahead and positive lookbehind.

import re

text = "There is a green apple tree and a red apple tree."

# Positive lookahead and negative lookahead.
pattern = r'(?<=green )apple(?= tree)'

matches = re.finditer(pattern, text)

for match in matches:
    print('\nMatch:', match.group(0))
