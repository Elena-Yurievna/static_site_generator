from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid Markdown syntax: missing closing delimiter {delimiter}")

        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))
                
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
            
        pattern = r"!\[(.*?)\]\((.*?)\)"
        matches = re.finditer(pattern, old_node.text)
        
        last_end = 0
        has_match = False
        
        for match in matches:
            has_match = True
            start, end = match.span()
            
            # Add text before the image
            if start > last_end:
                new_nodes.append(TextNode(old_node.text[last_end:start], TextType.TEXT))
                
            # Add the image node
            alt_text = match.group(1)
            image_url = match.group(2)
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))
            
            last_end = end
        
        # Add remaining text after the last image
        if has_match and last_end < len(old_node.text):
            new_nodes.append(TextNode(old_node.text[last_end:], TextType.TEXT))
        elif not has_match:
            new_nodes.append(old_node)
            
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
            
        # Pattern for markdown links: [text](url)
        pattern = r"\[(.*?)\]\((.*?)\)"
        matches = re.finditer(pattern, old_node.text)
        
        last_end = 0
        has_match = False
        
        for match in matches:
            has_match = True
            start, end = match.span()
            
            # Add text before the link
            if start > last_end:
                new_nodes.append(TextNode(old_node.text[last_end:start], TextType.TEXT))
                
            # Add the link node
            link_text = match.group(1)
            link_url = match.group(2)
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            
            last_end = end
        
        # Add remaining text after the last link
        if has_match and last_end < len(old_node.text):
            new_nodes.append(TextNode(old_node.text[last_end:], TextType.TEXT))
        elif not has_match:
            new_nodes.append(old_node)
            
    return new_nodes