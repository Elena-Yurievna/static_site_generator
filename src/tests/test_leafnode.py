import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Click me!</a>')

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Just plain text")
        self.assertEqual(node.to_html(), "Just plain text")

    def test_leaf_no_value_raises_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_repr(self):
        node = LeafNode("p", "Hello, world!", {"class": "myClass"})
        expected = "LeafNode(p, Hello, world!, {'class': 'myClass'})"
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main()