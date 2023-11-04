import os
import re
import datetime

# Directory where your markdown files are stored
markdown_dir = './_posts_copy/'

# Function to remove the malformed frontmatter
def remove_malformed_frontmatter(content):
    # Pattern to match the malformed frontmatter section
    pattern = r"\\---.*?\\---\s*"
    # Remove the matched patterns
    cleaned_content = re.sub(pattern, '', content, flags=re.DOTALL)
    return cleaned_content

# Function to extract date from filename
def extract_date(filename):
    date_match = re.search(r'\d{4}-\d{1,2}-\d{1,2}', filename)
    if date_match:
        return datetime.datetime.strptime(date_match.group(), '%Y-%m-%d').date()
    else:
        return None

# Function to create frontmatter
def create_frontmatter(date, imgplaceholder='imgplaceholder'):
    return f"""---
date: {date}
header:
  teaser: /img/{imgplaceholder}
  overlay_image: /img/{imgplaceholder}
  overlay_filter: 0.8
toc: true
toc_label: "Contents"
--- 
"""

# Iterate through all markdown files, clean the malformed frontmatter, and add new frontmatter
for filename in os.listdir(markdown_dir):
    if filename.endswith('.md'):
        filepath = os.path.join(markdown_dir, filename)
        date = extract_date(filename)
        if date:
            with open(filepath, 'r+', encoding='utf-8') as file:
                content = file.read()
                # Remove malformed frontmatter
                content = remove_malformed_frontmatter(content)
                # Create new frontmatter
                frontmatter = create_frontmatter(date)
                # Write new frontmatter and cleaned content back to the file
                file.seek(0, 0)
                file.write(frontmatter.rstrip('\r\n') + '\n' + content)
                file.truncate()  # Truncate the file to the current position

print("Malformed frontmatter removed and new frontmatter added to all markdown files.")
