from typing import Any
from remotezip import RemoteZip
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("remotezip")

@mcp.tool()
async def list_files(url: str) -> str:
    """Get list of files in a remote zip archive.

    Args:
        url: URL of the remote zip file (http, https, ftp supported)
    """
    try:
        with RemoteZip(url) as zip_file:
            files = zip_file.namelist()
            return "\n".join(files)
    except Exception as e:
        return f"Error listing files: {str(e)}"

@mcp.tool()
async def extract_file(url: str, filename: str, local_path: str = ".") -> str:
    """Extract a specific file from a remote zip archive to local storage.

    Args:
        url: URL of the remote zip file
        filename: Name of the file to extract
        local_path: Local directory to extract to (default: current directory)
    """
    try:
        with RemoteZip(url) as zip_file:
            zip_file.extract(filename, local_path)
            return f"Extracted {filename} to {local_path}"
    except Exception as e:
        return f"Error extracting file: {str(e)}"

@mcp.tool()
async def get_file_info(url: str, filename: str) -> str:
    """Get information about a specific file in the remote zip archive.

    Args:
        url: URL of the remote zip file
        filename: Name of the file
    """
    try:
        with RemoteZip(url) as zip_file:
            info = zip_file.getinfo(filename)
            return f"Filename: {info.filename}\nSize: {info.file_size} bytes\nCompressed size: {info.compress_size} bytes"
    except Exception as e:
        return f"Error getting file info: {str(e)}"

@mcp.tool()
async def get_zip_statistics(url: str) -> str:
    """Get statistics about the remote zip archive.

    Args:
        url: URL of the remote zip file
    """
    try:
        with RemoteZip(url) as zip_file:
            files = zip_file.infolist()
            total_files = len(files)
            total_size = sum(info.file_size for info in files)
            total_compressed = sum(info.compress_size for info in files)
            return f"Total files: {total_files}\nTotal uncompressed size: {total_size} bytes\nTotal compressed size: {total_compressed} bytes"
    except Exception as e:
        return f"Error getting statistics: {str(e)}"

def main():
    """Entry point for the MCP server."""
    # Initialize and run the server
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
