#!/usr/bin/env python

"""
process_csv.py

Copyright 2009-2014 by Project Gutenberg

Distributable under the GNU General Public License Version 3 or newer.

process a pg_catalog CSV file to turn multiline titles into single line titles
No dependencies, tested in Python 3.8, should work in python 3.6+

syntax:

`python process_csv.py (<path to input csv file> (<path to output file>))`

defaults: 
<path to input csv file>: `pg_catalog.csv`
<path to output file>: `pg_catalog_out.csv`

"""

import csv
import re
import sys

NEWLINE = re.compile(r' *[\r\n]+ *')

def oneline_title(text):
    return NEWLINE.sub('; ', text)

def process(in_file='pg_catalog.csv', out_file='pg_catalog_out.csv'):
    with open(in_file,'r') as pg_catalog:
        reader = csv.DictReader(pg_catalog, dialect="excel")
        writer = None
        with open(out_file,'w') as pg_catalog_out:
            for book in reader:
                if not writer:
                    writer = csv.DictWriter(pg_catalog_out, fieldnames=book.keys())
                    writer.writeheader()
                book['Title'] = oneline_title(book['Title'])
                writer.writerow(book)


def main():
    if len(sys.argv) > 1:
        in_file = sys.argv[1]
        if len(sys.argv) > 2:
            out_file = sys.argv[2]
            process(in_file=in_file, out_file=out_file)
        else:
            process(in_file=in_file)
    else:
        process()

if __name__ == '__main__':
    main()
