# README

This document provides instructions on how to set up your environment and run the `readme-generation.py` script.

## Requirements

You need Python 3.10 or later to run this script. You can check your Python version by running:

```bash
python --version
```

## Setting Up a Python Virtual Environment

It's recommended to use a virtual environment to isolate the dependencies for this project. Here's how you can set it up:

1. Create the virtual environment:

    ```bash
    python -m venv env
    ```

2. Activate the virtual environment:

    - On Windows:

        ```bash
        .\\env\\Scripts\\activate
        ```

    - On Unix or MacOS:

        ```bash
        source env/bin/activate
        ```

## Installing Requirements

Once you've activated the virtual environment, you can install the requirements:

```bash
pip install -r requirements.txt
```

## Running the Script

You can run the `readme-generation.py` script with the path to the YAML file and the output directory as parameters:

```bash
python readme-generation.py ../../model/example-model.yaml ../output/example1
```

This will generate a `readme.md` file in the specified output directory based on the model defined in the YAML file.