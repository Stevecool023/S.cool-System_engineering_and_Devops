#!/usr/bin/env python3

import re  # Import the 're' module, which provides support for regular expressions

text = "You can reach me at user@example.com or info@example.org."  # Define a text string

# Define the regex pattern using a raw string (r'...') to avoid interpreting backslashes as escape sequences
pattern = r'\w+@[\w.]+'

# Use the re.findall() function to find all non-overlapping matches of the pattern in the text
matches = re.findall(pattern, text)

# Iterate through the matches and print each one
for match in matches:
    print(match)
