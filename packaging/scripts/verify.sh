#!/usr/bin/env bash
set -euo pipefail

echo "Verifying installation..."

test -d /opt/edgepulse
test -f /etc/edgepulse/config.yaml
test -x /usr/local/bin/edgepulse
test -x /usr/local/bin/edgepulsed
test -f /etc/systemd/system/edgepulsed.service

edgepulse version >/dev/null

echo "Verification passed."
