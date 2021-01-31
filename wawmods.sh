#!/bin/bash
#
# useful for installing those huge czc map packs on the waw steam community page
# installs all waw mod exes in a given directory
# by default wine will not run this as steam's wine user and the files will end up in a different user's path in the same wine prefix.
# my work-around to this was to symlink the other user's mods folder to mine.
pfx="$HOME/.steam/steam/steamapps/compatdata/10090/pfx/"
if [ "$#" -eq 1 ];
then
    for f in "$1"/*.exe; do
        echo "running: $f"
        WINEPREFIX="$pfx" wine "$f"
    done
else
    echo "provide a directory to install mods from"
    exit 1
fi
echo "complete"
