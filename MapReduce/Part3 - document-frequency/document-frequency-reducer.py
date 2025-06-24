#!/usr/bin/python3
import sys

current_term = None
current_doc_id = set()

for line in sys.stdin:
    term, docid = line.strip().split('\t')  

    if term == current_term:
        current_doc_id.add(docid)
    else:
        if current_term:
            print('%s\t%s' % (current_term, len(current_doc_id)))
        current_term = term
        current_doc_id = set()
        current_doc_id.add(docid)

if current_term:
    print('%s\t%s' % (current_term, len(current_doc_id)))

