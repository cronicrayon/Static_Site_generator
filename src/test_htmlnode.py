import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_empty_node(self):
        node = HTMLNode()  # Create an empty node
        self.assertIsNone(node.tag)  # Ensure `tag` is None
        self.assertIsNone(node.value)  # Ensure `value` is None
        self.assertIsNone(node.children)  # Ensure `children` is an empty list
        self.assertIsNone(node.props)  # Ensure `props` is an empty dict

    def test_props_to_html(self):
        # Create an HTMLNode with certain properties
        props = {
            "href": "https://www.example.com",
            "target": "_blank",
        }
        node = HTMLNode(tag="a", value="", children=None, props=props)
        
        # Call the method you're testing
        result = node.props_to_html()
        
        # Assert it returns the expected string
        self.assertEqual(result, ' href="https://www.example.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()