import unittest

from textnode import TextNode
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is some `code over here` and more", "text")
        self.assertEqual(
            split_nodes_delimiter([node], "`", "text"),
            "[TextNode(This is some , text, None), TextNode(code over here, text, None), TextNode( and more, text, None)]",
        )
