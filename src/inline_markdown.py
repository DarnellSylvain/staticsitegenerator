import re
from textnode import TextNode, text_type_text, text_type_code


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise ValueError("Invalid node type - must be TextNode")

        if node.text_type != text_type_text:
            new_nodes.extend([node])
            continue

        split_nodes = []
        sections = node.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")

        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    image_pattern = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(image_pattern, text)


def extract_markdown_links(text):
    link_pattern = r"\[(.*?)\]\((.*?)\)"
    return re.findall(link_pattern, text)


def split_nodes_image(old_nodes):
    pass


def split_nodes_link(old_nodes):
    pass
