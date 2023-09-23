#!/usr/bin/env python3
import re

text = "John's phone number is (123) 456-7890 and Jane's is (987) 654-3210."

pattern_1 = r"(\w+)'s (\(\d{3}\) \d{3}-\d{4})"
pattern_2 = r'\((\d{3})\) (\d{3}-\d{4})'

# Use finditer to find all matches in the text.
matches = re.finditer(pattern_1, text)

print("House owner, Area Zip_code, Owner's phone_number:")

# Iterate over matches using a loop.
for match in matches:
    name = match.group(1)
    address_info = match.group(2)
    zip_code, phone_number = re.search(pattern_2, address_info).groups()

    print(name + ", " + zip_code + ", " + phone_number)
