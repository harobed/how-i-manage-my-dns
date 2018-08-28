#!/usr/bin/env python3

from pathlib import Path
from urllib.request import urlopen, Request
from difflib import unified_diff
import os.path
import re
import sys

DOMAIN_NAME = Path(".").resolve().name


def replace_serial(data):
    return re.sub(
        r"(.*SOA.* )(\d*)( \d* \d* \d* \d*\n.*)",
        r"\1SERIAL\3",
        data,
        flags=re.MULTILINE,
    )


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
    remote_records_txt = response.read().decode("utf8")

if not os.path.exists("records.txt"):
    print("File records.txt not exists\n")
    print(remote_records_txt)
    sys.exit(0)

with open("records.txt", "r") as f:
    local_records_txt = replace_serial(f.read())

diff_result = "".join(
    list(
        unified_diff(
            local_records_txt.strip().splitlines(keepends=True),
            replace_serial(remote_records_txt.strip()).splitlines(keepends=True),
            lineterm="",
            fromfile="records.txt",
            tofile="prod",
        )
    )
).strip()

if diff_result == "":
    print("No difference between online records and records.txt file")
else:
    print(diff_result)
