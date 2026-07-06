#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

echo "Installing application files..."

mkdir -p /opt/edgepulse
mkdir -p /etc/edgepulse
mkdir -p /var/log/edgepulse

rsync -a --delete \
  --exclude ".git" \
  --exclude ".venv" \
  --exclude "__pycache__" \
  --exclude ".pytest_cache" \
  --exclude ".ruff_cache" \
  "${REPO_ROOT}/src/edgepulse" \
  /opt/edgepulse/

cp "${REPO_ROOT}/pyproject.toml" /opt/edgepulse/

if [[ ! -f /etc/edgepulse/config.yaml ]]; then
  cp "${REPO_ROOT}/config/config.yaml" /etc/edgepulse/config.yaml
fi

install -m 0755 "${REPO_ROOT}/packaging/scripts/edgepulse" /usr/local/bin/edgepulse
install -m 0755 "${REPO_ROOT}/packaging/scripts/edgepulsed" /usr/local/bin/edgepulsed

echo "Application files installed."
