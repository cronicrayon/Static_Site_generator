import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD, "wwww.test.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "wwww.test.com")
        self.assertEqual(node, node2)

    def test_misgrammer(self):
        node = TextNode("This is a text node", TextType.BOLD, "wwww.test.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "wwww.test.com")
        self.assertEqual(node, node2)

    def test_wrong_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "wwww.test.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "wwww.test.com")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
