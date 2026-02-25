import unittest

from markdown_to_blocks import BlockType, block_to_block_type, markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
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

    def test_block_to_quote(self):
        md = """> erste Zeile
> zweite Zeile
> dritte Zeile"""

        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_heading(self):
        md = """### bsdfhsdjf"""
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)
