from textnode import TextNode
from htmlnode import (
    ParentNode,
    LeafNode
)

def main():
    parent1 = ParentNode(
        "div",
        [   
            ParentNode(
                "div",
                [
                    LeafNode("p", "My paragraph. Lorem ipsum something something."),
                ],
                {
                    "class": "paragraph"
                },
            ),
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        
        {
            "class": "container", 
            "href": "htpps://nverk.me"
        },
    )

    print(parent1.to_html())
    


main()