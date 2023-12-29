from datetime import datetime
import os
import subprocess
import platform

# Current date in the desired format
current_date = datetime.now().strftime("%Y-%m-%d")

# Function to get the post name from the user
def get_post_name():
    post_name = input("Enter the name of the post: ")
    file_post_name = post_name.replace(" ", "-")
    return post_name, file_post_name

# Function to open the /img/ directory in file explorer
def open_image_directory():
    img_path = os.path.abspath("./img/")
    if platform.system() == "Windows":
        os.startfile(img_path)
    elif platform.system() == "Darwin":  # macOS
        subprocess.Popen(["open", img_path])
    else:  # Linux and other OS
        subprocess.Popen(["xdg-open", img_path])

    return input("Enter the path of the chosen image or press Enter to skip: ")

# Get the post name and formatted name
post_name, file_post_name = get_post_name()

# Open image directory and get image path from user
image_path = open_image_directory()

# Use the chosen image or the default placeholder
image_path = image_path or "/img/replace.jpg"

# Template for the markdown file content with dynamic header and image
markdown_template = f"""---
date: {current_date}
header:
  teaser: {image_path}
  overlay_image: {image_path}
  overlay_filter: 0.8
toc: true
toc_label: "Contents"
---

# {post_name}

Lorem Ipsum"""

# File name for the new markdown file
file_name = f"{current_date}-{file_post_name}.md"

# Function to create and write the markdown file
def create_markdown_file(file_name, content):
    folder_path = "./_posts/"  # Replace with the desired folder path
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "w") as file:
        file.write(content)
    return f"File '{file_path}' created successfully."

# Create the markdown file
create_markdown_file(file_name, markdown_template)
