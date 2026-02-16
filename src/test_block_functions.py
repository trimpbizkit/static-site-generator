import unittest

from block_functions import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType
)

class TestBlockFunctions(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_paragraph_block(self):
        md = "A paragraph block with some **bold** text"
        type = block_to_block_type(md)
        self.assertEqual(BlockType.PARAGRAPH, type)

    def test_heading_block(self):
        md = "# This is a heading"
        type = block_to_block_type(md)
        self.assertEqual(BlockType.HEADING, type)
        md = "## This is a heading"
        type = block_to_block_type(md)
        self.assertEqual(BlockType.HEADING, type)
        md = "### This is a heading"
        type = block_to_block_type(md)
        self.assertEqual(BlockType.HEADING, type)
        md = "#### This is a heading"
        type = block_to_block_type(md)
        self.assertEqual(BlockType.HEADING, type)
        md = "##### This is a heading"
        type = block_to_block_type(md)
        self.assertEqual(BlockType.HEADING, type)
        md = "###### This is a heading"
        type = block_to_block_type(md)
        self.assertEqual(BlockType.HEADING, type)
        
    def test_code_block(self):
        md = "```\nThis is a code block\n```"
        type = block_to_block_type(md)
        self.assertEqual(BlockType.CODE, type)
    
    def test_quote_block(self):
        md = "> This is a quote block\n> Luke, I am your father\n> We are going to need a bigger boat"
        type = block_to_block_type(md)
        self.assertEqual(BlockType.QUOTE, type)

    def test_unordered_list_block(self):
        md = "- This is an unordered list\n- with\n- items"
        type = block_to_block_type(md)
        self.assertEqual(BlockType.ULIST, type)

    def test_ordered_list_block(self):
        md = "1. This is an ordered list\n2. with\n3. items"
        type = block_to_block_type(md)
        self.assertEqual(BlockType.OLIST, type)


if __name__ == "__main__":
    unittest.main()
