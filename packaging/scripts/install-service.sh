#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

echo "Installing systemd service..."

install -m 0644 \
  "${REPO_ROOT}/packaging/systemd/edgepulsed.service" \
  /etc/systemd/system/edgepulsed.service

systemctl daemon-reload

echo "Systemd service installed."
