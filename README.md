# Applied Machine Learning — Basic | Hands-on material

Companion material for the University of Bologna's [Applied Machine Learning — Basic course](https://www.unibo.it/it/studiare/insegnamenti-competenze-trasversali-moocs/insegnamenti/insegnamento/2026/558922). It provides short, practical introductions to the Python tools used during the course. Work through the material in numerical order; it is intended for experimentation, so change and re-run the examples.

## Repository at a glance

- `handson-0/` — Python foundations: syntax, operators, functions, packages, and data handling.
- `handson-1/` — data manipulation with pandas.
- `handson-2/` — data visualisation with Matplotlib.
- `notebooks/` — self-contained Jupyter/Colab versions: `Python101.ipynb`, `Pandas101.ipynb`, and `Matplotlib101.ipynb`.
- `example_scripts/` — supplementary examples.
- `requirements.txt` — Python packages needed for the hands-ons.

Each `handson-*` folder corresponds to one hands-on session and contains runnable Python scripts. The notebooks cover the same introductory topics in an interactive format; use whichever format is requested in class or suits your workflow.

## Run locally

Use Python 3. Create an isolated environment, install the dependencies, then open a notebook or run a script from the repository root:

```bash
git clone https://github.com/clissa/aml-basic-handson.git
cd aml-basic-handson
python -m venv .venv
```

Activate the environment (`.venv\\Scripts\\Activate.ps1` on Windows PowerShell, or `source .venv/bin/activate` on macOS/Linux), then:

```bash
python -m pip install -r requirements.txt
jupyter notebook
# or, for example:
python handson-0/001_basics.py
```

If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` for the current terminal, then activate the environment again.

## Use Google Colab

Open one of the files in `notebooks/` in [Google Colab](https://colab.research.google.com/) (File → Open notebook → GitHub, then search for `clissa/aml-basic-handson`), or use the direct notebook links below. Run cells from top to bottom and save a copy to your Google Drive before editing.

- [Python 101](https://colab.research.google.com/github/clissa/aml-basic-handson/blob/main/notebooks/Python101.ipynb)
- [Pandas 101](https://colab.research.google.com/github/clissa/aml-basic-handson/blob/main/notebooks/Pandas101.ipynb)
- [Matplotlib 101](https://colab.research.google.com/github/clissa/aml-basic-handson/blob/main/notebooks/Matplotlib101.ipynb)

The notebooks' main libraries are already available in Colab. For any missing package, run `!pip install -r https://raw.githubusercontent.com/clissa/aml-basic-handson/main/requirements.txt` in a notebook cell.
