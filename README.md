# ntt

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/centralelyon/ntt/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/centralelyon/ntt/tree/main)
[![Documentation Status](https://readthedocs.org/projects/ntt/badge/?version=latest)](https://ntt.readthedocs.io/en/latest/?badge=latest)

_Quickly build pipelines to process images and videos._


## Installation

### Using `venv` (recommended)

1. **Create a virtual environment:**

```bash
python -m venv venv
```

2. **Activate the environment:**

* On macOS/Linux:

```bash
source venv/bin/activate
```
* On Windows:

```bash
venv\Scripts\activate
```

3. **Install the module:**

```bash
pip install ntt
```

## Usage

```python
import ntt
 
ntt.__version__  # Example usage
```

## Tests

Assuming you have cloned the repository or installed the source package, you can run tests with `pytest`:

```bash
$ pytest tests
```

## Samples

To download the data samples (videos, images, sounds, etc.) used in tests and examples, clone the repository and update the `.env` file with the path to the cloned folder:

```
git clone https://github.com/centralelyon/ntt-samples.git
```

## Examples

Look at the `examples` folder to see how to use ntt functions.

Assuming you have a `crop.mp4 ` video in a `samples` folder and an `output`
folder, here is how to use `extract_first_frame` function.

```python
import os
from dotenv import load_dotenv
from ntt.frames.frame_extraction import extract_first_frame

if __name__ == "__main__":
    load_dotenv()

    output = extract_first_frame(
        video_path_in=os.environ.get("NTT_SAMPLES_PATH"),
        video_name_in="crop.mp4",
        frame_path_out=os.environ.get("PATH_OUT"),
        frame_name_out="crop-ex.jpg",
    )

    print(f"Frame successfully extracted at {output}") if output is not None else print(
        "Frame extraction failed"
    )
```

## Repository structure

```bash
.
├── .circleci: configuration for CircleCI
│   ├── config.yml
│   └── ...
├── examples: simple examples on how to use ntt functions
│   ├── (files)
│   └── ...
├── samples: sample videos, images and data
│   ├── (files)
│   └── ...
├── src: the package source code
│   └── ntt: the main module
│       ├── README.md
│       ├── __init__.py
│       ├── frames: module for frame extraction
│       │   └── ...
│       ├── ...
│       └── ...
├── tests: pytest files
│   ├── (files)
│   └── ...
├── .gitignore
├── Dockerfile
├── README.md
├── pyproject.toml: ntt Python packaging file, contains ntt dependencies
├── requirements.txt
└──
```

## Module structure

Each module structure is as follows:

```bash
.
├── ...
├── ntt/
│   ├── __init__.py
│   ├── README.md
│   ├── name_of_the_module/
│   │   ├── __init__.py
│   │   ├── README.md
│   │   ├── name_of_the_function1.py
│   │   ├── name_of_the_function2.py
│   │   └── ...
│   ├── ...
│   └── ...
└── ...
```

## CircleCI

The project is configured to run tests on CircleCI. The configuration file is
`.circleci/config.yml`.

## Docker

### Steps

- build the image

> docker build -t ntt . 

```bash
$ docker build -t ntt .
```
 
#### Linux/Unix/Mac

- run the image (rm is to remove the container after it is stopped)

> docker run --rm -v ${PWD}:/app ntt

- show the list of containers

> docker ps -a

- run a custom script

>  docker run --rm -v ${PWD}:/app -e PYTHONPATH=/app/src ntt python tests/test_random_strings.py

- run in interactive mode

> docker run --rm -it -v ${PWD}:/app -e PYTHONPATH=/app/src ntt bash

#### Windows

- run the image

> docker run -v "$(pwd)":/app ntt python ntt/frames/test/test_frame_extraction.py

## Acknowledgments

<img src="https://liris.cnrs.fr/sites/default/files/logo_liris_160_0.png" style="height:50px">&nbsp;&nbsp;&nbsp;<img src="https://www.ec-lyon.fr/sites/default/files/styles/paragraph_image/public/content/paragraphs/images/2024-10/2024_logo-centrale-h_rouge_rvb.jpg.webp" style="height:50px">&nbsp;&nbsp;&nbsp;<img src="https://www.natation-handisport.org/wp-content/uploads/2021/10/logo_NePTUNE_color-768x204.png" style="height:50px">
