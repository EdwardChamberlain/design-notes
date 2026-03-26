# Python Reference Files

This page collects the default Python reference files I reuse across projects. It keeps the style guide and adds starter templates for `flake8`, `.gitignore`, and `pyproject.toml`.

## Python Style Guide

[Download the Python style guide](../assets/documents/python_style_guide.txt){:download="python_style_guide.txt"}

The style guide defines expectations for naming, comments, formatting, imports, type hints, docstrings, and package build structure. It is intended as a consistent baseline rather than a rigid rulebook.

## Default `.flake8`

[Download the default flake8 config](../assets/documents/flake8.ini){:download=".flake8"}

Use this as the baseline `flake8` configuration for Python projects. It keeps the default checks and sets the maximum line length to 150 characters.

```ini
[flake8]
max-line-length = 150
```

## Standard `.gitignore`

[Download the standard gitignore](../assets/documents/gitignore.txt){:download=".gitignore"}

This `.gitignore` covers the usual Python-generated files, virtual environments, build outputs, test caches, and common tool-specific local state that should not be committed.

??? note "Show `.gitignore`"
    ```gitignore
    # Byte-compiled / optimized / DLL files
    __pycache__/
    *.py[codz]
    *$py.class

    # C extensions
    *.so

    # Distribution / packaging
    .Python
    build/
    develop-eggs/
    dist/
    downloads/
    eggs/
    .eggs/
    lib/
    lib64/
    parts/
    sdist/
    var/
    wheels/
    share/python-wheels/
    *.egg-info/
    .installed.cfg
    *.egg
    MANIFEST

    # PyInstaller
    #   Usually these files are written by a python script from a template
    #   before PyInstaller builds the exe, so as to inject date/other infos into it.
    *.manifest
    *.spec

    # Installer logs
    pip-log.txt
    pip-delete-this-directory.txt

    # Unit test / coverage reports
    htmlcov/
    .tox/
    .nox/
    .coverage
    .coverage.*
    .cache
    nosetests.xml
    coverage.xml
    *.cover
    *.py.cover
    .hypothesis/
    .pytest_cache/
    cover/

    # Translations
    *.mo
    *.pot

    # Django stuff:
    *.log
    local_settings.py
    db.sqlite3
    db.sqlite3-journal

    # Flask stuff:
    instance/
    .webassets-cache

    # Scrapy stuff:
    .scrapy

    # Sphinx documentation
    docs/_build/

    # PyBuilder
    .pybuilder/
    target/

    # Jupyter Notebook
    .ipynb_checkpoints

    # IPython
    profile_default/
    ipython_config.py

    # pyenv
    #   For a library or package, you might want to ignore these files since the code is
    #   intended to run in multiple environments; otherwise, check them in:
    # .python-version

    # pipenv
    #   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
    #   However, in case of collaboration, if having platform-specific dependencies or dependencies
    #   having no cross-platform support, pipenv may install dependencies that don't work, or not
    #   install all needed dependencies.
    # Pipfile.lock

    # UV
    #   Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
    #   This is especially recommended for binary packages to ensure reproducibility, and is more
    #   commonly ignored for libraries.
    # uv.lock

    # poetry
    #   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
    #   This is especially recommended for binary packages to ensure reproducibility, and is more
    #   commonly ignored for libraries.
    #   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
    # poetry.lock
    # poetry.toml

    # pdm
    #   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
    #   pdm recommends including project-wide configuration in pdm.toml, but excluding .pdm-python.
    #   https://pdm-project.org/en/latest/usage/project/#working-with-version-control
    # pdm.lock
    # pdm.toml
    .pdm-python
    .pdm-build/

    # pixi
    #   Similar to Pipfile.lock, it is generally recommended to include pixi.lock in version control.
    # pixi.lock
    #   Pixi creates a virtual environment in the .pixi directory, just like venv module creates one
    #   in the .venv directory. It is recommended not to include this directory in version control.
    .pixi

    # PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
    __pypackages__/

    # Celery stuff
    celerybeat-schedule
    celerybeat.pid

    # Redis
    *.rdb
    *.aof
    *.pid

    # RabbitMQ
    mnesia/
    rabbitmq/
    rabbitmq-data/

    # ActiveMQ
    activemq-data/

    # SageMath parsed files
    *.sage.py

    # Environments
    .env
    .envrc
    .venv
    env/
    venv/
    ENV/
    env.bak/
    venv.bak/

    # Spyder project settings
    .spyderproject
    .spyproject

    # Rope project settings
    .ropeproject

    # mkdocs documentation
    /site

    # mypy
    .mypy_cache/
    .dmypy.json
    dmypy.json

    # Pyre type checker
    .pyre/

    # pytype static type analyzer
    .pytype/

    # Cython debug symbols
    cython_debug/

    # PyCharm
    #   JetBrains specific template is maintained in a separate JetBrains.gitignore that can
    #   be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
    #   and can be added to the global gitignore or merged into this file.  For a more nuclear
    #   option (not recommended) you can uncomment the following to ignore the entire idea folder.
    # .idea/

    # Abstra
    #   Abstra is an AI-powered process automation framework.
    #   Ignore directories containing user credentials, local state, and settings.
    #   Learn more at https://abstra.io/docs
    .abstra/

    # Visual Studio Code
    #   Visual Studio Code specific template is maintained in a separate VisualStudioCode.gitignore
    #   that can be found at https://github.com/github/gitignore/blob/main/Global/VisualStudioCode.gitignore
    #   and can be added to the global gitignore or merged into this file. However, if you prefer,
    #   you could uncomment the following to ignore the entire vscode folder
    # .vscode/

    # Ruff stuff:
    .ruff_cache/

    # PyPI configuration file
    .pypirc

    # Marimo
    marimo/_static/
    marimo/_lsp/
    __marimo__/

    # Streamlit
    .streamlit/secrets.toml
    ```

## `pyproject.toml` Template

[Download the `pyproject.toml` template](../assets/documents/pyproject.toml){:download="pyproject.toml"}

This template matches the style guide baseline: PEP 621 metadata, `hatchling` as the build backend, `hatch-vcs` for versioning from Git tags, and a `src/` package layout.

```toml
[build-system]
requires = ["hatchling>=1.27.0", "hatch-vcs>=0.4.0"]
build-backend = "hatchling.build"

[project]
name = "example-package"
description = "Short package description"
readme = "README.md"
requires-python = ">=3.11"
authors = [
  { name = "Your Name", email = "you@example.com" },
]
classifiers = [
  "Programming Language :: Python :: 3",
  "Programming Language :: Python :: 3 :: Only",
]
dependencies = []
dynamic = ["version"]

[project.optional-dependencies]
dev = [
  "flake8",
  "pytest",
]

[tool.hatch.version]
source = "vcs"

[tool.hatch.build.targets.wheel]
packages = ["src/example_package"]
```
