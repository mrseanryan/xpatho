#! python3
"""
xpatho.py
Author: Sean Ryan
Version: 1.0

A command line tool to obfuscate XPath expressions (replacing any IP sensitive parts)

Usage: xpatho.py <path to text file containing XPath expressions> [options]

The options are:
[-c --csv_column (If reading a CSV file, specifies which column to read, using a 0-based index)]
[-d --csv_delimiter (If reading a CSV file, specifies the field delimiter)]
[-e --empty (Do not omit empty XPaths)]
[-h --help]
[-o --output_csv (If reading a CSV file, this is the path to the new output CSV file)]
[-u --unique (Omit duplicates)]

Examples: [Windows]
xpatho.py testData\\xpaths_1.txt
xpatho.py \\data\\xpaths_1.txt

Examples: [Unix/Mac]
xpatho.py ./testData/xpaths_1.txt
xpatho.py /data/xpaths_1.txt
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
parser.add_option('-e', '--empty', dest='is_keep_empties_enabled', action='store_const',
                const=True, default=False,
                help='Also output empty XPaths')
parser.add_option('-o', '--output_csv', dest='output_csv', type='string',
                default='',
                help='If reading a CSV file, this is the path to the new output CSV file')
parser.add_option('-u', '--unique', dest='is_unique_enabled', action='store_const',
                const=True, default=False,
                help='Only output unique XPaths: omit any duplicates')

(options, args) = parser.parse_args()
if (len(args) != 1):
    usage()
    sys.exit(2)

pathToXPath = args[0]

def is_csv_file(filePath):
    extension = os.path.splitext(filePath)[1]
    return extension.lower() == ".csv"

if is_csv_file(pathToXPath):
    if(options.csv_column < 0):
        raise Exception("For a CSV file, you must set the option --csv_column")
    if(len(options.output_csv) == 0):
        raise Exception("For a CSV file, you must set the option --output_csv")

def ilen(iterable):
    return reduce(lambda sum, element: sum + 1, iterable, 0)

def list_size_as_text(events):
    return str(ilen(events))

def process_file(path_to_file):
    obfuscated_xpaths = []
    with open(path_to_file, encoding="utf8") as opened_file:
        state = MultilineState()
        for line in opened_file:
                if (state.is_line_balanced(line)):
                    obfuscated_xpaths.append(xpath_obfuscator.obfuscate(state.get_combined()))
                    state = MultilineState()
    return obfuscated_xpaths

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
    obfuscated_xpaths = []
    path_to_xpath_only = pathToXPath
    if (is_csv_file(pathToXPath)):
        (obfuscated_xpaths, line_count) = process_csv_to_new_csv(pathToXPath, options.csv_column, options.csv_delimiter, options.output_csv)
        print(f"Output new CSV file with {line_count} obfuscated XPaths at {options.output_csv}")
        return
    else:
        obfuscated_xpaths = process_file(path_to_xpath_only)

    if (not(options.is_keep_empties_enabled)):
        obfuscated_xpaths = list(filter(len, obfuscated_xpaths))
    obfuscated_xpaths = trim_all(obfuscated_xpaths)
    if (options.is_unique_enabled):
        obfuscated_xpaths = list(set(obfuscated_xpaths))

    print("\n".join(obfuscated_xpaths))

    suffix = ""
    print(f"# Processed {list_size_as_text(obfuscated_xpaths)} XPaths {suffix}")

if __name__ == '__main__':
    main()
