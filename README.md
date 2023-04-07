# ntt

Modules to create a video processing pipeline

## Module structure

Each module structure is as follows:

```bash
.
├── Dockerfile
├── README.md
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

