#!/usr/bin/env python3

# Phone numbers can have different formats like: (123) 456-7890, 555-5555,+000 000 000 000, 0799 999 999, 0111111111.
# Use regex to find contacts with the above formats.

# Import re in order to utilize functions in regular expressions module.
import re

# Define contat_list where numbers are to be obtained from.
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
pattern = "(\(\d{3}\) \d{3}-\d{4})|(\d{3}-\d{4})|([+]\d{3}\s{1}\d{3}\s{1}\d{3}\s{1}\d{3})|(07\d{2}\s{1}\d{3}\s{1}\d{3})|\n"\
            "(011\d{7})"

# Initialize the list of contacts found, matches.
matches = re.findall(pattern, contact_list)

# Start for loop to iterate over and print contacts.
for match in matches:
    # join empty strings from contacts to print one contact
    phone_number = ''.join(filter(None, match))
    print(phone_number)
