#!/usr/bin/env python3

# Import re in order to utilize functions in the regular expressions module.
import re

# Define contact_list where numbers are to be obtained from.
contact_list = "Contacts of the short-listed software engineers are:\n"\
               " Stephen Karanja :   +254 700 986 273\n"\
               "                 :   0798 365 257\n"\
               "                 :   0701 283 64t\n"\
               " Abel Mutwa      :   +132 836 836 638\n"\
               "                 :   +333 868 823234\n"\
               "                 :   0111563452\n"\
               " Zeynep Gatwiri  :   (456) 123-5672\n"\
               "                 :   676-6757"

# Spell out the pattern to use when looking for the contacts.
pattern = r'(\(\d{3}\) \d{3}-\d{4})|\d{3}-\d{4}|[+]\d{3}\s{1}\d{3}\s{1}\d{3}\s{1}\d{3}|07\d{2}\s{1}\d{3}\s{1}\d{3}|011\d{7}'

# Initialize the list of contacts found, matches.
# Use finditer to find all matches and iterate over them.
matches = re.finditer(pattern, contact_list)

# Start a for loop to iterate over and print contacts.
for match in matches:
    # Extract the matched portion of the text.
    phone_number = match.group(0)
    
    # Print the phone number
    print(phone_number)

