import re
from textnode import TextNode, TextType
from splitnode import split_nodes_delimiter

def extract_image_nodes(text):
    pattern = r'!\[(.*?)\]\((.*?)\)'
    matches = re.finditer(pattern, text)
    nodes = []
    last_index = 0
    for match in matches:
        if match.start() > last_index:
            nodes.append(TextNode(text[last_index:match.start()], TextType.TEXT))
        nodes.append(TextNode(match.group(1), TextType.IMAGE, match.group(2)))
        last_index = match.end()
    if last_index < len(text):
        nodes.append(TextNode(text[last_index:], TextType.TEXT))
    return nodes

def extract_link_nodes(text):
    pattern = r'\[(.*?)\]\((.*?)\)'
    matches = re.finditer(pattern, text)
    nodes = []
    last_index = 0
    for match in matches:
        if match.start() > last_index:
            nodes.append(TextNode(text[last_index:match.start()], TextType.TEXT))
        nodes.append(TextNode(match.group(1), TextType.LINK, match.group(2)))
        last_index = match.end()
    if last_index < len(text):
        nodes.append(TextNode(text[last_index:], TextType.TEXT))
    return nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    
    new_nodes = []
    for node in nodes:
        if node.text_type == TextType.TEXT:
            new_nodes.extend(extract_image_nodes(node.text))
        else:
            new_nodes.append(node)
    nodes = new_nodes

    new_nodes = []
    for node in nodes:
        if node.text_type == TextType.TEXT:
            new_nodes.extend(extract_link_nodes(node.text))
        else:
            new_nodes.append(node)
    nodes = new_nodes

    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

    return nodes
