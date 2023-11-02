import os
import requests
from bs4 import BeautifulSoup

# Define directories and new image path
src_html_dir = "import_squarespace/_postsog/"
dest_img_dir = "/assets/images/old_blog"
new_img_path_url = "/assets/images/old_blog"

os.makedirs(dest_img_dir, exist_ok=True)

html_files = [f for f in os.listdir(src_html_dir) if f.endswith('.html')]

for file in html_files:
    try:  
        with open(os.path.join(src_html_dir, file), 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

        for img_tag in soup.find_all('img', src=lambda s: 'squarespace-cdn.com' in s):
            img_name = img_tag['src'].split('/')[-1]
            
            # Only download the image if it doesn't already exist locally
            if not os.path.exists(os.path.join(dest_img_dir, img_name)):
                response = requests.get(img_tag['src'], stream=True)
                if response.status_code == 200:
                    with open(os.path.join(dest_img_dir, img_name), 'wb') as img_file:
                        img_file.write(response.content)

            new_img_url = f'{new_img_path_url}/{img_name}'

            # changing the src, data-image, and srcset attributes to the new location
            img_tag['src'] = new_img_url
            if 'data-image' in img_tag.attrs:
                img_tag['data-image'] = new_img_url
            if 'srcset' in img_tag.attrs:
                img_tag['srcset'] = new_img_url

        with open(os.path.join(src_html_dir, file), 'w', encoding='utf-8') as f:
            f.write(str(soup))

    except UnicodeDecodeError:  
        print(f"UnicodeDecodeError encountered. Problem file: {file}")
        continue
