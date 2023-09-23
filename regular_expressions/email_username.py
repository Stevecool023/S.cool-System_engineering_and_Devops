#!/usr/bin/env python3

# Extract email and username.

import re

text = "Email: zeynepgatwiri@gmail.com, Username: Zeygatwiri"

pattern = r'Email: (\w+@\w+\.\w+), Username: (\w+)'

matches = re.finditer(pattern, text)

print()
for match in  matches:
    email = match.group(1)
    username = match.group(2)
    print('email is: ', email)
    print('username is: ', username)
