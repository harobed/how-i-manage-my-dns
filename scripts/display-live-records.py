#!/usr/bin/env python3
from pathlib import Path
from urllib.request import urlopen, Request

DOMAIN_NAME = Path(".").resolve().name

# read api-key
with open("api-key.secret", "r") as f:
    API_KEY = f.read().strip()

# read DOMAIN_NAME records
with urlopen(
    Request(
        url="https://dns.api.gandi.net/api/v5/domains/%s/records" % DOMAIN_NAME,
        data=None,
        headers={"X-Api-Key": API_KEY, "Accept": "text/plain"},
    )
) as response:
    print(response.read().decode("utf8"))
