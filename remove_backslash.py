import os

# Directory containing markdown files
directory = './'

for filename in os.listdir(directory):
    # Only process .md files
    if filename.endswith('.md'):
        with open(os.path.join(directory, filename), 'r') as f:
            content = f.read()

        # Replace \--- with ---
        clean_content = content.replace(r'\---', '---')

        # Write the cleaned content back to the file
        with open(os.path.join(directory, filename), 'w') as f:
            f.write(clean_content)
