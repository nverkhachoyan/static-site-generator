class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("This method must be overridden by child classes.")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_result = ""
        for prop, prop_value in self.props.items():
            props_result = props_result + f' {prop}="{prop_value}"'
        return props_result

    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self,  tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: {self.tag} tag requires value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: Parent node requires a tag")
        if self.children is None:
            raise ValueError("Invalid HTML: Parent node requires children")
        
        start_tag = f"<{self.tag}{self.props_to_html()}>"
        children_html = ""

        for child in self.children:
            children_html = children_html + child.to_html()
        
        end_tag = f"</{self.tag}>"
        
        return f"{start_tag}{children_html}{end_tag}"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"



        
    

            
        
