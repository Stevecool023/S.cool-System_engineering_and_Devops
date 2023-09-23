#!/usr/bin/env python3

# This regex program is for validating passwords.
# Rule: A password should have atleast one uppercase, lowercase and digit character.
# + and be between 8 and 16 charaters long.

import re
passwords = """hgiu8u4t8iu, ry8qy948phurehu, iuy8try98yhierh, qyt8fhaer8h,\
            XCTY_gygyu35-76, 364A589/-tyy_u, uDygui-7667_54!"""

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,16}$'

# Split the passwords in a list.
password_list = passwords.split(',')

print()
print('Valid passwords from the list are:')

for password in password_list:
    # Remove leading and trailling whitespace from each password.
    password = password.strip()
    # Check for matching passwords.
    if re.match(pattern, password):
        print(password)
