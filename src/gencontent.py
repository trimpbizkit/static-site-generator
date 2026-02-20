import os
from pathlib import Path

from markdown_blocks import markdown_to_html_node
from logger_singleton import LoggerSingleton as logger

DEFAULT_TITLE = "My Statically Generated Site"

def extract_title(markdown):
    '''
    Pull the h1 header from the markdown file (the line that starts with a single #) and return it.
    If there is no h1 header, log a warning and return default value.
    '''
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    logger.warn("no title extracted, using default")
    return DEFAULT_TITLE


def generate_page(from_path, template_path, dest_path):
    '''
    Read the markdown file at from_path and store the contents in a variable.
    Read the template file at template_path and store the contents in a variable.
    Use markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
    Use the extract_title function to grab the title of the page.
    Replace the {{ Title }} and {{ Content }} placeholders in the template.
    Write the new full HTML page to a file at dest_path. 
    Create any necessary directories if they don't exist.
    '''
    logger.info(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as file:
        markdown_content = file.read()
    with open(template_path, 'r') as file:
        template = file.read()
    
    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace(r"{{ Title }}", title, 1)
    template = template.replace(r"{{ Content }}", html, 1)
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, 'w') as file:
        file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    '''
    Crawl every entry in the content directory
    For each markdown file found, generate a new .html file using the same template.html.
    The generated pages should be written to the public directory in the same directory structure.
    '''
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            if Path(dest_path).suffix == ".md":
                dest_path = Path(dest_path).with_suffix(".html")
                generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
    