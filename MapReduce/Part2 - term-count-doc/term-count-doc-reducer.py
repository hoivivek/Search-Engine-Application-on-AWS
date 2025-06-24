#!/usr/bin/python3

import sys

current_doc = None
current_count = 0
for line in sys.stdin:
    docid, count = line.strip().split('\t')
    count = int(count) 
    if current_doc == docid:
        current_count += count
    else:
        if current_doc:
            print('%s\t%s' % (current_doc, current_count))          
        current_doc = docid
        current_count = count

if current_doc:
   print('%s\t%s' % (current_doc, current_count))
