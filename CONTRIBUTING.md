# Contributing

## Code Style

The project uses [black](https://pypi.org/project/black/) for code formatting.

Install black as a [Visual Studio Code extension](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter).

## Tests

Run tests with `pytest`:

```bash
$ pytest
```

## CircleCI

The project is configured to run tests on CircleCI. The configuration file is `.circleci/config.yml`.

## Docker

The project is configured to run on Docker. The configuration file is `Dockerfile`.

Build the image with:

```bash
docker build -t ntt .
```

Run the example scripts with:

```bash
docker run --rm -v ${PWD}:/app ntt python /app/scripts/example_generate_random_image.py /app/output/random_image.jpg
docker run --rm -v ${PWD}:/app ntt python /app/scripts/example_generate_annotated_image.py /app/output/annotated_image.jpg
docker run --rm -v ${PWD}:/app ntt python /app/scripts/example_inject_exif_into_image.py /app/output/image_with_exif.jpg
docker run --rm -v ${PWD}:/app ntt python /app/scripts/example_extract_exif_from_image.py /app/output/image_with_exif.jpg
docker run --rm -v ${PWD}:/app ntt python /app/scripts/example_generate_video_and_extract_first_frame.py /app/output
```

These scripts use the project I/O helpers rather than raw OpenCV writes:
`ntt.frames.io.write` for images and `ntt.videos.io.write` for videos.

### VS Code

VS Code tasks are provided in [.vscode/tasks.json](.vscode/tasks.json) for the Docker build and for each example script.

In VS Code:

1. Open `Terminal > Run Task`.
2. Run `docker-build-ntt`.
3. Run one of the `docker-run-example-*` tasks.

The workspace is mounted into the container at `/app`, and generated files are written to the local `output/` folder.


## Pull request (PR)

- Keep the PR small and focus on a issue you are solving
- Use an explicit title and references to the issue you are solving (if any)
- Explain what the PR does and why you make some changes
- Ideally include screenshots when related to UI or graphics when related to speed or errors

## Bug report

You may open an issue:

- Open an [Issue](/issues/new)

## Documentation

- The project uses [Sphinx](https://www.sphinx-doc.org/en/master/) for documentation.

Install the [autodocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) extension for Visual Studio Code.

Use the Google style docstrings.

## Environment variables

We use dotenv to manage environment variables. Use the `.env` file in the root of the project (or create one if it doesn't exist).

## Local development setup

For local development, it is recommended to use the virtual environment listed in the README.md file and run the following commands:

```
python -m pip install --upgrade pip
pip install -e .
pip install pytest
```
