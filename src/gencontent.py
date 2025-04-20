import os
from markdown_blocks import markdown_to_html_node

def generate_page(from_path, template_path, dest_path, base_path="/"):
    print(f" * {from_path} -> {dest_path}")
    
    with open(from_path, "r") as f:
        markdown_content = f.read()
    with open(template_path, "r") as f:
        template = f.read()

    html = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    template = template.replace('href="/', f'href="{base_path}')
    template = template.replace('src="/', f'src="{base_path}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template)


def generate_page_recursive(content_dir, template_path, output_dir, base_path="/"):
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith(".md"):
                full_md_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_md_path, content_dir)
                relative_dir = os.path.dirname(relative_path)
                file_name = os.path.splitext(os.path.basename(file))[0]

                if file_name == "index":
                    dest_path = os.path.join(output_dir, relative_dir, "index.html")
                else:
                    dest_path = os.path.join(output_dir, relative_dir, f"{file_name}.html")

                generate_page(full_md_path, template_path, dest_path, base_path)

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")
