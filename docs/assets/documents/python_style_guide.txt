# Python Style Guide

## 1. Self-Documenting Code First
Code should explain itself through clear structure and naming. Readers should understand intent without relying on comments.

### Guidelines
- Use full, descriptive names for variables, functions, classes, and methods.
- Avoid abbreviations and acronyms wherever possible.
- Always prefer clarity over brevity, even if names become longer.

### Naming Rules
- Use full words such as `config` instead of shortened forms like `cfg`.
- Common, unambiguous terms such as `doc` may be acceptable in limited contexts, but default to full words.
- Longer names are encouraged when they improve readability and intent.

### Exceptions
- Short loop variables are acceptable when the context is obvious and local:
```python
for point in points:
    ...
for file in files:
    ...
```
- Single-letter variables may be used sparingly in very small scopes.

---

## 2. Comments Are a Last Resort
Comments should not explain obvious behaviour. Well-written code should be understandable without inline commentary.

### Guidelines
- Do not restate what the code is doing line by line.
- Prefer refactoring over commenting when code is unclear.
- Comments should explain *why*, not *what*, when required.

### Acceptable Uses
- Section headers to improve structure and navigation:
```python
# --- Tag Creation ---
# --- Create Output Directory ---
```
- Explaining non-obvious decisions, constraints, or trade-offs.

---

## 3. Formatting and Linting
Consistency is mandatory and enforced through tooling.

### Guidelines
- Code must conform to PEP 8.
- Code must pass default `flake8` checks.
- Maximum line length is **150 characters**.
- Follow standard Python conventions for whitespace, naming, and layout.

---

## 4. Imports Must Be Explicit
Imports should make the origin of all symbols immediately clear.

### Guidelines
- Use fully qualified imports:
```python
import package
package.module.function()
```
- Avoid `from x import y` as it obscures where symbols originate.
- Renaming imports is acceptable only where it is an established convention:
```python
import numpy as np
import pandas as pd
```

---

## 5. Type Hinting Is Mandatory Where Possible
Type hints improve readability, correctness, and tooling support.

### Guidelines
- All function and method arguments should be type hinted where practical.
- All functions and methods must declare return types.
- Use standard constructs from the `typing` module where required.

---

## 6. Docstrings for Public Interfaces
Docstrings exist for users of the code, not to duplicate implementation details.

### Guidelines
- Use Sphinx-style docstrings for all public functions, methods, and classes.
- Describe behaviour, intent, and usage.
- Do not include `:type:` or `:rtype:` tags.
- Types must be derived from type hints to avoid duplication and drift.
- Keep docstrings concise and accurate.

---

## 7. Package Builds Use pyproject.toml
Python modules should be packaged with a `pyproject.toml` file. Prefer modern PEP 621 metadata and avoid legacy `setup.py` packaging unless forced by external constraints.

### Guidelines
- Define package metadata in `[project]`.
- Use `hatchling` as the build backend and `hatch` to build distributions.
- Define package versions dynamically from Git tags instead of hard-coding them in source files.
- Use a `src/` layout for installable packages.
- Do not define versions in `__init__.py`, `_version.py`, or similar source files unless runtime version introspection explicitly requires it.
- Do not generate or commit a dedicated version file unless runtime version introspection explicitly requires it.

### Minimal Example
```toml
[build-system]
requires = ["hatchling", "hatch-vcs"]
build-backend = "hatchling.build"

[project]
name = "example-package"
description = "Short package description"
readme = "README.md"
requires-python = ">=3.11"
dynamic = ["version"]

[tool.hatch.version]
source = "vcs"

[tool.hatch.build.targets.wheel]
packages = ["src/example_package"]
```
- Create release tags such as `v1.2.3`; `hatch build` will derive the package version from Git without a separate version file.

---

## 8. General Philosophy
- Optimise for readability over cleverness.
- Assume the reader is intelligent but unfamiliar with the code.
- Write code that you would be happy to maintain in six months.
