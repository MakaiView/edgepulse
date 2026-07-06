#!/usr/bin/env bash
set -euo pipefail

echo "Checking system..."

if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: python3 is required."
  exit 1
fi

if ! command -v systemctl >/dev/null 2>&1; then
  echo "ERROR: systemd/systemctl is required."
  exit 1
fi

python3 - <<'PY'
import sys

if sys.version_info < (3, 13):
    raise SystemExit("ERROR: Python 3.13+ is required.")

print(f"Python OK: {sys.version.split()[0]}")
PY

echo "System check passed."
