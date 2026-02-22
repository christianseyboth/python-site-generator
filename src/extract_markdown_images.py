import re
from typing import Text

from textnode import TextNode, TextType


def extract_markdown_images_and_links(text):
    rexed = re.findall(r"\[(.*?)\]\((http.*?)\)", text)

    return rexed


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        remaining_text = node.text

        for image_alt, image_link in images:
            sections = remaining_text.split(f"![{image_alt}]({image_link})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")

            link_node = []

            if len(sections[0]) != 0:
                link_node.append(TextNode(sections[0], TextType.TEXT))
            link_node.append(TextNode(image_alt, TextType.IMAGE, image_link))

            new_nodes.extend(link_node)
            remaining_text = sections[-1]

        if len(remaining_text) != 0:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        remaining_text = node.text

        if len(links) == 0:
            new_nodes.append(node)

        for link_target, link_url in links:
            sections = remaining_text.split(f"[{link_target}]({link_url})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")

            link_node = []

            if len(sections[0]) != 0:
                link_node.append(TextNode(sections[0], TextType.TEXT))
            link_node.append(TextNode(link_target, TextType.LINK, link_url))

            new_nodes.extend(link_node)
            remaining_text = sections[-1]

    if len(remaining_text) != 0:
        new_nodes.append(TextNode(remaining_text))

    return new_nodes
