from enum import Enum

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
