import unittest
from gencontent import (
    extract_title,
    DEFAULT_TITLE
)

class TestGencontent(unittest.TestCase):
    def test_extract_title_basic_md(self):
        md = """
# Hello
        
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        title = extract_title(md)
        self.assertEqual(
            title,
            "Hello"
        )

    def test_extract_title_md_out_of_order(self):
        md = """
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items

# Hello
        
This is **bolded** paragraph
"""
        title = extract_title(md)
        self.assertEqual(
            title,
            "Hello"
        )

    def test_extract_title_md_long_trailhead(self):
        md = "#                     Hello                       "
        title = extract_title(md)
        self.assertEqual(
            title,
            "Hello"
        )

    def test_no_title(self):
        md = "no title"
        title = extract_title(md)
        self.assertEqual(
            title,
            DEFAULT_TITLE
        )

    def test_double_title(self):
        md = """
# Title one

# Title two, will be ignored
"""
        title = extract_title(md)
        self.assertEqual(
            title,
            "Title one"
        )

if __name__ == "__main__":
    unittest.main()