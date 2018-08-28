# Usage

## Configure

Add your Gandi `api-key` to `api-key.secret`

## First import

```
$ ./display-live-records.py > records.txt
$ git add records.txt
```

## See diff between live record and records.txt file

```
$ ./diff.py
No difference between online records and records.txt file
```

## Update records

```
$ ./push_records.py
```
