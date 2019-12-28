def isPhoneNumb(text):
    if len(text) != 12:
        return False
    for index in range(0, 3):
        if not text[index].isdecimal():
            return False
    if text[3] != '-':
        return False
    for index in range(4, 7):
        if not text[index].isdecimal():
            return False
    if text[7] != '-':
        return False
    for index in range(8, 12):
        if not text[index].isdecimal():
            return False
    return True
message = 'Call me at 415-555-1011 tomm. 414-413-4444 is my office.'
for index in range(len(message)):
    chunk = message[index:index+12]
    if isPhoneNumb(chunk):
        print('Phone number found: ' + chunk)
print('Done')