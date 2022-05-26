# EPUB of the StarkNet and Cairo Documentation

Unofficial EPUB of the [EPUB of the StarkNet and Cairo documentation](https://www.cairo-lang.org/docs/).

Last updated: `2022-05-26`.

## Setup

```bash
$ python3 -m venv --copies venv
$ . ./venv/bin/activate
$ python -m pip install -U pip wheel
$ python -m pip install -r requirements.txt
```

Additionally, you want to install `epubcheck`.

## Fetch, and Convert

```bash
$ python -m src
```

## Hack

```bash
$ python -m pip install -r requirements-dev.txt
$ ./checks.sh
```