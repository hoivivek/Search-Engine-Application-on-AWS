#!/usr/bin/python3
import sys

current_key = None
current_count = 0

for line in sys.stdin:
    key, count = line.strip().split('\t')
    if current_key == key:
        current_count += int(count)
    else:
        if current_key:
            docid, term = current_key.split('+', 1)
            print(f"{docid}\t{term}\t{current_count}")
        current_key = key
        current_count = int(count)

if current_key:
    docid, term = current_key.split('+', 1)
    print(f"{docid}\t{term}\t{current_count}")

