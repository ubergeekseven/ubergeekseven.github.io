import os
import html2text

source_directory = 'import_squarespace/_postsoriginal/'
output_directory = 'import_squarespace/mdposts/'

# Ensure output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Initialize the converter
converter = html2text.HTML2Text()
converter.ignore_links = False

# Loop through the files in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith(".html"):
        with open(os.path.join(source_directory, filename), 'r', encoding='utf-8') as file:
            html_content = file.read()
            md_content = converter.handle(html_content)
            # Save the markdown content to a new file
            with open(os.path.join(output_directory, filename.replace('.html', '.md')), 'w', encoding='utf-8') as md_file:
                md_file.write(md_content)
