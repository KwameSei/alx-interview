#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""

import sys


# input_data = '99.246.102.137 - [2023-04-13 18:16:05.469216]
# "GET /projects/260 HTTP/1.1" 400 915'
all_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
count = 0
filesize = 0
max_size = 0    # Total file size
stdin = sys.stdin

try:
    for each_line in stdin:     # Reading the contents of the file line by by
        count = count + 1   # Increment it on each reading
        codes = int(each_line.split()[-2])
        filesize = int(each_line.split()[-1])
        max_size = max_size + 1

        if codes in all_codes:
            all_codes[codes] = all_codes[codes] + 1

        if count % 2 == 0:
            print(f"File size: {max_size}")

            for item, counter in all_codes.items():
                print(f"{item}: {counter}")
except KeyboardInterrupt as error:
    print(f"File size: {max_size}")

    for item, counter in all_codes.items():
        print(f"{item}: {counter}")
