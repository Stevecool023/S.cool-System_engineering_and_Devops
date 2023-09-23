#!/usr/bin/env python3

import re

text = "John's phone number is (123) 456-7890, and Jane's is (987) 654-3210."

# Define a pattern with capturing groups to match phone numbers
pattern = r'\((\d{3})\) (\d{3}-\d{4})'

# Find all matches using finditer
matches = re.finditer(pattern, text)

for match in matches:
    area_code = match.group(1)
    phone_number = match.group(2)
    print("Area Code:", area_code)
    print("Phone Number:", phone_number)

