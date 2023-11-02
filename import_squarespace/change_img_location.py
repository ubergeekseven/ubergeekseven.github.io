import os
import re

# Define the directory and paths
src_md_dir = "./_posts/"
old_path = "/assets/images/old_blog//"
new_path = "/assets/img/"

md_files = [f for f in os.listdir(src_md_dir) if f.endswith('.md')]

for file in md_files:
    try:  
        with open(os.path.join(src_md_dir, file), 'r', encoding='utf-8') as f:
            file_content = f.read()

        # Substitute old path with new path
        modified_content = re.sub(old_path, new_path, file_content)

        with open(os.path.join(src_md_dir, file), 'w', encoding='utf-8') as f:
            f.write(modified_content)

    except UnicodeDecodeError:  
        print(f"UnicodeDecodeError encountered. Problem file: {file}")
        continue
