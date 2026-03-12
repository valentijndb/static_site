class HTMLNode:
    
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""
        
        output = ""
        for k,v in self.props.items():
            output += f" {k}=\"{v}\""
        
        return output

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")

        if self.tag == None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("tag is mandatory")

        if self.children is None:
            raise ValueError("you cannot have a parentnode without children")
        
        output = f"<{self.tag}{self.props_to_html()}>"
        
        for child in self.children:
            output+= child.to_html()
        output += f"</{self.tag}>"

        return output

    def __repr__(self):
            return f"ParentNode({self.tag}, children: {self.children}, {self.props})"