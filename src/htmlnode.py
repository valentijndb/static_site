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
        if len(self.props) == 0:
            return ""
        
        output = ""
        for k,v in self.props.items():
            output += f" {k}=\"{v}\""
        
        return output
