import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a", "google", props={"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.props_to_html(), 'href="https://www.google.com" target="_blank"'
        )
