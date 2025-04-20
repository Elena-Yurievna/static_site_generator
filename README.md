# 📘 static_site_generator

A simple static site generator written in Python.  
It converts Markdown (`.md`) files into styled HTML pages using a shared HTML template and publishes them with GitHub Pages.

---

## 🚀 Demo (no CSS yet)

🖥️ Live site:  
👉 [https://elena-yurievna.github.io/static_site_generator/](https://elena-yurievna.github.io/static_site_generator/)

---

## 🧱 Features

- 📝 Write content in Markdown
- 🧠 Custom `HTMLNode` classes with inline formatting support
- 🎨 Template rendering with basepath replacement
- 📁 Recursively generates pages from nested folders
- 🌍 GitHub Pages compatible (`/docs` folder deployment)
- 🧪 Fully testable with unit tests and Boot.dev CLI

---

## 📁 Project Structure

static_site_generator/
├── content/            # Your markdown files (index.md, blog/*.md, etc.)
├── docs/               # Output directory (published to GitHub Pages)
├── static/             # CSS, images, assets (copied to docs/)
├── templates/          # HTML templates with {{ Title }}, {{ Content }}
├── src/
│   ├── main.py         # Main entry point
│   ├── gencontent.py   # HTML generation logic
│   ├── copystatic.py   # File copy logic
│   ├── markdown_blocks.py, htmlnode.py, etc.
├── test.sh             # Run unit tests
├── build.sh            # Build site for GitHub Pages
├── .gitignore
└── README.md

---

## ⚙️ Usage

### 🔧 Local build and preview

./main.sh

### Generates site to docs/
Serves at http://localhost:8888
🏗️ Production (GitHub Pages) build

./build.sh
Generates site to docs/ with /static_site_generator/ as base URL.

### Writing Content
Just place Markdown files in the content/ folder.
Supports:

# headings → <h1>
**bold**, _italic_, `code`
![alt](url) images
[text](url) links
Ordered and unordered lists
Nested folders like /blog/post.md