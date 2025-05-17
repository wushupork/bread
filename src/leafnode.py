from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    """
    A class representing a leaf node in an HTML tree.
    Inherits from HtmlNode.
    """

    def __init__(self, tag: str, value: str = None, props: dict = None):
        """
        Initialize a LeafNode with a tag, value, and optional properties.

        :param tag: The HTML tag of the node.
        :param value: The text content of the node.
        :param props: Optional dictionary of properties for the node.
        """
        super().__init__(tag, value, [], props)
        
    def to_html(self) -> str:
        """
        Convert the LeafNode to its HTML representation.

        :return: A string representing the HTML of the node.
        """
        props_html = self.props_to_html()
        if self.value:
            return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
        else:
            raise ValueError("LeafNode must have a value to convert to HTML.")
        
    