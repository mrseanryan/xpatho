#! python3
"""
xpatho_csv.py
Author: Sean Ryan
Version: 1.0

A command line tool to obfuscate XPath expressions (replacing any IP sensitive parts)

Usage: xpatho_csv.py <path to CSV file containing XPath expressions> <path to output CSV file> [options]

The options are:
[-c --csv_column (If reading a CSV file, specifies which column to read, using a 0-based index)]
[-d --csv_delimiter (If reading a CSV file, specifies the field delimiter)]
[-h --help]

Examples: [Windows]
xpatho_csv.py testData\\xpaths_1.csv temp\\xpaths_1.obfuscated.csv -csv_column 1
xpatho_csv.py \\data\\xpaths_2.csv temp\\xpaths_2.obfuscated.csv -csv_column 1

Examples: [Unix/Mac]
xpatho_csv.py ./testData/xpaths_1.csv temp/xpaths_1.obfuscated.csv -csv_column 1
xpatho_csv.py /data/xpaths_2.csv temp/xpaths_2.obfuscated.csv -csv_column 1
"""

import csv
from functools import reduce
from operator import delitem
from optparse import OptionParser
import os
import sys
import tempfile
from multiline_state import MultilineState

import xpath_obfuscator

# usage() - prints out the usage text, from the top of this file :-)
def usage():
    print(__doc__)

# optparse - parse the args
parser = OptionParser(
    usage='%prog <path to text file containing XPath expressions> [options]')
parser.add_option('-c', '--csv_column', dest='csv_column', type='int', nargs=1,
                default=-1,
                help='If reading a CSV file, specifies which column to read, using a 0-based index')
parser.add_option('-d', '--csv_delimiter', dest='csv_delimiter', type='string',
                default='\t',
                help='If reading a CSV file, specifies the field delimiter')

(options, args) = parser.parse_args()
if (len(args) != 2):
    usage()
    sys.exit(2)

pathToXPath = args[0]
pathToOutputCsv = args[1]

if(options.csv_column < 0):
    raise Exception("For a CSV file, you must set the option --csv_column")

def trim_all(texts):
    return [t.strip() for t in texts]

def process_csv_to_new_csv(pathToFile, csv_column, csv_delimiter, csv_out_path):
    tmp_file = tempfile.NamedTemporaryFile(delete=False)

    reader = csv.reader(open(pathToFile, newline=''), delimiter=csv_delimiter, skipinitialspace = True)

    line_count = 0
    with open(csv_out_path, 'w', newline='') as fout:
        writer = csv.writer(fout, delimiter=csv_delimiter)
        for row in reader:
                xpath = row[csv_column].replace("\n", " ").replace("\r", "")
                obfuscated = xpath_obfuscator.obfuscate(xpath)
                row[csv_column] = obfuscated
                writer.writerow(row)
                line_count = line_count + 1

    tmp_file.close()

    return (tmp_file.name, line_count)

def main():
    (obfuscated_xpaths, line_count) = process_csv_to_new_csv(pathToXPath, options.csv_column, options.csv_delimiter, pathToOutputCsv)
    print(f"Output new CSV file with {line_count} obfuscated XPaths at {pathToOutputCsv}")
    return

if __name__ == '__main__':
    main()
