#!/bin/bash
# Install script for AIPT
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AIPT_SRC="$SCRIPT_DIR/aipt.py"
AIPT_DST="/usr/local/bin/AIPT"

# Ensure the script has a python3 shebang
if ! head -1 "$AIPT_SRC" | grep -q '^#!'; then
    echo '#!/usr/bin/env python3' | cat - "$AIPT_SRC" > temp && mv temp "$AIPT_SRC"
fi

chmod +x "$AIPT_SRC"
sudo cp "$AIPT_SRC" "$AIPT_DST"
sudo chmod +x "$AIPT_DST"
echo "[AIPT] Installed. You can now run 'sudo AIPT' from anywhere." 