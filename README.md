# Python Boilerplate

Simple Python boilerplate with Pixi, Ruff, pre-commit hook and Docker

## What you need

- pixi installed
  `brew install pixi`
- git installed
  `brew install git`
- pre-commit installed
  `brew install pre-commit`
- optionally docker and docker-compose installed

## Getting started

1. Clone the repository
2. Navigate to the cloned project directory: `cd python_boilerplate`
3. `pixi install`
4. `pre-commit install`
5. Copy the example env file and set your variables: `cp .env_example .env`
6. `pixi run main`
7. `pixi run lint`
8. `pixi run test`
9. `docker-compose up`

## Project structure

- `src/python_boilerplate`: The main application code
- `tests/python_boilerplate`: The test cases for the project
- `data/`: Contains the data files you don't want to commit to git.
- `.pixi/envs/default/bin/python`: Your local python binary for the project

## Hints

- We have a logger instance you can use `from python_boilerplate.util import logger`
- We have a config files in `./config/` you can use the one accoring to your environment with `from python_boilerplate.util import config`
- You can access the data folder from `./data/` with `from python_boilerplate.data import DATA_DIR`.
- The root of the project can be accessed with `from python_boilerplate.util import ROOT_DIR`.

---

generated with https://github.com/pemukl/python-template
