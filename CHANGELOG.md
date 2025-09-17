# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial release of RemoteZip MCP Server
- Support for listing files in remote zip archives
- Support for extracting individual files from remote zip archives
- Support for getting file information and zip statistics
- Support for HTTP, HTTPS, and FTP protocols
- Partial reading capability to minimize bandwidth usage
- GitHub Actions workflow for automated releases
- Release script for easy version tagging

### Dependencies
- `mcp>=1.2.0`: Model Context Protocol framework
- `remotezip`: Library for partial reading of remote zip files

### Development
- Python 3.10+ support
- setuptools-based packaging
- Comprehensive README with installation and usage instructions
