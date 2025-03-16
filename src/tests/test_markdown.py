import unittest
from markdown import extract_markdown_images, extract_markdown_links, markdown_to_blocks, block_to_html_node

def test_extract_markdown_images(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


def test_extract_markdown_images_multiple(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image](https://i.imgur.com/abc.png)"
    )
    self.assertListEqual(
        [
            ("image", "https://i.imgur.com/zjjcJKZ.png"),
            ("image", "https://i.imgur.com/abc.png"),
        ],
        matches,
    )

def test_extract_markdown_images_no_images(self):
    matches = extract_markdown_images("This is text with no images")
    self.assertListEqual([], matches)

def test_extract_markdown_images_no_text(self):
    matches = extract_markdown_images("![image](https://i.imgur.com/zjjcJKZ.png)")
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

def test_extract_markdown_images_no_url(self):
    matches = extract_markdown_images("![image]")
    self.assertListEqual([], matches)

def test_ectract_markdown_links(self):
    matches = extract_markdown_links(
        "This is text with a [link](https://www.google.com)"
    )
    self.assertListEqual([("link", "https://www.google.com")], matches)


def test_extract_markdown_links_multiple(self):
    matches = extract_markdown_links(
        "This is text with a [link](https://www.google.com) and another [link](https://www.yahoo.com)"
    )
    self.assertListEqual(
        [
            ("link", "https://www.google.com"),
            ("link", "https://www.yahoo.com"),
        ],
        matches,
    )

def test_extract_markdown_links_no_links(self):
    matches = extract_markdown_links("This is text with no links")
    self.assertListEqual([], matches)

def test_markdown_to_blocks(self):
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ],
    )

def test_markdown_to_blocks_no_newlines(self):
    md = "This is a single block of text"
    blocks = markdown_to_blocks(md)
    self.assertEqual(blocks, ["This is a single block of text"])

def test_markdown_to_blocks_empty_lines(self):
    md = "\n\nThis is a block of text\n\n"
    blocks = markdown_to_blocks(md)
    self.assertEqual(blocks, ["This is a block of text"])

def test_block_to_html_node(self):
    block = "This is a paragraph"
    node = block_to_html_node(block)
    self.assertEqual(node.tag, "p")
    self.assertEqual(len(node.children), 1)
    self.assertEqual(node.children[0].tag, "text")
    self.assertEqual(node.children[0].text, "This is a paragraph")

def test_block_to_html_node_unordered_list(self):
    block = "- This is a list\n- with items"
    node = block_to_html_node(block)
    self.assertEqual(node.tag, "ul")
    self.assertEqual(len(node.children), 2)
    self.assertEqual(node.children[0].tag, "li")
    self.assertEqual(node.children[0].children[0].tag, "text")
    self.assertEqual(node.children[0].children[0].text, "This is a list")
    self.assertEqual(node.children[1].tag, "li")
    self.assertEqual(node.children[1].children[0].tag, "text")
    self.assertEqual(node.children[1].children[0].text, "with items")

if __name__ == "__main__":
    unittest.main()