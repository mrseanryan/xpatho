# XPathO README

A command line tool to obfuscate XPath expressions (replacing any IP sensitive parts)

# use

See the built-in help:

```
python xpatho.py
```

```
Usage: xpatho.py <path to text file containing XPath expressions> [options]

The options are:
[-h --help]

Examples: [Windows]
xpatho.py testData\xpaths_1.txt
xpatho.py \data\xpaths_1.txt

Examples: [Unix/Mac]
xpatho.py ./testData/xpaths_1.txt
xpatho.py /data/xpaths_1.txt
```

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
