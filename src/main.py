from textnode import TextNode
from htmlnode import ParentNode, LeafNode
from inline_markdown import split_nodes_delimiter, split_nodes_image, text_to_textnodes


def main():
    # pass
    # node1 = TextNode(
    #     "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
    #     "text",
    # )

    # node2 = TextNode(
    #     "Lorem ipsum image haha ![ipsum image](https://i.imgur.com/zjjcJKZ.png) and another ![brand new image](https://i.imgur.com/3elNhQu.png)",
    #     "text",
    # )

    print(
        text_to_textnodes(
            "This is **really** text with an image ![image](https://i.imgur.com/zjjcJKZ.png) and another *especially* good one with an image ![second image](https://i.imgur.com/3elNhQu.png)"
        )
    )

    # text_node = TextNode("This is some `code over here` and more", "text")
    # print(split_nodes_delimiter([text_node], "`", "code"))

    # parent1 = ParentNode(
    #     "div",
    #     [
    #         ParentNode(
    #             "div",
    #             [
    #                 LeafNode("p", "My paragraph. Lorem ipsum something something."),
    #             ],
    #             {"class": "paragraph"},
    #         ),
    #         LeafNode("b", "Bold text"),
    #         LeafNode(None, "Normal text"),
    #         LeafNode("i", "italic text"),
    #         LeafNode(None, "Normal text"),
    #     ],
    #     {"class": "container", "href": "htpps://nverk.me"},
    # )

    # print(parent1.to_html())


main()
