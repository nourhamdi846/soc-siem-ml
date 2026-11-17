#!/usr/bin/env python3
import sys, json, requests
alert_file = sys.argv[1]
hook_url = sys.argv[3]
with open(alert_file) as f:
    alert = json.load(f)
requests.post(hook_url, json=alert, timeout=10)
