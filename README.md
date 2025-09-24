# ntt

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/centralelyon/ntt/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/centralelyon/ntt/tree/main)
[![Documentation Status](https://readthedocs.org/projects/ntt/badge/?version=latest)](https://ntt.readthedocs.io/en/latest/?badge=latest)

`ntt` is a Python module that provides simple and consistent interfaces for common image and video processing tasks. It wraps around popular libraries such as Pillow, OpenCV, imageio, and scikit-image to simplify their usage and make them interchangeable, to build complex pipelines.

* [**Pillow**](https://python-pillow.org/) – image file handling
* [**OpenCV**](https://opencv.org/) – computer vision, image and video processing
* [**imageio**](https://imageio.github.io/) – read/write images and videos
* [**scikit-image**](https://scikit-image.org/) – scientific image processing


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


## Tests

```python
import ntt
 
ntt.__version__  # Check the version
```

Assuming you have cloned the repository or installed the source package, you can run tests with `pytest`:

```bash
$ pytest tests
```

## Samples

To download the data samples (videos, images, sounds, etc.) used in tests and examples, clone the repository and update the `.env` file with the path to the cloned folder:

```
git clone https://github.com/centralelyon/ntt-samples.git
```

Alternatively, you can generate fake videos samples by running the following script:

```python
from ntt.videos.video_generation import random_video

video = random_video(320, 240, 10, 2)
```

## Building pipelines

The ultimate goal of `ntt` is to build complex pipelines for video and image processing. For that, we also built a separate tool, the [`pipeoptz`](https://github.com/centralelyon/pipeoptz/) library, which provides a simple way to create and manage pipelines of functions.

<p align="center">
<img src="https://private-user-images.githubusercontent.com/586236/493305988-6fe114c4-b1fe-46a7-a9da-2540661ad3ce.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTg3MTMzNDMsIm5iZiI6MTc1ODcxMzA0MywicGF0aCI6Ii81ODYyMzYvNDkzMzA1OTg4LTZmZTExNGM0LWIxZmUtNDZhNy1hOWRhLTI1NDA2NjFhZDNjZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwOTI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDkyNFQxMTI0MDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lMGE2ZmMyNzRkM2JiY2NjOWFlNzUwZjA1NmFlMTgzZGViYTViOGM5ZWM2N2U3OTM5N2Y2N2Q1MmIzNGYwMGMwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.4ATz2sWYMydw0eI0NDlWkCZZWzarukmWlozPc6mQoUk" width="50%">
</p>

```python
import random

from ntt.frames.frame_generation import random_frame
from ntt.frames.display import display_frame
from pipeoptz import Pipeline, Node

def random_number():
    num = random.randint(100, 600)
    return num

pipeline = Pipeline("Simple Pipeline", "Generate a random image.")

node_gen_width = Node("GenWidth", random_number) 
node_gen_height = Node("GenHeight", random_number)
node_random_frame = Node(
    "random_frame", random_frame, fixed_params={"width": 10, "height": 3}
)

pipeline.add_node(node_gen_width)
pipeline.add_node(node_gen_height)
pipeline.add_node(
    node_random_frame, predecessors={"width": "GenWidth", "height": "GenHeight"}
)

outputs = pipeline.run()
display_frame(outputs[1][pipeline.static_order()[-1]])

```

## Examples

You may look at the `examples` folder to see how to use `ntt` functions. Also a look a the `tests` folder to see how functions are tested. And of course, the documentation at [https://ntt.readthedocs.io](https://ntt.readthedocs.io).

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

<p align="center">
<img src="https://liris.cnrs.fr/sites/default/files/logo_liris_160_0.png" style="height:50px">&nbsp;&nbsp;&nbsp;<img src="https://www.ec-lyon.fr/sites/default/files/styles/paragraph_image/public/content/paragraphs/images/2024-10/2024_logo-centrale-h_rouge_rvb.jpg.webp" style="height:50px">&nbsp;&nbsp;&nbsp;<img src="https://www.natation-handisport.org/wp-content/uploads/2021/10/logo_NePTUNE_color-768x204.png" style="height:50px"></p>