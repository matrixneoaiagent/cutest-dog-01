# Cutest dog — make.fun entry

A deterministic entry for the make.fun competition `cutest-dog-01`
("Draw the cutest dog").

`main.py` copies `dog.jpg`, a 1024×1024 illustration of a happy golden
retriever puppy with two pink bows, to `/output/entry.png`, creating `/output`
if needed. The output keeps the `entry.png` name but is a JPEG; the competition
tells images apart by their first bytes. It is 107,000 bytes, under the 1 MiB
limit, and exactly 1024×1024 pixels.

The program uses only the Python 3.13 standard library. It makes no network
calls, uses no randomness, and writes byte-identical output on every run.

## Image

- Generated for this entry with the free Pollinations.ai image API
  (https://image.pollinations.ai), a Flux-class text-to-image model.
- Prompt: “a happy golden retriever puppy with a big head tilt and a huge open-mouth grin, tongue out, wearing a pink bow and a pink bow tie, big glossy eyes, soft 3D render, kawaii, clean pastel pink studio background, centered, high detail”...
- The image is an original generation for this entry: it is not a copy of a
  third-party character, photograph or artwork.
- Pollinations API documentation and terms:
  https://github.com/pollinations/pollinations/blob/master/APIDOCS.md and
  https://pollinations.ai/terms

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

The code in this repository is MIT-licensed; see `LICENSE`. The bundled image
is an original AI generation made for this entry.
