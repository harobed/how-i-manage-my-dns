# How I maintain my DNS configurations in Git

Based on [LiveDNS Gandi](https://doc.livedns.gandi.net) API, maybe [dnscontrol](https://github.com/StackExchange/dnscontrol) in next iteration.


## Prerequisites

* Python3 (see why below)
* [git-crypt](https://www.agwa.name/projects/git-crypt/)

How to install with brew:

```
$ brew install git-crypt
```

## Usage

Read readme file in:

* [example.io/README.md](cmshub.io/)
* [example.com/README.md](santa-maria.io/)


## How I use it?  What is my workflow?

I want to update `example.io` DNS configuration.

1. I go `santa-maria.io` directory
2. I update `records.txt` file
3. I launch `./diff.py` to see the diff between `records.txt` and current live config
4. if diff is ok, I launch `./push_records.py` to push my config
5. I commit my update to git


## Init git-crypt (First time you create a git repository)

```
$ git-crypt
```

## Add new user to git-crypt

```
$ git-crypt add-gpg-user contact@stephane-klein.info
```

## How to add new domain

Note: this workflow support only LiveDNS Gandi provider.

```
$ mkdir example.com
$ cd example.com
$ ln -s ../scripts/diff.py diff.py
$ ln -s ../scripts/display-live-records.py display-live-records.py
$ ln -s ../scripts/push_records.py push_records.py
$ ln -s ../scripts/README.md README.md
```

Next: follow `example.com/README.md` instructions.


## Why use Python3?

I use python here because this curl command return error: `Error while parsing rdata: Text input is malformed.` but same config work with Python script:

```
$ curl -v -X PUT \
    -H "Content-Type: text/plain" \
    -H "X-Api-Key: $(cat api-key.secret)" \
    --data-binary @records.txt \
    https://dns.api.gandi.net/api/v5/zones/xxxxx/records
```


## Possible progression

I'll maybe use [dnscontroll](https://github.com/StackExchange/dnscontrol) in next iteration when [dnscontrol howe brew will be available](https://github.com/StackExchange/dnscontrol/issues/396).
