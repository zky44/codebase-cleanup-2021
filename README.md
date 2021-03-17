# codebase-cleanup-2021

Some starter code to facilitate lessons on code maintenance and quality control, including refactoring and automated testing.

The instructions are here.

## Setup

Create and activate a new virtual environment:

```sh
conda create -n cleanup-env python=3.8
conda activate cleanup-env
```

Copy the default products inventory (then optionally customize the resulting "products.csv" file with your own products as desired):

```sh
cp data/default_products.csv data/products.csv
```

## Installation

```sh
pip install -r requirements.txt
```

## Usage

Running the abbreviated shopping cart:

```sh
python -m app.shopping
```

Running the abbreviated game:

```sh
python -m app.game
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
