import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for raw in f:
        ip = ''.join(re.findall(re.compile(r'^\d+\.\d+\.\d+\.\d+'), raw))
        date = ''.join(re.findall(re.compile(r'\d{,2}/\w+/\d{4}:\d{2}:\d{2}:\d{2}\s\+\d{4}'), raw))
        get = ''.join(re.findall(re.compile(r'GET'), raw))
        path = ''.join(re.findall(re.compile(r'/\w+/[^0-9]\w+'), raw))
        code = ''.join(re.findall(re.compile(r'"\s(\d{3})\s'), raw))
        size = ''.join(re.findall(re.compile(r'\s(\d+)\s"'), raw))

        compiles = (ip, date, get, path, code, size)

        print(compiles)
