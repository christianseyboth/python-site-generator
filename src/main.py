from htmlnode import HTMLNode, ParentNode
from leafnode import LeafNode
from splitnodedelimiter import split_nodes_delimiter
from textnode import TextNode, TextType


def main():
    text_node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    html_node = HTMLNode(
        "p",
        "test",
        None,
        {
            "href": "https://www.google.com",
            "target": "_blank",
        },
    )

    leaf_node = LeafNode("p", "Hello World!")

    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    node3 = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node3], "`", TextType.CODE)
    print(new_nodes)


main()
