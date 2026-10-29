check_dir=$(mktemp -d)
git clone ~/h-drive/calculator "$check_dir/calculator"
cd "$check_dir/calculator"
#!/bin/bash
set -e
cd -- "$(dirname -- "$0")"
python3 calculator.py
