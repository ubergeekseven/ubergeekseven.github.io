import os
import re

def format_date(date_str):
    # Split the date and convert each part to an integer to remove leading zeros, then convert back to string
    parts = date_str.split('-')
    return '-'.join(str(int(part)) for part in parts)

def remove_second_date(filename):
    # Adjusted regular expression to correctly capture individual date components
    date_pattern = r'(\d{4})-(\d{1,2})-(\d{1,2})-(\d{4})-(\d{1,2})-(\d{1,2})-(.*)'
    match = re.match(date_pattern, filename)
    if match:
        # Format the first date to remove leading zeros
        first_date = format_date(f"{match.group(1)}-{match.group(2)}-{match.group(3)}")
        # Reconstruct the filename with the formatted first date and the remaining parts
        return f"{first_date}-{match.group(7)}"
    else:
        return filename

def rename_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            try:
                new_filename = remove_second_date(filename)
                if new_filename != filename:
                    old_file = os.path.join(directory, filename)
                    new_file = os.path.join(directory, new_filename)
                    if not os.path.exists(new_file):
                        os.rename(old_file, new_file)
                        print(f"Renamed '{filename}' to '{new_filename}'")
                    else:
                        print(f"Error: Cannot rename '{filename}' to '{new_filename}' because the new file name already exists.")
            except OSError as e:
                print(f"Error: {e.strerror} while renaming '{filename}'.")

# Set your directory path here
directory_path = './_posts_copy/'
rename_files_in_directory(directory_path)
