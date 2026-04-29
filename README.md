# design-notes
Personal notes for engineering design.

## Local Build

Create a virtual environment and install the MkDocs dependencies:

```bash
python3 -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
```

Run a local preview server:

```bash
mkdocs serve
```

Then open <http://127.0.0.1:8000/> in a browser.

Build the static site into the `site/` directory:

```bash
mkdocs build --strict
```
