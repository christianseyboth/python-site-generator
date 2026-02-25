from enum import Enum
from inspect import cleandoc
from shlex import join

from htmlnode import HTMLNode, ParentNode
from text_to_text_nodes import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    return [b.strip() for b in blocks if b.strip()]


def block_to_block_type(md):
    if (
        md.startswith("# ")
        or md.startswith("## ")
        or md.startswith("### ")
        or md.startswith("#### ")
        or md.startswith("##### ")
        or md.startswith("###### ")
    ):
        return BlockType.HEADING

    elif md.startswith("```\n") and md.endswith("```"):
        return BlockType.CODE

    elif md.startswith(">"):
        lines = md.split("\n")
        is_quote = all(line.startswith(">") for line in lines)

        if is_quote:
            return BlockType.QUOTE

    elif md.startswith("- "):
        lines = md.split("\n")
        is_unordered_list = all(line.startswith("- ") for line in lines)

        if is_unordered_list:
            return BlockType.UNORDERED_LIST

    elif md.startswith("1. "):
        lines = md.split("\n")
        is_ordered_list = all(
            line.startswith(f"{index + 1}. ") for index, line in enumerate(lines)
        )

        if is_ordered_list:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []

    for block in blocks:
        type = block_to_block_type(block)

        if type == BlockType.PARAGRAPH:
            lines = block.split("\n")
            cleaned = [line.strip() for line in lines if len(line) != 0]
            children = text_to_children(" ".join(cleaned))
            block_nodes.append(ParentNode("p", children))

        if type == BlockType.HEADING:
            heading = strip_and_convert_headings(block)
            stripped = block.lstrip("# ")

            children = text_to_children(stripped)
            block_nodes.append(ParentNode(heading, children))

        if type == BlockType.CODE:
            stripped = block[4:-3]
            inner = TextNode(stripped, TextType.CODE)
            block_nodes.append(ParentNode("pre", [text_node_to_html_node(inner)]))

        if type == BlockType.QUOTE:
            stripped = strip_and_convert_quotes(block)
            children = text_to_children(stripped)
            block_nodes.append(ParentNode("blockquote", children))

        if type == BlockType.ORDERED_LIST:
            children = strip_and_convert_olist(block)
            block_nodes.append(ParentNode("ol", children))

        if type == BlockType.UNORDERED_LIST:
            children = strip_and_convert_ulist(block)
            block_nodes.append(ParentNode("ul", children))

    return ParentNode("div", block_nodes)


def text_to_children(text):
    nodes = text_to_textnodes(text)

    return [text_node_to_html_node(text_node) for text_node in nodes]


def strip_and_convert_headings(text):
    hash_count = 0

    for char in text.strip():
        if char != "#":
            break
        hash_count += 1

    return f"h{hash_count}"


def strip_and_convert_quotes(text):
    lines = text.split("\n")
    cleaned = [line.strip("> ", 1) for line in lines if len(line) != 0]
    return " ".join(cleaned)


def strip_and_convert_olist(text):
    lines = text.split("\n")
    cleaned = []
    children = []

    for line in lines:
        if len(line) != 0:
            stripped = line.split(". ", 1)
            cleaned.append(stripped[1])

    for line in cleaned:
        children.append(ParentNode("li", text_to_children(line)))

    return children


def strip_and_convert_ulist(text):
    lines = text.split("\n")
    cleaned = [line.lstrip("- ", 1) for line in lines if len(line) != 0]
    children = []

    for line in cleaned:
        children.append(ParentNode("li", text_to_children(line)))

    return children


md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""


node = markdown_to_html_node(md)
html = node.to_html()

print(html)
