#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics
"""
import sys
import re
import signal


total_size = 0
status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0,
                     '403': 0, '404': 0, '405': 0, '500': 0}

try:
    i = 0
    file = sys.stdin.readlines()
    pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} '
                         r'- \[\d{1,4}-\d{1,2}-\d{1,2} \d+:\d+:\d+'
                         r'.+\] "\w+ /\w+/\d+ '
                         r'\w+/\d.\d" (?P<status_code>200|301|'
                         r'400|401|403|404|405|500) '
                         r'(?P<file_size>\d+)\n')
    for line in file:
        i += 1
        match = pattern.fullmatch(line)
        if match is None:
            continue
        total_size += int(match.group('file_size'))
        if match.group('status_code') not in status_codes_dict:
            continue
        status_code = match.group('status_code')
        status_codes_dict[status_code] += 1
        if i % 10 == 0:
            print('File size: {}'.format(total_size))
            for key, val in status_codes_dict.items():
                if val != 0:
                    print('{}: {}'.format(key, val))

except KeyboardInterrupt:
        sys.stdout.flush()
