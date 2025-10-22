# TempSH File Uploader

A simple Python command-line tool to upload files anonymously to [temp.sh](https://temp.sh/) - a temporary file hosting service.

## Features

- 📤 Simple file upload to temp.sh
- 🔒 Anonymous uploading (no registration required)
- 🚀 Easy to install and use
- 💻 Cross-platform compatibility

## Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Step-by-step Installation

1. **Update system packages:**
   ```bash
   sudo apt update
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Make the script executable:**
   ```bash
   sudo chmod +x tempsh.py
   ```

4. **Install system-wide (optional):**
   ```bash
   sudo cp tempsh.py /usr/local/bin/tempsh
   ```

## Usage

### Basic usage:
```bash
python3 tempsh.py filename.txt
```

### Download temp.sh file
```bash
python3 tempsh.py https://temp.sh/AwDs/filename.txt
```

### If installed system-wide:
```bash
tempsh -f filename.txt
```

### Command-line options:
- `file`: Specify the file to upload (required)

## Example upload

```bash
$ tempsh document.pdf

[*] Uploading document.pdf...
[*] https://temp.sh/abc123/document.pdf
```

## Example downlaod

```bash
$ tempsh https://temp.sh/aQdS/document.pdf

[*] Downloading file document.pdf...
[*] Saved on document.pdf
```

## Dependencies

- `requests` - For HTTP requests
- `argparse` - For command-line argument parsing

All dependencies are listed in `requirements.txt`

## How it works

The script uses the temp.sh API to upload files anonymously. Temp.sh provides temporary file hosting where files are typically available for a limited time (usually a few days).

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Feel free to submit issues and pull requests to improve this tool.

## Disclaimer

This tool is for legitimate use only. Please respect temp.sh's terms of service and only upload files you have permission to share.
