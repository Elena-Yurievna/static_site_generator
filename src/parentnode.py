from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("ParentNode must have a tag")
        if not children:
            raise ValueError("ParentNode must have at least one child")

        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        children_html = ''.join(child.to_html() for child in self.children)
        props_html = self.props_to_html()
        props_html = f"{props_html}" if props_html else ""
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"