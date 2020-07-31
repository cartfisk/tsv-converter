#!/usr/bin/python

import glob
import csv
import sys
import os

# Create glob pattern, fetch filenames
if len(sys.argv) < 2:
    pattern = os.path.join('.', 'tsv', '*.tsv')
else:
    pattern = os.path.join(sys.argv[1], '*.tsv')

filenames = glob.glob(pattern)

# Loop through, and convert
for i, source_filename in enumerate(filenames):
    csv.field_size_limit(sys.maxsize)
    
    print(source_filename)
    print(source_filename.rstrip('.tsv'))
    dest_filename = os.path.join('.', 'csv', os.path.basename(source_filename).rstrip('.tsv')) + '.csv'

    with open(source_filename) as source_tsv:
        reader = csv.reader(source_tsv, delimiter='\t', quotechar='|')
        with open(dest_filename, 'w', newline='') as dest_csv:
            writer = csv.writer(dest_csv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

            for row in reader:
                writer.writerow(row)

    i += 1
    print('Created: ' + os.path.basename(dest_filename))

print('\n', i, 'files have been converted...\n')