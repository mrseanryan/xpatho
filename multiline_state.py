"""
Combine a multiline XPath into just 1 line
"""

class MultilineState:
    def __init__(self):
        self.balance = 0
        self.sub_lines = []

    def is_line_balanced(self, line):
        openings_count = line.count('[')
        closings_count = line.count(']')
        self.balance = self.balance + openings_count - closings_count
        self.sub_lines.append(line)
        return self.balance == 0

    def _trim_all(self, texts):
        return [t.strip() for t in texts]

    def get_combined(self):
        if (self.balance != 0):
            raise Exception("Error - you should only call get_combined() if the multiline is balanced!")
        return " ".join(self._trim_all(self.sub_lines))
