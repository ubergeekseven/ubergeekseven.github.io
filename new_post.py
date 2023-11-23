from datetime import datetime

# Current date in the desired format
current_date = datetime.now().strftime("%Y-%m-%d")

# Template for the markdown file content
markdown_template = f"""---
date: {current_date}
header:
  teaser: /img/replace.jpg
  overlay_image: /img/replace.jpg
  overlay_filter: 0.8
toc: true
toc_label: "Contents"
--- 

# Header

Lorem Ipsum"""

# File name for the new markdown file
file_name = f"{current_date}-newpost.md"


import os

# Function to create and write the markdown file
def create_markdown_file(file_name, content):
    folder_path = "./_posts/"  # Replace with the desired folder path
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "w") as file:
        file.write(content)
    return f"File '{file_path}' created successfully."


# Create the markdown file
create_markdown_file(file_name, markdown_template)
