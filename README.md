# codebase-cleanup-2021

Some starter code to facilitate lessons on code maintenance and quality control, including refactoring and automated testing.

The instructions are here.

## Setup

```sh
conda create -n cleanup-env python=3.8
conda activate cleanup-env
```

## Installation

```sh
pip install -r requirements.txt
```

## Usage

Running the abbreviated game:

```sh
python -m app.game
```

Running the abbreviated shopping cart:

```sh
python -m app.shopping
```

Running the abbreviated robo advisor:

```sh
python -m app.robo
```

## Testing

Running all tests:

```sh
pytest
```
