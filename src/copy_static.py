import os
import shutil

def clear_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
        print(f"Cleared directory: {directory}")

def copy_directory(src, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)
        print(f"Created directory: {dest}")

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
            print(f"Copied file: {src_path} -> {dest_path}")
        elif os.path.isdir(src_path):
            copy_directory(src_path, dest_path)

def copy_static_to_public():
    clear_directory("public")
    copy_directory("static", "public")
