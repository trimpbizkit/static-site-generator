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
