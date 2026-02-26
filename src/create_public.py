import os
import shutil


def create_public_files(source_path, destination_path):
    if not os.path.exists(destination_path):
        os.mkdir(destination_path)

    for filename in os.listdir(source_path):
        from_path = os.path.join(source_path, filename)
        dest_path = os.path.join(destination_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            create_public_files(from_path, dest_path)
