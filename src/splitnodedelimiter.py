from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    n_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            n_nodes.append(node)
            continue

        if node.text.count(delimiter) % 2 != 0:
            raise Exception(
                "Check the markdwon syntax, a closing delimiter sign is missing"
            )

        parts = node.text.split(delimiter)

        for i in range(len(parts)):
            if parts[i] == "":
                continue
            if i % 2 == 0:
                n_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                n_nodes.append(TextNode(parts[i], text_type))

    return n_nodes
