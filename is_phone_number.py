
def is_phone_nuber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    
    return True

# print('415-555-4242 - this is phon number:')
# print(is_phone_nuber('415-555-4242'))
# print('Moshi moshi - this is phon number:')
# print(is_phone_nuber('Moshi moshi'))

massage = 'Call me tomorrow on number 415-555-1011. 415-555-9999 - this is number my office'

for i in range(len(message)):
    chunk = massage[i:i+12]
    if is_phone_nuber(chunk):
        print('Found phone nubmer:')
