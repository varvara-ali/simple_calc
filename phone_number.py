try:
    phone_number = input()

    phone_number = phone_number.replace(' ', '').replace('\n', '').replace('\t', '')
    is_valid = True
    if not phone_number.startswith('8') and not phone_number.startswith('+7'):
        raise ValueError("неверный формат")
    if phone_number.startswith('+7'):
        phone_number = '8' + phone_number[2:]
    if '(' in phone_number or ')' in phone_number:
        if phone_number.count('(') != 1 or phone_number.count(')') != 1 or \
                phone_number.find(')') <= phone_number.find('('):
            raise ValueError("неверный формат")
    if phone_number.startswith('-') or phone_number.endswith('-'):
        raise ValueError("неверный формат")
    if '--' in phone_number:
        raise ValueError("неверный формат")

    phone_number = phone_number.replace('-', '').replace('(', '').replace(')', '')
    if any([not t.isdigit() for t in phone_number]):
        raise ValueError("неверный формат")

    if phone_number.startswith('8'):
        phone_number = '+7' + phone_number[1:]

    if len(phone_number) != 12:
        raise ValueError("неверное количество цифр")

    print(phone_number)
except ValueError as e:
    print(f'{e}')
