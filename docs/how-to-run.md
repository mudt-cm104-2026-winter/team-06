# How to run the app

This page shows how to start Movie Ratings on your own laptop.
Running the app is optional. You only need it if you want to try your changes.

## What you need

- Python 3.10 or newer
- This repository on your laptop (`git clone ...`)

Check your Python version:

```bash
python --version
```

On Mac, use `python3` instead of `python`.

## Steps on Mac

Open the terminal in the project folder and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Steps on Windows

Open **Git Bash** in the project folder and run:

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

In PowerShell, the second line is `.venv\Scripts\activate` instead.

## Open the app

Open http://127.0.0.1:8000 in your browser.
Stop the app with `Ctrl+C` in the terminal.

## Good to know

- `.venv` is a small Python just for this project. You create it only once.
  Next time, you only need the `activate` line and the `uvicorn` line.
- The ratings are kept in memory. After a restart, the list is empty again.