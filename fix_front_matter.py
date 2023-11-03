import os

def clean_front_matter(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    start_idx = content.find('\\---') if '\\---' in content else content.find('---')
    end_idx = content.rfind('\\---') if '\\---' in content else content.rfind('---')

    if start_idx != -1 and end_idx != -1:
        front_matter = content[start_idx:end_idx+3]

        front_matter = front_matter.replace('\\', '')

        lines = front_matter.split('\n')
        cleaned_lines = []
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                cleaned_lines.append(f'{key.strip()}:\n  {value.strip()}')
            else:
                cleaned_lines.append(line)
        cleaned_front_matter = '\n'.join(cleaned_lines)

        new_content = content[:start_idx] + cleaned_front_matter + content[end_idx+3:]
        with open(file_path, 'w') as f:
            f.write(new_content)

def clean_end_front_matter(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Find the last occurrence of "---"
    for i in range(len(lines) - 1, -1, -1):
        line = lines[i].rstrip()
        if "---" in line:
            # Remove the last occurrence of "---"
            lines.pop(i)
            break

    # Add the "---" back at the end of the file
    lines.append('---\n')

    # Write the file back
    with open(file_path, 'w') as f:
        f.writelines(lines)

def clean_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                print(f'Cleaning {file_path}...')
                clean_front_matter(file_path)
                clean_end_front_matter(file_path)

# Test the function with your directory path
directory_path = "./_posts"
clean_directory(directory_path)
