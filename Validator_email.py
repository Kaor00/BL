import validators

v = validators.email('ka1RieZzz@ou.ru')

if v:
    print('[+] Ok\nThe email address is valid.')
else:
    print('[+] BAD\nThe email address format is not valid.')

# Странно работает
