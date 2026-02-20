from enum import Enum

from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def markdown_to_blocks(markdown) -> list[str]:
    '''
    Split the given markdown document into a list of blocks
    
    :param markdown: raw string representing a full markdown document
    :return: a list of "block" strings
    :rtype: list[str]
    '''
    blocks = []
    sections = markdown.split("\n\n")
    for section in sections:
        if len(section) == 0:
            continue
        blocks.append(section.strip())
    return blocks

def block_to_block_type(block) -> BlockType:
    '''
    Identify the type of the markdown block
    
    :param block: a single block of markdown text, assume all leading and trailing whitespace was stripped
    :return: the enum representing the identified markdown block type
    :rtype: BlockType
    '''
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        # Headings start with 1-6 # characters, followed by a space and then the heading text.
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        # Multiline Code blocks must start with 3 backticks and a newline, then end with 3 backticks.
        return BlockType.CODE
    if block.startswith(">"):
        # Every line in a quote block must start with a "greater-than" character: > followed by the quote text. 
        # A space after > is allowed but not required.
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith('- '):
        # Every line in an unordered list block must start with a - character, followed by a space.
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith('1. '):
        # Every line in an ordered list block must start with a number followed by a . character and a space.
        # The number must start at 1 and increment by 1 for each line.
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    # If none of the above conditions are met, the block is a normal paragraph.
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        html_node = block_to_html_node(block)
        block_nodes.append(html_node)
    return ParentNode("div", block_nodes)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.CODE:
            return code_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case BlockType.ULIST:
            return ulist_to_html_node(block)
        case BlockType.OLIST:
            return olist_to_html_node(block)
        case _:
            raise ValueError("invalid block type")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    size = 0
    for hash in block:
        if hash == "#":
            size += 1
        else:
            break
    if size + 1 >= len(block):
        raise ValueError(f"invalid heading size: {size}")
    text = block[size + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{size}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text_node = TextNode(block[4:-3], TextType.TEXT)
    html_node = text_node_to_html_node(text_node)
    code_node = ParentNode("code", [html_node])
    return ParentNode("pre", [code_node])

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        parts = item.split(". ", 1)
        text = parts[1]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)
