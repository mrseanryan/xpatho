#! python3
"""
xpatho.py
Author: Sean Ryan
Version: 1.0

A command line tool to obfuscate XPath expressions (replacing any IP sensitive parts)

Usage: xpatho.py <path to text file containing XPath expressions> [options]

The options are:
[-e --empty (Do not omit empty XPaths)]
[-h --help]
[-u --unique (Omit duplicates)]

Examples: [Windows]
xpatho.py testData\\xpaths_1.txt
xpatho.py \\data\\xpaths_1.txt

Examples: [Unix/Mac]
xpatho.py ./testData/xpaths_1.txt
xpatho.py /data/xpaths_1.txt
"""

from functools import reduce
from operator import delitem
from optparse import OptionParser
import os
import sys
from multiline_state import MultilineState

import xpath_obfuscator

# usage() - prints out the usage text, from the top of this file :-)
def usage():
    print(__doc__)

# optparse - parse the args
parser = OptionParser(
    usage='%prog <path to text file containing XPath expressions> [options]')
parser.add_option('-e', '--empty', dest='is_keep_empties_enabled', action='store_const',
                const=True, default=False,
                help='Also output empty XPaths')
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
    raise Exception("For a CSV file, please instead use 'xpath_csv.py'")

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

def main():
    path_to_xpath_only = pathToXPath

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
