import os
import shutil
from create_public import create_public_files

dir_path_static = "./static"
dir_path_public = "./public"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    create_public_files("./static", "./public")


main()
