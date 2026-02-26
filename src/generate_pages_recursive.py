import os
import pathlib

from extract_title import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content):
        raise Exception("Content Path does not exist!")

    dir_content = os.listdir(dir_path_content)

    for content in dir_content:
        source_path = os.path.join(dir_path_content, content)
        dest_path = os.path.join(dest_dir_path, content)
        if os.path.isfile(source_path):
            if content.endswith(".md"):
                generate_page(
                    source_path,
                    template_path,
                    pathlib.Path(dest_path).with_suffix(".html"),
                )
        else:
            generate_pages_recursive(source_path, template_path, dest_path)
