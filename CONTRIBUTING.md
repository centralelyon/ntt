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
