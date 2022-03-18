from parameterized import parameterized
import unittest

import xpath_obfuscator

class TestDescriptionCleaner(unittest.TestCase):

    def test_empty_text(self):
        actual = xpath_obfuscator.obfuscate("")
        self.assertEqual("", actual)

    def test_plain_text(self):
        actual = xpath_obfuscator.obfuscate("Just some plain text")
        self.assertEqual("token_10000 token_10002 token_10001 token_10003", actual)

    @parameterized.expand([
        ('simple XPath 1', '[red]','[token_10000]'),
        ('simple XPath 2', '[apple/stalk]','[token_10000/token_10001]'),
        ('XPath with string literal 1', "[color = 'red']","[token_10000 = 'token_10001']"),
        ('XPath with string literal 2', "[color = 'longer_color']","[token_10000 = 'token_10001']"),
        ('XPath with string literal 2', "[color = 'A1']","[token_10000 = 'A1']"),
        ('XPath with keywords 1', '[red and bright]','[token_10001 and token_10000]'),
        ('XPath with keywords 2', '[red or bright]','[token_10001 or token_10000]'),
        ('complex XPath 1', "[Part1.StatusPart2Part3_Status/Part4.Status/StatusCode = 'X1']", "[token_10000.token_10004/token_10001.token_10002/token_10003 = 'X1']")
    ])
    def test_calculate_target_date(self, msg, input, expected):
        actual = xpath_obfuscator.obfuscate(input)
        self.assertEqual(expected, actual, msg)

if __name__ == '__main__':
    unittest.main()
