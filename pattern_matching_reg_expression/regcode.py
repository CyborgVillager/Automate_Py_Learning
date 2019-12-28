import re
# more information for reg expre operators
# https://docs.python.org/3/library/re.html
# https://www.w3schools.com/python/python_regex.asp
# https://www.programiz.com/python-programming/regex

phone_Number_Regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
match = phone_Number_Regex.search('My number is 751-555-60606 .')
print('Phone number found: ' + match.group())

#pg 152-8 - maki custom chara classes