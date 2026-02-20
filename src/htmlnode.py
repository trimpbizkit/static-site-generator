class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        '''
        Constructor for HTMLNode. 
        An HTMLNode without a tag will just render as raw text.
        An HTMLNode without a vlaue will be assumed to have children.
        An HTMLNode without children will be assumed to have a value.
        An HTMLNode without props simply won't have any attributes.
        
        :param tag: A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        :param value: A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        :param children: A list of HTMLNode objects representing the children of this node
        :param props: A dictionary of key-value pairs representing the attributes of the HTML tag
        '''
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method is not yet implemented")
    
    def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return ""
        result = ""
        for k, v in self.props.items():
            result += f' {k}="{v}"'
        return result
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        '''
        Constructor for LeafNode. 
        A LeafNode is a type of HTMLNode that represents a single HTML tag with no children.
        
        :param tag: A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        :param value: A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        :param props: A dictionary of key-value pairs representing the attributes of the HTML tag
        '''
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        '''
        Constructor for ParentNode. 
        A ParentNode nests HTML nodes inside of one another.
        
        :param tag: A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        :param children: A list of HTMLNode objects representing the children of this node
        :param props: A dictionary of key-value pairs representing the attributes of the HTML tag
        '''
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
            raise ValueError("invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
