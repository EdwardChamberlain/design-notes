# Python Reference Files

This page collects the default Python reference files I reuse across projects. It keeps the style guide and adds starter templates for `flake8`, `.gitignore`, and `pyproject.toml`.

## Python Style Guide

[Download the Python style guide](../assets/documents/python_style_guide.txt){:download="python_style_guide.txt"}

The style guide defines expectations for naming, comments, formatting, imports, type hints, docstrings, and package build structure. It is intended as a consistent baseline rather than a rigid rulebook.

## Default `.flake8`

[Download the default flake8 config](../assets/documents/flake8.txt){: data-dotfile-download=".flake8" }

Use this as the baseline `flake8` configuration for Python projects. It keeps the default checks and sets the maximum line length to 150 characters.

## Standard `.gitignore`

[Download the standard gitignore](../assets/documents/gitignore.txt){: data-dotfile-download=".gitignore" }

This `.gitignore` covers the usual Python-generated files, virtual environments, build outputs, test caches, and common tool-specific local state that should not be committed.

## `pyproject.toml` Template

[Download the `pyproject.toml` template](../assets/documents/pyproject.toml){:download="pyproject.toml"}

This template matches the style guide baseline: PEP 621 metadata, `hatchling` as the build backend, `hatch-vcs` for versioning from Git tags, and a `src/` package layout.
