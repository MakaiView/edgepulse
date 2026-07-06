#!/usr/bin/env bash
set -euo pipefail

if [[ "${EUID}" -ne 0 ]]; then
  echo "ERROR: install.sh must be run with sudo."
  echo "Try: sudo ./install.sh"
  exit 1
fi

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Installing EdgePulse..."

bash "${REPO_ROOT}/packaging/scripts/check-system.sh"
bash "${REPO_ROOT}/packaging/scripts/install-files.sh"
bash "${REPO_ROOT}/packaging/scripts/install-service.sh"
bash "${REPO_ROOT}/packaging/scripts/verify.sh"

echo
echo "EdgePulse installed successfully."
echo "Next:"
echo "  sudo systemctl enable edgepulsed"
echo "  sudo systemctl start edgepulsed"

