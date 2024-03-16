import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        input_nodes = [TextNode("This is some `code over here` and more", "text")]
        expected_output = [
            TextNode("This is some ", "text"),
            TextNode("code over here", "code"),
            TextNode(" and more", "text"),
        ]

        self.assertEqual(
            split_nodes_delimiter(input_nodes, "`", "code"),
            expected_output,
        )

    def test_text_to_textnodes(self):
        input_text = "This is **really** text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another *especially* ![second image](https://i.imgur.com/3elNhQu.png)"
        expected_output = [
            TextNode("This is ", text_type_text, None),
            TextNode("really", text_type_bold, None),
            TextNode(" text with an ", text_type_text, None),
            TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text, None),
            TextNode("especially", text_type_italic, None),
            TextNode(" ", text_type_text, None),
            TextNode(
                "second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
            ),
        ]
        self.assertEqual(text_to_textnodes(input_text), expected_output)
