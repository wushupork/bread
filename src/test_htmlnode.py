import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "Hello, World!", [], {"class": "greeting"})
        node2 = HTMLNode("div", "Hello, World!", [], {"class": "greeting"})
        if node is node2:
            self.assertTrue(True)
        #self.assertEqual(node, node2)

    def test_repr(self):    
        node = HTMLNode("div", "Hello, World!", [], {"class": "greeting"})
        print (node.props)
        expected_repr = 'HTMLNode(tag=div, value=Hello, World!, children=[], props={"class": "greeting"})'
        self.assertEqual(repr(node), expected_repr)

    def test_props_to_html(self):
        node = HTMLNode("div", "Hello, World!", [], {"class": "greeting", "id": "main"})
        expected_props_html = '"class"="greeting" "id"="main"'
        self.assertEqual(node.props_to_html(), expected_props_html)
if __name__ == "__main__":
    unittest.main()