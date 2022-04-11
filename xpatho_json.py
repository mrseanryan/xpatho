#! python3
"""
xpatho_json.py
Author: Sean Ryan
Version: 1.0

A command line tool to obfuscate XPath expressions (replacing any IP sensitive parts)

Usage: xpatho_json.py <path to JSON file containing XPath expressions> [options]

The options are:
[-h --help]

Examples: [Windows]
xpatho.py testData\\xpaths_1.json
xpatho.py \\data\\xpaths_1.json

Examples: [Unix/Mac]
xpatho.py ./testData/xpaths_1.json
xpatho.py /data/xpaths_1.json
"""

from optparse import OptionParser
import os
import sys
import json

import xpath_obfuscator

# usage() - prints out the usage text, from the top of this file :-)
def usage():
    print(__doc__)

# optparse - parse the args
parser = OptionParser(
    usage='%prog <path to JSON file containing XPath expressions> [options]')

(options, args) = parser.parse_args()
if (len(args) != 1):
    usage()
    sys.exit(2)

pathToXPath = args[0]

def is_json_file(filePath):
    extension = os.path.splitext(filePath)[1]
    return extension.lower() == ".json"

if not is_json_file(pathToXPath):
    raise Exception("This command is only for JSON files (the filename must end in '.json'")

def process_file(path_to_file):
    obfuscated_xpath_count = 0
    json_out = {}
    with open(path_to_file, encoding="utf8") as opened_file:
        data = json.load(opened_file)
        for e in data: 
            content = data[e]
            json_out[e] = []
            for entry in content:
                projectId = entry['projectid']
                xpath = entry['xpath']
                obfuscated_xpath = xpath_obfuscator.obfuscate(xpath)
                json_out[e].append({'projectid': projectId, 'xpath': obfuscated_xpath})
                obfuscated_xpath_count = obfuscated_xpath_count + 1
    print(json.dumps(json_out, indent=4, sort_keys=True))

def main():
    path_to_xpath_only = pathToXPath
    process_file(path_to_xpath_only)

if __name__ == '__main__':
    main()
