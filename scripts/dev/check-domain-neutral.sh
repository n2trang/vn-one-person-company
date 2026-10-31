#!/usr/bin/env bash
# Wrapper kept for compatibility; the real logic lives in the Python version
# so the check works on Windows and Linux without requiring Git Bash.

set -euo pipefail
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/../.." && pwd)"
exec python3 "$REPO_ROOT/scripts/dev/check_domain_neutral.py"
