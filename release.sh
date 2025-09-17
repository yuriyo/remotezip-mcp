#!/bin/bash

# Release script for remotezip-mcp
# Usage: ./release.sh <version>
# Example: ./release.sh 1.0.0

set -e

if [ $# -ne 1 ]; then
    echo "Usage: $0 <version>"
    echo "Example: $0 1.0.0"
    exit 1
fi

VERSION=$1
TAG="r$VERSION"

echo "Creating release $VERSION with tag $TAG"

# Check if tag already exists
if git tag -l | grep -q "^$TAG$"; then
    echo "Error: Tag $TAG already exists"
    exit 1
fi

# Create annotated tag
git tag -a "$TAG" -m "Release $VERSION"

# Push tag to trigger GitHub Actions
git push origin "$TAG"

echo "Tag $TAG created and pushed!"
echo "GitHub Actions will automatically:"
echo "  - Build the Python package"
echo "  - Create a GitHub release"
echo "  - Upload distribution files"
echo "  - Generate release notes from commits"
