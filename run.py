#! /usr/bin/python
#
# working code from frequently used modules
#

import datetime
import argparse
import csv
import json
import re

timeNow = datetime.datetime.now().strftime("%Y-%m%d-%H%M-%S")
timestampedFilename = "data-" + timeNow

parser = argparse.ArgumentParser(description='read a file from CLI argument and write output.')
parser.add_argument('-i', '--input',  help='Input CSV filename', required=True)
parser.add_argument('-o', '--output', help='Output prefix to JSON filename', required=True)
args = parser.parse_args()

outJsonfile = args.output + "-" + timestampedFilename + ".json"

# sanity check arguments
print ("Input file: %s" % args.input)
print ("Output file: %s" % outJsonfile)

data = {}
data['people'] = []

with open(args.input, 'rb') as f:
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader)  # skip the heading
    for line in csv_reader:
        #use next line for degugging 
        #print(line)
        data['people'].append({
            'username': line[1],
            'email': line[2],
            'desk': line[0]
        })

with open(outJsonfile, 'w') as outfile:
    json.dump(data, outfile, sort_keys=True)

jsonString = json.dumps(data, indent=4, sort_keys=True)
print(jsonString)
print('\n')