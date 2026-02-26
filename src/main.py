import os
import shutil
from create_public import create_public_files
from extract_title import generate_page
from generate_pages_recursive import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    create_public_files("./static", "./public")

    generate_pages_recursive("content", "template.html", "public")


main()
