# RemoteZip MCP Server

An MCP server that provides tools for accessing remote zip files over HTTP, HTTPS, and FTP protocols without downloading the entire archive.

## Features

- List files in remote zip archives
- Extract individual files from remote zip archives
- Get file information and statistics
- Support for HTTP, HTTPS, and FTP protocols
- Partial reading - only downloads necessary parts of the zip file

## Installation

### From Source

1. Install Python 3.10 or higher
2. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/remotezip-mcp.git
   cd remotezip-mcp
   ```
3. Install dependencies:
   ```bash
   pip install -e .
   ```

### From GitHub Releases

Download the latest release from the [Releases](https://github.com/yourusername/remotezip-mcp/releases) page and install:

```bash
pip install remotezip_mcp-1.0.0-py3-none-any.whl
```

## MCP Server Configuration

### For VSCode

1. **Install the MCP extension**:
   - Search for "MCP (Model Context Protocol)" in VSCode extensions
   - Install the extension by Anthropic

2. **Create MCP configuration file**:
   - Create the file `~/.vscode/mcp.json` (on macOS/Linux) or `%APPDATA%\Code\User\mcp.json` (on Windows)
   - Or use the global config: `~/.config/mcp/mcp.json`

3. **Add the following configuration to your mcp.json**:

```json
{
  "mcpServers": {
    "remotezip": {
      "command": "remotezip-mcp",
      "args": [],
      "env": {
        "PATH": "$PATH"
      }
    }
  }
}
```

4. **Restart VSCode** to load the MCP server

### For Cursor

1. **Open Cursor settings**:
   - Press `Cmd/Ctrl + ,` to open settings
   - Or go to File → Preferences → Settings

2. **Navigate to MCP settings**:
   - Search for "mcp" in the settings search bar
   - Look for "MCP: Servers" or "Model Context Protocol" section

3. **Add a new MCP server** with these exact settings:

- **Name**: `RemoteZip MCP Server`
- **Command**: `remotezip-mcp`
- **Arguments**: Leave this field empty
- **Environment Variables**: (optional)

4. **Save and restart Cursor** to activate the MCP server

### Alternative: Manual MCP Configuration

If your editor doesn't have built-in MCP support, you can also run the server manually:

```bash
# Start the MCP server
remotezip-mcp
```

Then connect to it using your MCP client with the server running on the default port.

### Troubleshooting

- **Command not found**: Make sure `remotezip-mcp` is in your PATH after installation
- **Permission denied**: Try running with `sudo` or check file permissions
- **Server won't start**: Verify the installation with `remotezip-mcp --help`
- **Configuration not loading**: Check the JSON syntax in your mcp.json file

## Usage

Run the server:
```bash
python remotezip_server.py
```

Or use the installed command:
```bash
remotezip-mcp
```

## Tools

- `list_files(url)`: Get list of files in the archive
- `extract_file(url, filename, local_path)`: Extract a file to local storage
- `get_file_info(url, filename)`: Get details about a specific file
- `get_zip_statistics(url)`: Get overall statistics of the archive

## Development

### Setup Development Environment

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode
pip install -e .
```

### Running Tests

```bash
# Run the MCP server
python remotezip_server.py
```

### Creating Releases

Use the provided release script:

```bash
./release.sh 1.0.0
```

This will:
1. Create a git tag `r1.0.0`
2. Push the tag to GitHub
3. Trigger GitHub Actions to build and release

## GitHub Actions

The repository includes automated release workflows:

- **Release Workflow** (`.github/workflows/release.yml`): Automatically builds and releases when version tags are pushed
- Triggers on tags matching pattern `r*`
- Builds Python wheel and source distribution
- Creates GitHub release with generated release notes

## Dependencies

- `remotezip`: For partial reading of remote zip files
- `mcp`: Model Context Protocol framework
- `fastmcp`: FastMCP server implementation

## License

MIT License - see LICENSE file for details
