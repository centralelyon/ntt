# ntt

_A modular video processing pipeline_

To use it in your project, add the following to your `requirements.txt` file:

```bash
ntt @ git+https://github.com/centralelyon/ntt.git@main#egg=ntt
```


Or import the module (assuming you cloned this repository):

```python
import sys

sys.path.append('../ntt')
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
```


## Module structure

Each module structure is as follows:

```bash
.
├── Dockerfile
├── README.md
├── requirements.txt
├── name_of_module
│   ├── README.md
│   ├── __init__.py
│   ├── function1.py
│   ├── function2.py
│   ├── examples
│   │   ├── __init__.py
│   │   ├── example_my_function1.py
│   │   └── example_my_function2.py
│   ├── tests
│   │   ├── __init__.py
│   │   ├── test_my_function1.py
│   │   └── test_my_function2.py
│   └── ...

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

> docker build -t app . 

```bash
$ docker build -t ntt .
```
 
#### Linux/Unix/Mac

- run the image

> docker run --rm -v ${PWD}:/app app

(rm is to remove the container after it is stopped)

> docker ps -a

(shows the list of containers)

- run a custom script

> docker run --rm -v ${PWD}:/app app python frames/test/test_frame_extraction.py

#### Windows

- run the image

> docker run --rm -v ${PWD}:/app app

