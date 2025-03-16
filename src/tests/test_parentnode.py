import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "More normal text"),
            ],
        )
        expected_html = "<p><b>Bold text</b>Normal text<i>Italic text</i>More normal text</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_parent_with_props(self):
        node = ParentNode(
            "div",
            [
                LeafNode("span", "Inside div"),
            ],
            {"class": "container"}
        )
        expected_html = '<div class="container"><span>Inside div</span></div>'
        self.assertEqual(node.to_html(), expected_html)

    def test_parent_without_tag_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "Some text")])

    def test_parent_without_children_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode("p", None)

    def test_repr(self):
        node = ParentNode("ul", [LeafNode("li", "Item 1"), LeafNode("li", "Item 2")])
        expected_repr = "ParentNode(ul, [LeafNode(li, Item 1, None), LeafNode(li, Item 2, None)], None)"
        self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()