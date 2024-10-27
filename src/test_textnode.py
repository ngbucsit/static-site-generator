import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is also a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_invalid_text_type(self):
        with self.assertRaises(Exception):
            TextNode("This is a text node", "bold")

    def test_default_url(self):
        node = TextNode("This is a text node without a url", TextType.NORMAL)
        self.assertIsNone(node.url)


if __name__ == "__main__":
    unittest.main()
