from parameterized import parameterized
import unittest

import multiline_state

class TestMultilineState(unittest.TestCase):

    def test_empty_text(self):
        state = multiline_state.MultilineState()
        self.assertTrue(state.is_line_balanced(""))
        self.assertEqual("", state.get_combined())

    def test_attempt_combine_unbalanced_line_raises(self):
        state = multiline_state.MultilineState()
        self.assertFalse(state.is_line_balanced("[ color ="))
        self.assertRaises(Exception, lambda : state.get_combined())

    @parameterized.expand([
        # balanced - single line
        ('simple XPath 1', ['[red]'],'[red]'),
        ('simple XPath 2', ['[apple/stalk]'],'[apple/stalk]'),
        ('XPath with string literal 1', ["[color = 'red']"],"[color = 'red']"),
        ('XPath with string literal 2', ["[color = 'longer_color']"],"[color = 'longer_color']"),
        ('XPath with string literal 2', ["[color = 'A1']"],"[color = 'A1']"),
        ('XPath with keywords 1', ['[red and bright]'],'[red and bright]'),
        ('XPath with keywords 2', ['[red or bright]'],'[red or bright]'),
        ('complex XPath 1', ["[Part1.StatusPart2Part3_Status/Part4.Status/StatusCode = 'X1']"], "[Part1.StatusPart2Part3_Status/Part4.Status/StatusCode = 'X1']"),
        # balanced - single line
        # xxx
        ('simple XPath 1', ['[red', ']'],'[red ]'),
        ('simple XPath 2', ['[apple / ', '  stalk]  '], '[apple / stalk]'),
        ('XPath with string literal 1', ["[color =", "  'red']"],"[color = 'red']"),
        ('XPath with string literal 2', ["[color ", "= ", "  'longer_color']"],"[color = 'longer_color']"),
        ('XPath with string literal 2', ["[color = 'A1']"],"[color = 'A1']"),
        ('XPath with keywords 1', ['[red and',' bright]'],'[red and bright]'),
        ('XPath with keywords 2', ['[red ', 'or ', 'bright]'],'[red or bright]'),
        ('complex XPath 1', ["[Part1.StatusPart2Part3_Status", "/Part4", ".Status/", "StatusCode =", " 'X1']"], "[Part1.StatusPart2Part3_Status /Part4 .Status/ StatusCode = 'X1']")

    ])
    def test_balanced_single_line(self, msg, inputs, expected):
        state = multiline_state.MultilineState()
        for x in inputs:
            state.is_line_balanced(x)
        actual_combined = state.get_combined()
        self.assertEqual(expected, actual_combined, msg)

    #xxx unbalanced
if __name__ == '__main__':
    unittest.main()
