import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_page_recursive

content_dir = "./content"
template_path = "./template.html"
public_dir = "./public"
static_dir = "./static"

def main():
    print("Deleting public directory...")
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)

    print("Copying static files...")
    copy_files_recursive(static_dir, public_dir)

    print("Generating pages...")
    generate_page_recursive(content_dir, template_path, public_dir)

if __name__ == "__main__":
    main()