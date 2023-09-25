#!/usr/bin/env python3
# Use capturing groups to print domain and username parts of and email.

import re

# Input text containing email addresses
text = "Email: user@example.com, Contact: info@company.org, Support: help@domain.net"

# Regular expression pattern for matching email addresses
email_pattern = r'(\w+)@(\w+\.\w+)'

# Use findall to find all email addresses in the text
matches = re.findall(email_pattern, text)

# Initialize a counter for email numbering
email_count = 1

# Iterate over the matches and print the results
for match in matches:
    username, domain = match
    print(f"Email {email_count}:")
    print(f"  Username: {username}")
    print(f"  Domain: {domain}\n")
    email_count += 1
