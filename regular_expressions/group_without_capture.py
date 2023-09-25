#!/usr/bin/env python3
# Group parts of a pattern without capturing them.

import re
text = 'Match cat and cats and not catssss.'
pattern = r'cat(?:s)?'
matches = re.finditer(pattern, text)
for match in matches:
    print('Match:',match.group(0))
