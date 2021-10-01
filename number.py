phone_number = input()

phone_number = phone_number.replace(' ', '').replace('\n', '').replace(' ', '')
is_valid = True
if phone_number.startswith('8') or phone_number.startswith('+7'):
    pass
else:
    is_valid = False
if '(' in phone_number or ')' in phone_number:
    if phone_number.count('(') != 1 or phone_number.count(')') != 1 \
or phone_number.find(')') <= phone_number.find('('):
        is_valid = False
if phone_number.startswith('-') or phone_number.endswith('-'):
    is_valid = False
if '--' in phone_number:
    is_valid = False

phone_number = phone_number.replace('-', '').replace('(', '').replace(')', '')

if phone_number.startswith('8'):
    phone_number = '+7' + phone_number[1:]

if not phone_number[1:].isdigit() or len(phone_number) != 12:
    is_valid = False

if is_valid:
    print(phone_number)
else:
    print('error')
