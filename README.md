# Cutest dog — make.fun entry

A deterministic entry for the make.fun competition `cutest-dog-01`
("Draw the cutest dog").

`main.py` copies `dog.jpg`, a 1024×1024 photo of a white puppy, to
`/output/entry.png`, creating `/output` if needed. The output keeps the
`entry.png` name but is a JPEG; the competition tells images apart by their
first bytes. It is 171,715 bytes, under the 1 MiB limit, and exactly
1024×1024 pixels.

The program uses only the Python 3.13 standard library. It makes no network
calls, uses no randomness, and writes byte-identical output on every run.

## Image source

- Source page: https://commons.wikimedia.org/wiki/File:Puppy_filtered.jpg
- License: CC0 1.0 Universal (public domain dedication),
  https://creativecommons.org/publicdomain/zero/1.0/
- Bundled unmodified as `dog.jpg`.

## Run

Inside the competition sandbox (Python 3.13):

```sh
python3 main.py
```

This writes `/output/entry.png`.

For a local run, `MAKEFUN_OUTPUT_DIR` can replace `/output`:

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.png`.

## License

The code in this repository is MIT-licensed; see `LICENSE`. The bundled photo
is CC0.
