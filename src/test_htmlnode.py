import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        test_props = {"a": 1, "b": 2, "c": 3}
        node = HTMLNode(props=test_props)
        expected = ' a="1" b="2" c="3"'
        self.assertEqual(node.props_to_html(), expected)

    def test_empty_props_to_html(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_values(self):
        node = HTMLNode(
            "div",
            "Div text"
        )
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Div text")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode(
            "p",
            "Paragraph text",
            None,
            {"class": "a"}
        )
        expected = "HTMLNode(p, Paragraph text, children: None, {'class': 'a'})"
        self.assertEqual(node.__repr__(), expected)


if __name__ == "__main__":
    unittest.main()
