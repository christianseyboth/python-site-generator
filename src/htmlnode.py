class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""

        html = ""

        for prop, value in self.props.items():
            html += f' {prop}="{value}"'

        return html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()} {self.value}/>"

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid Tag: no value")
        if self.children is None:
            raise ValueError("Invalid children: no value")

        html = f"<{self.tag}>"

        for child in self.children:
            html += child.to_html()

        html += f"</{self.tag}>"
        return html

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
