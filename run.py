#! /usr/bin/python
import argparse

__author__ = ''

parser = argparse.ArgumentParser(description='read a file from CLI argument and write output.')
parser.add_argument('-i', '--input',  help='Input filename', required=True)
parser.add_argument('-o', '--output', help='Output filename', required=True)
args = parser.parse_args()

# sanity check arguments
print ("Input file: %s" % args.input)
print ("Output file: %s" % args.output)

import csv
import json

data = {}
data['people'] = []

with open(args.input, 'rb') as f:
    # TODO read file
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader)  # skip the heading
    # TODO loop through file
    for line in csv_reader:
        data['people'].append({
            # 'name': 'Scott',
            # 'website': 'stackabuse.com',
            # 'from': 'Nebraska',
            'username': line[1],
            'email': line[2],
            'desk': line[0]
        })
        # data['people'].append({
        #     'name': 'Larry',
        #     'website': 'google.com',
        #     'from': 'Michigan'
        # })
        # data['people'].append({
        #     'name': 'Tim',
        #     'website': 'apple.com',
        #     'from': 'Alabama'
        # })
        # TODO print var1
        # print(line[1])

###################
import datetime

timeNow = datetime.datetime.now().strftime("%Y-%m%d-%H%M-%S")

timestampFilename = "data-" + timeNow + ".json"

with open(timestampFilename, 'w') as outfile:
    json.dump(data, outfile, sort_keys=True)

jsonString = json.dumps(data, indent=4, sort_keys=True)
print(jsonString)
print ('\n\n  Current date/time: {}'.format(timeNow))
