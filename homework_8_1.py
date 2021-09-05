import re

RE_EMAIL = re.compile(
    r'(?P<username>[^@А-Яа-я`~!#$%^&*()_+"№;:?=-]+)@(?P<domain>[^@А-Яа-я`~!#$%^&*()_+"№;:?=-]+\.[^@А-Яа-я`~!#$%^&*()_+"№;:?=-]+)')

email = input('Введите email: ')
assert RE_EMAIL.match(email), f'wrong email: {email}'
[print(mail.groupdict()) for mail in re.finditer(RE_EMAIL, email)]
