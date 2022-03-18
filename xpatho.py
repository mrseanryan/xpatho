#! python3
"""
xpatho.py
Author: Sean Ryan
Version: 1.0

A command line tool to obfuscate XPath expressions (replacing any IP sensitive parts)

Usage: xpatho.py <path to text file containing XPath expressions> [options]

The options are:
[-h --help]

Examples: [Windows]
xpatho.py testData\\xpaths_1.txt
xpatho.py \\data\\xpaths_1.txt

Examples: [Unix/Mac]
xpatho.py ./testData/xpaths_1.txt
xpatho.py /data/xpaths_1.txt
"""

from functools import reduce
from optparse import OptionParser
import sys

import xpath_obfuscator

# usage() - prints out the usage text, from the top of this file :-)


def usage():
    print(__doc__)



# optparse - parse the args
parser = OptionParser(
    usage='%prog <path to text file containing XPath expressions> [options]')

(options, args) = parser.parse_args()
if (len(args) != 1):
    usage()
    sys.exit(2)

pathToXPath = args[0]


def ilen(iterable):
    return reduce(lambda sum, element: sum + 1, iterable, 0)

def list_size_as_text(events):
    return str(ilen(events))

def process_file(path_to_file):
    obfuscated_xpaths = []
    with open(path_to_file) as opened_file:
        for line in opened_file:
            obfuscated_xpaths.append(xpath_obfuscator.obfuscate(line))
    return obfuscated_xpaths

def main():
    obfuscated_xpaths = process_file(pathToXPath)

    print(obfuscated_xpaths)

    print(f"Processed {list_size_as_text(obfuscated_xpaths)} XPaths")

if __name__ == '__main__':
    main()
