from blocktype import BlockType

def block_to_block_type(block):
    if block.startswith("#"):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        return BlockType.QUOTE
    elif block.startswith("- "):
        return "list"
    elif block[0].isdigit() and block[1:3] == ". ":
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH