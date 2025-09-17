# RemoteZip MCP Server

An MCP server that provides tools for accessing remote zip files over HTTP, HTTPS, and FTP protocols without downloading the entire archive.

## Features

- List files in remote zip archives
- Extract individual files from remote zip archives
- Get file information and statistics
- Support for HTTP, HTTPS, and FTP protocols
- Partial reading - only downloads necessary parts of the zip file

## Installation

1. Install Python 3.10 or higher
2. Install dependencies:
   ```bash
   pip install -e .
   ```

## Usage

Run the server:
```bash
python remotezip_server.py
```

## Tools

- `list_files(url)`: Get list of files in the archive
- `extract_file(url, filename, local_path)`: Extract a file to local storage
- `get_file_info(url, filename)`: Get details about a specific file
- `get_zip_statistics(url)`: Get overall statistics of the archive
