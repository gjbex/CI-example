# CI example

Repository to illustrate

  * Continuous Integration (CI) for software development projects.
  * Using poetry to manage Python software development projects.


## What is it?

  1. `pyproject.toml`: poetry project configuration file.
  1. `poetry.lock`: poetry lock file.
  1. `ci_example`: Python source code directory.
  1. `tests`: pytest unit test for the project.
  1. `CONTRIBUTING.md`: how to contribute to this repository.
  1. `LICENSE`: license for the material in this repository.


## Note

The `main` branch of this repository passes both the `pytest` and the `mypy`
tests, however, the `development` branch of the repository has a test case that
fails intentionally to illustrate that you can prevent a pull request in such a
case.

For that reason, the `main` branch is protected, i.e., only merges through pull
requests are allowed, and the pull request has to pass the build test.
