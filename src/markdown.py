import re
from blockparsel import block_to_block_type
from textnode import text_node_to_html_node
from text_to_textnodes import text_to_textnodes
from parentnode import ParentNode
from blocktype import BlockType

def extract_markdown_images(text):
    # Extracts all image URLs from a given text
    # and returns them as a list
    return re.findall(r"!\[.*?\]\((.*?)\)", text)

def extract_markdown_links(text):
    # Extracts all link URLs from a given text
    # and returns them as a list
    return re.findall(r"\[.*?\]\((.*?)\)", text)

def markdown_to_blocks(markdown):
    # Splits a markdown text into blocks
    # based on the presence of two newlines
    blocks = markdown.split("\n\n")
    return [block.strip() for block in blocks if block.strip()]

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    children = [block_to_html_node(block) for block in blocks]
    return ParentNode("div", children)

def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if block_type == BlockType.PARAGRAPH:
        return ParentNode("p", text_to_children(block))
    elif block_type == BlockType.UNORDERED_LIST:
        items = block.split("\n")
        children = [ParentNode("li", text_to_children(item[2:])) for item in items if item.strip()]
        return ParentNode("ul", children)
    elif block_type == BlockType.ORDERED_LIST:
        items = block.split("\n")
        children = [ParentNode("li", text_to_children(item[3:])) for item in items if item.strip()]
        return ParentNode("ol", children)
    elif block_type == BlockType.CODE:
        return ParentNode("pre", [ParentNode("code", text_to_children(block))])
    elif block_type == BlockType.QUOTE:
        return ParentNode("blockquote", text_to_children(block))
    elif block_type == BlockType.HEADING:
        level = len(block.split()[0])
        return ParentNode(f"h{level}", text_to_children(block))
    else:
        raise ValueError(f"Unknown block type: {block_type}")