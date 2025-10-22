#!/usr/bin/env python3

import requests
import argparse

def upload(file_n):
    try:
        url = "https://temp.sh/upload"
        with open(file_n, 'rb') as f:
            file = {'file': f}
            
            menu_text = f"\n[*] Uploading {file_n}..."
            print(menu_text)
            
            req = requests.post(url, files=file)
            uplink = req.text

            print(f'[*] {uplink}\n')
        
    except Exception as e:
        print(e)

def main():
    parser = argparse.ArgumentParser(description="A simple script to upload files anonymously to https://temp.sh/")
    parser.add_argument('-f', '--file', type=str, required=True, help='File to upload')
    args = parser.parse_args()

    file_n = args.file
    
    upload(file_n=file_n)

if __name__ == "__main__":
    main()
