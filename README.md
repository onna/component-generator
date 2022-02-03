<div align="center">

# Component Generator

[Overview](#overview)
•
[Development](#development)
•
[Website](https://python-component-generator.readthedocs.io)

</div>

## Menu

- [Overview](#overview)
- [Documentation](#documentation)
- [Usage](#usage)
- [Development](#development)
- [Install the dev environment](#install-the-dev-environment)
- [License](#license)

## Overview

Generate backend components quickly.

## Documentation

Please check the [website](https://python-component-generator.readthedocs.io)

## Usage

### PIP

```console
pip install component-generator
```

## Development

### Requirements

- [Python 3.8](https://www.python.org/)
- [Poetry](https://python-poetry.org/)

### Tests

To run all the tests run:

```shell
tox
```

Note, to combine the coverage data from all the tox environments run:

Windows

```console
set PYTEST_ADDOPTS=--cov-append
tox
```

Linux/macOS

```console
PYTEST_ADDOPTS=--cov-append tox
```
