#!/usr/bin/python3

import sys

for line in sys.stdin:
    docid, term, count = line.strip().split('\t')
    print('%s\t%s' % (docid, count))
