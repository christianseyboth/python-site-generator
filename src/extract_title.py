import os

from markdown_to_blocks import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            splitted = line.split("# ")
            return splitted[1].strip()
    raise Exception("No h1 found!")


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path}, to {dest_path} using {template_path}.")

    if not os.path.exists(from_path):
        raise FileNotFoundError("Markdown File not found!")
    elif not os.path.exists(template_path):
        raise FileNotFoundError("Template File not found!")

    markdown = open(from_path).read()
    node = markdown_to_html_node(markdown)
    title = extract_title(markdown)

    template = open(template_path).read()
    html = node.to_html()

    template = (
        template.replace("{{ Title }}", title)
        .replace("{{ Content }}", html)
        .replace('href)"/', f'href="{basepath}')
        .replace('src="/', f'src="{basepath}')
    )

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    with open(dest_path, "w") as f:
        f.write(template)
