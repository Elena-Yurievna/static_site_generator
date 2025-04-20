import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_page_recursive

def main():
    content_dir = "./content"
    template_path = "./template.html"
    output_dir = "./docs"
    static_dir = "./static"
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"

    print(f"Using base path: {base_path}")

    print("Deleting output directory...")
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    print("Copying static files...")
    copy_files_recursive(static_dir, output_dir)

    print("Generating pages...")
    generate_page_recursive(content_dir, template_path, output_dir, base_path)

if __name__ == "__main__":
    main()