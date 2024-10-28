class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        html_props = ""
        if not isinstance(self.props, dict):
            return html_props
        for key, value in self.props.items():
            html_props += f'{key}="{value}" '
        return html_props[:-1]

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        self.tag = tag
        self.value = value
        self.props = props
        super().__init__(self.tag, self.value, None, self.props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if not self.tag:
            return str(self.value)
        props = " " + self.props_to_html() if self.props else ""
        return f"<{self.tag}{props}>{self.value}</{self.tag}>"
