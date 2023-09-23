#!/usr/bin/env python3
# Using word bounderies.

import re
text = 'This is an example of word bounderies. words are really important. \n'\
        'Use them to display: Hello,world! and hello, Universe.'
text_0 = 'Displaying, declaring and commiting wordings is cool.'

pattern_a = r'\b\w+\b'
pattern_b = r'\b\W\b'
pattern_c = r'\b\w+ing\b'

words = re.findall(pattern_a, text)
non_words = re.findall(pattern_b, text)
ing_words = re.findall(pattern_c, text_0)

print()
print('Words in the text are:')
for word in words:
    print(word, end=', ')
print()
print()

print('None-words in the text are:')
for non_word in non_words:
    print(non_word, end='; ')
print()
print()

print('ing_words in the text are:')
for ing_word in ing_words:
    print(ing_word, end=', ')
print()
