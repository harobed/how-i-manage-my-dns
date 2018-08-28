#!/usr/bin/env python3
# I use python here because this curl command return error: "Error while parsing rdata: Text input is malformed." but same config work with current Python script
#
# curl -v -X PUT -H "Content-Type: text/plain" \
#             -H "X-Api-Key: $(cat api-key.secret)" \
#             --data-binary @records.txt \
#              https://dns.api.gandi.net/api/v5/zones/71dd7ba6-8c23-11e7-abec-00163e6dc886/records

import sys
from urllib.request import urlopen, Request
from pathlib import Path
import json

DOMAIN_NAME = Path(".").resolve().name

# read api-key
with open("api-key.secret", "r") as f:
    api_key = f.read().strip()

with urlopen(
    Request(
        url="https://dns.api.gandi.net/api/v5/domains/%s" % DOMAIN_NAME,
        data=None,
        headers={"X-Api-Key": api_key, "Content-Type": "text/json"},
    )
) as response:
    if response.status != 200:
        print(
            "Error [status=%s]: %s" % (response.status, response.read().decode("utf8"))
        )
        sys.exit(2)

    zone_records_href = json.loads(response.read())["zone_records_href"]

with open("records.txt", "r") as f:
    with urlopen(
        Request(
            method="PUT",
            url=zone_records_href,
            headers={"X-Api-Key": api_key, "Content-Type": "text/plain"},
            data=f.read().encode(),
        )
    ) as response:
        if response.status == 201:
            print("Success [status=%s]" % response.status)
        else:
            print("Error [status=%s]" % response.status)
            sys.exit(2)
