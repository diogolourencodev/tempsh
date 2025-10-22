#!/usr/bin/env python3

import requests
import argparse

def upload(file_n):
    try:
        if file_n.startswith('https://temp.sh/'):
            req = requests.post(file_n)
            
            file_name = file_n.split('/')[-1]
            
            menu_text = f"\n[*] Downloading file {file_name}..."
            print(menu_text)
            
            with open(file_name, 'w') as out:
                out.write(req.text)
            print(f'[*] Saved on {file_name}\n')
        else:
            url = "https://temp.sh/upload"
            with open(file_n, 'rb') as f:
                file = {'file': f}
                
                menu_text = f"\n[*] Uploading {file_n}..."
                print(menu_text)
                
                req = requests.post(url, files=file)
                uplink = req.text

                print(f'[*] {uplink}\n')
        
    except Exception as e:
        print(f'error: {e}')

def main():
    parser = argparse.ArgumentParser(description="A simple script to upload files anonymously to https://temp.sh/")
    parser.add_argument('file', help='File to upload')

    args = parser.parse_args()

    file_n = args.file
    
    upload(file_n=file_n)

if __name__ == "__main__":
    main()
