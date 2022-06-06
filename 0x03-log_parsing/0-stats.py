#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""
import re
import sys


total_size = 0
status_codes_dict = {200: 0, 301: 0, 400: 0, 401: 0,
                     403: 0, 404: 0, 405: 0, 500: 0}
i = 0
pattern = re.compile(r'(?P<ip_address>.+)\s*'
                     r'-\s*(?P<date>\[\d{1,4}-\d{1,2}-\d{1,2} '
                     r'\d+:\d+:\d+.+\]) "\w+ /\w+/\d+ '
                     r'\w+/\d.+" (?P<status_code>200|301|'
                     r'400|401|403|404|405|500) '
                     r'(?P<file_size>\d+)\n')
try:
    for line in sys.stdin:
        i += 1
        match = pattern.fullmatch(line)
        try:
            status_code = int(match.group('status_code'))
        except AttributeError:
            status_code = ''
        if match is None:
            if i % 10 == 0:
                print('File size: {}'.format(total_size))
                for key, val in status_codes_dict.items():
                    if val != 0:
                        print('{}: {}'.format(key, val))
            continue
        if status_code not in status_codes_dict:
            total_size += int(match.group('file_size'))
            continue
        total_size += int(match.group('file_size'))
        status_codes_dict[status_code] += 1
        if i % 10 == 0:
            print('File size: {}'.format(total_size))
            for key, val in sorted(status_codes_dict.items()):
                if val != 0:
                    print('{}: {}'.format(key, val))
    else:
        print('File size: {}'.format(total_size))
        for key, val in sorted(status_codes_dict.items()):
            if val != 0:
                print('{}: {}'.format(key, val))

except KeyboardInterrupt:
    print('File size: {}'.format(total_size))
    for key, val in sorted(status_codes_dict.items()):
        if val != 0:
            print('{}: {}'.format(key, val))
