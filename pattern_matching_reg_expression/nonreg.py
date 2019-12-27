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

print('415-555-4242 is a phone number: ')
print(str(isPhoneNumb('415-555-4242')))
print('Jonathan Almawi is a phone number')
print(isPhoneNumb('Jonathan Almawi'))
