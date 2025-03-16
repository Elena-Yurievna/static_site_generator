import unittest
from htmlnode import HTMLNode
from enum import Enum

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertTrue(result.startswith(" "))
        self.assertIn('href="https://www.google.com"', result)
        self.assertIn('target="_blank"', result)
    
    def test_repr(self):
        node = HTMLNode(tag="p", value="Hello, world!", children=None, props={"class": "myClass"})
        expected = "HTMLNode(p, Hello, world!, None, {'class': 'myClass'})"
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main()
