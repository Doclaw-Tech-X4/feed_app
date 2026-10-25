# Feed App

Python application for working with feeds. This repository's source files and configuration are the source of truth for supported features and commands; update the project-specific sections below to match the implementation.

## Requirements

- Python 3.10 or later (adjust to the version supported by the project)
- Dependencies listed in the repository's dependency manifest, if present

## Getting started

Clone the repository and enter its directory:

```bash
git clone <repository-url>
cd feed_app
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Install dependencies using the manifest included in the project. For a `requirements.txt` file:

```bash
python -m pip install -r requirements.txt
```

If the project is packaged with `pyproject.toml`, use its documented installation instructions instead.

## Usage

Run the application using its configured entry point or framework command. The exact command depends on the repository's source layout; check the application module and project configuration for the entry point.

Document the available workflows here, including how to add or retrieve feeds, any supported formats, and any required external services, once confirmed from the implementation.

## Configuration

Configuration is defined by the application and its project files. Document required environment variables and their defaults here. Keep credentials and other secrets out of source control; use a local, untracked environment file when supported.

## Tests

Run the test command configured by the project. If the repository uses `pytest`, run:

```bash
python -m pytest
```

## Project layout

The repository's current file tree determines the package and module layout. Add a short description of the key directories and entry-point modules here as they are confirmed.

## Contributing

1. Create a branch for your change.
2. Keep changes focused and add or update tests where appropriate.
3. Run the project's tests and checks before opening a pull request.

## License

See the repository's license file, if provided. No license terms are stated in this README.


## Running the frontend

```bash
uv add streamlit
uv run streamlit run frontend.py
```

## Running the backend check the toml file for dependencies and install using uv

```
uv run python3 main.py
```