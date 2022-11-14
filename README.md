# EPUB of the StarkNet and Cairo Documentation

Unofficial EPUB of the [StarkNet and Cairo documentation](https://www.cairo-lang.org/docs/).

- Download: [starknet-and-cairo-documentation.epub](output/starknet-and-cairo-documentation.epub)
- Last updated: `2022-11-14`.

## Setup

```bash
$ python3 -m venv --copies venv
$ . ./venv/bin/activate
$ python -m pip install -U pip wheel
$ python -m pip install -r requirements.txt
```

Additionally, you want to install `epubcheck`.

## Fetch, and Convert

```bash
$ python -m src
```
## Hack

```bash
$ python -m pip install -r requirements-dev.txt
$ ./checks.sh
```
