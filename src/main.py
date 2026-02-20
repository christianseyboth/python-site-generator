from htmlnode import HTMLNode
from textnode import TextNode


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

    html = html_node.props_to_html()
    print(html)


main()
