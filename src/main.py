import os
import shutil
import sys
from create_public import create_public_files
from extract_title import generate_page
from generate_pages_recursive import generate_pages_recursive

basepath = sys.argv[1] if len(sys.argv) == 2 else "/"
dir_path_static = "./static"
dir_path_public = "./docs"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    create_public_files(dir_path_static, dir_path_public)

    generate_pages_recursive("content", "template.html", "docs", basepath)


main()
