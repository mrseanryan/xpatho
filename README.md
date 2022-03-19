# XPathO README :negative_squared_cross_mark:

A command line tool to obfuscate XPath expressions (replacing any IP sensitive parts)

# how to use

## use - reading a plain text file with 1 XPath per line

See the built-in help:

```
python xpatho.py
```

```
Usage: xpatho.py <path to text file containing XPath expressions> [options]

The options are:
[-c --csv_column (If reading a CSV file, specifies which column to read, using a 0-based index)]
[-d --csv_delimiter (If reading a CSV file, specifies the field delimiter)]
[-e --empty (Do not omit empty XPaths)]
[-h --help]
[-o --output_csv (If reading a CSV file, this is the path to the new output CSV file)]
[-u --unique (Omit duplicates)]

Examples: [Windows]
xpatho.py testData\xpaths_1.txt -u
xpatho.py \data\xpaths_1.txt -u -e

Examples: [Unix/Mac]
xpatho.py ./testData/xpaths_1.txt -u
xpatho.py /data/xpaths_1.txt -u -e
```

## examples

| Description | Input | Obfuscated Output |
|---|---|---|
| XPath with keywords 1 | `[red and bright]` | `[token_10001 and token_10000]` |
| XPath with keywords 2 | `[red or bright]` | `[token_10001 or token_10000]` |
| Complex XPath 1 | `[Part1.StatusPart2Part3_Status/Part4.Status/StatusCode = 'X1']` | `[token_10000.token_10004/token_10001.token_10002/token_10003 = 'X1']` |

## notes

- by default, empty XPaths are omitted. See the options for how to override this.
- very short tokens (less than 3 letters) are not obfuscated

# use - reading a CSV file where 1 column has XPaths that need to be obfuscated

See the built-in help:

```
python xpatho_csv.py
```

```
Usage: xpatho_csv.py <path to CSV file containing XPath expressions> <path to output CSV file> [options]

The options are:
[-c --csv_column (If reading a CSV file, specifies which column to read, using a 0-based index)]
[-d --csv_delimiter (If reading a CSV file, specifies the field delimiter)]
[-h --help]
[-o --csv_output_delimiter (The column/field delimiter to use in the output CSV file)]

Examples: [Windows]
xpatho_csv.py testData\\xpaths_1.csv temp\\xpaths_1.obfuscated.csv -csv_column 1
xpatho_csv.py \\data\\xpaths_2.csv temp\\xpaths_2.obfuscated.csv -csv_column 1

Examples: [Unix/Mac]
xpatho_csv.py ./testData/xpaths_1.csv temp/xpaths_1.obfuscated.csv -csv_column 1
xpatho_csv.py /data/xpaths_2.csv temp/xpaths_2.obfuscated.csv -csv_column 1
```

## notes

- very short tokens (less than 3 letters) are not obfuscated

# setup

1. Install Python 3.7.x and pip

- Python 3.7.9 or later
- pip 21.3.1 or later

2. Install dependencies

```
pip install -r pip.config
```

# libraries used

xpatho uses a few nice libraries:

| Library       | URL                                             | Description                                              |
| ------------- | ----------------------------------------------- | -------------------------------------------------------- |
| parameterized | https://pypi.org/project/parameterized/         | Easily parameterize your unit tests                      |

# tools used

| Tool | URL                           | Description                                                                                                               |
| ---- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| pip  | https://pypi.org/project/pip/ | pip used with a config file, makes it easy to restore a Python project on another machine (even between Windows and Mac!) |

# license

License is [MIT](./LICENSE)
