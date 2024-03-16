import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ul = "unordered_list"
block_type_ol = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    if re.search(r"^#+ ", block):
        return block_type_heading
    if re.search(r"^```(.*)```$", block, re.DOTALL):
        return block_type_code
    if re.search(r"^>", block):
        return block_type_quote
    if re.search(r"^(\*|-)", block):
        return block_type_ul
    if re.search(r"^[0-9].(.*)", block, re.DOTALL):
        return block_type_ol
    return block_type_paragraph
