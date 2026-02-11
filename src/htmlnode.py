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
