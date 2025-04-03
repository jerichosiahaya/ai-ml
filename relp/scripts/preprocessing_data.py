import json
import re
from bs4 import BeautifulSoup

def main():
    data_path = ''
    mod_data_path = ''
    article_type = 'non_lestari' # lestari OR non_lestari

    with open(data_path, 'r') as file:
        data = json.load(file)

    preprocess_data(data, mod_data_path, article_type)

def clean_text(text: str):
    soup = BeautifulSoup(text, 'html.parser')
    # Remove HTML tags
    text = soup.get_text(separator=' ')
    # Remove "Baca juga" sections
    text = re.sub(r'Baca juga:.*?(\n|$)', '', text)
    # Remove unnecessary white spaces
    text = re.sub(r'\s+', ' ', text).strip()
    # Remove line breaks
    text = ''.join(part.split('\\', 1)[0] if '\\' in part else part for part in text.splitlines())
    # Remove KOMPAS.com
    text = re.sub(r'\S+\s*,?\s*KOMPAS\.com\s*-', '', text)
    # Remove date format: Jumat (11/09/2023)
    text = re.sub(r'[A-Za-z]+ \(\d{1,2}/\d{1,2}/\d{4}\)[,\.]*', '', text)
    # Remove unwanted patterns
    patterns_to_remove = ['Kompas.com', 'KOMPAS.com', '\'', '\u201c', '\u201d', '\u2013', '\u00b0', '\u2018', '\u2019']
    for pattern in patterns_to_remove:
        text = re.sub(pattern, '', text)
    # Remove unnecessary white spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def preprocess_data(input_data, output_path, article_type):
    for entry in input_data:
        # Remove unwanted fields
        entry.pop('Url', None)
        entry.pop('Tag', None)
        entry.pop('SiteName', None)

        # Set label
        if article_type == 'lestari':
            entry['label'] = 1
        else:
            entry['label'] = 0

        # Combine Title, Description and Content
        entry['text'] = f"{entry.get('Title', '')}. {entry.get('Description', '')}. {entry.get('Content', '')}"

        # Remove unwanted fields
        entry.pop('Content', None)
        entry.pop('Title', None)
        entry.pop('Description', None)

        # Clean text
        entry['text'] = clean_text(entry['text'])
    
    with open(output_path, 'w') as file:
        json.dump(input_data, file, indent=4)

    print("Data modified and saved to ", output_path)

if __name__ == "__main__":
    main()