#!/bin/bash
set -e

NAME="$1"
URL="$2"
VERSION="$3"

cd vendor
CURR_VERSION=`cat $NAME/vendor-commit 2>/dev/null || true`
if [ "$CURR_VERSION" == "$VERSION" ]; then
    exit 0
fi

rm -rf "$NAME"
git clone -o "$NAME" "$URL"
cd "$NAME"
git reset --hard "$VERSION"
rm -rf `find . -name .git` `find . -name .gitmodules`
echo "$VERSION" > vendor-commit
