# ntt

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/centralelyon/ntt/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/centralelyon/ntt/tree/main)

_A modular video processing pipeline_

## Import using pip (editable mode)

> pip install -e .    

## Import with a clone

Or import the module (assuming you cloned this repository):

```python
import sys

from frames.frame_extraction import extract_first_frame

if __name__ == "__main__":

    extract_first_frame(video_path_in = "samples/", 
                    video_name_in = "C0005.MP4",
                    frame_path_out = "samples/",
                    frame_name_out = "C0005.jpg" 
                    )
```

## Repository structure

```bash
.
├── README.md
├── requirements.txt
├── samples : sample videos, images and data
│   ├── (files)
│   └── ...
├── ntt : the main module
│   ├── README.md
│   ├── __init__.py
│   ├── frames : module for frame extraction
│   │   └── ...
│   ├── ...
│   └── ...
├── .circleci : configuration for CircleCI
│   ├── config.yml
│   └── ...
├── .gitignore
├── Dockerfile
└──
```

## Module structure

Each module structure is as follows:

```bash
.
├── ...
├── ntt/
│   ├── name_of_the_module
│   ├── README.md
│   ├── __init__.py
│   ├── name_of_the_module/
│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── name_of_the_function1.py
│   │   ├── name_of_the_function2.py
│   │   ├── examples
│   │   │   ├── __init__.py
│   │   │   ├── example_name_of_the_function1.py
│   │   │   └── example_name_of_the_function2.py
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   ├── test_name_of_the_function1.py
│   │   │   └── test_name_of_the_function2.py
│   │   └── ...
│   ├── ...
│   └── ...
└── ...
```

## Tests

Run tests with `pytest`:

```bash
$ pytest
```

## CircleCI

The project is configured to run tests on CircleCI. The configuration file is `.circleci/config.yml`.

## Docker

### Steps

- build the image

> docker build -t ntt . 

```bash
$ docker build -t ntt .
```
 
#### Linux/Unix/Mac

- run the image

> docker run --rm -v ${PWD}:/app ntt

(rm is to remove the container after it is stopped)

> docker ps -a

(shows the list of containers)

- run a custom script

> docker run --rm -v ${PWD}:/app ntt python ntt/frames/test/test_frame_extraction.py

#### Windows

- run the image

> docker run -v "$(pwd)":/app ntt python ntt/frames/test/test_frame_extraction.py


## Modules orchestration

_Example of a pipeline_

The general idea is to have a pipeline that looks like this:

1. store videos
2. loaders
3. pre-processors
4. analysis(tracking, detection, segmentation, etc.)
5. post-processors
6. visualizers
7. debug/monitoring

