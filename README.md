# ntt

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/centralelyon/ntt/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/centralelyon/ntt/tree/main)
[![Documentation Status](https://readthedocs.org/projects/ntt/badge/?version=latest)](https://ntt.readthedocs.io/en/latest/?badge=latest)

`ntt` is a Python module that provides simple and consistent interfaces for common image and video processing tasks. It wraps around popular Python libraries to simplify their usage and make them interchangeable, to build complex pipelines. In particular:

* [**Pillow**](https://python-pillow.org/) – image file handling
* [**OpenCV**](https://opencv.org/) – computer vision, image and video processing
* [**imageio**](https://imageio.github.io/) – read/write images and videos
* [**scikit-image**](https://scikit-image.org/) – scientific image processing
* [**NumPy**](https://numpy.org/) – arrays and calculations

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

The module is available on [Pypi](https://pypi.org/project/ntt/):

```bash
pip install ntt
```

Or install the development version from source:

```bash
git clone
pip install -e .
```

## Tests

```python
import ntt
print(ntt.__version__)  # Check the version
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

An interesting use of `ntt` is to build complex pipelines for video and image processing. For that, we also built a separate tool, the [Pipeoptz](https://github.com/centralelyon/pipeoptz/) library, which provides a simple way to create and manage pipelines of functions.

<p align="center">
<img src="https://private-user-images.githubusercontent.com/586236/535009904-b224b218-e59a-4f8f-bcce-355e5de044ba.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjgyOTY5MDAsIm5iZiI6MTc2ODI5NjYwMCwicGF0aCI6Ii81ODYyMzYvNTM1MDA5OTA0LWIyMjRiMjE4LWU1OWEtNGY4Zi1iY2NlLTM1NWU1ZGUwNDRiYS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMTEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDExM1QwOTMwMDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03OTIxOWVjNTVlNjM1Zjk4YTBmYmUzZDBmNWU3NWNkZmQzNWExYTMyODhmZTRjYzUxN2M3ZDcxMmFjM2U1NTQxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.f6z2CSZyAWEaf1RUk-wh4Ia6yEHNL7aQWqp0FEHTtr0" width="50%">
</p>

The image above is generated using the code below available as a [gist](https://gist.github.com/romsson/5e83ae6dbadf4175e3bbc1454a44a939).

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


## CircleCI

The project is configured to run tests on CircleCI. The configuration file is
`.circleci/config.yml`.

## Docker

A Docker image is available for this project in the root fo the project

### Steps

- build the image:

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