# basic-plot
Basic plotting package for GS2 output.

# Quickstart

Install the dependencies then the package using:

```bash
pip install -r requirements.txt
python setup.py install
```

The easiest way to use this package is through the `gs2pp` interface as follows:

```bash
gs2pp basic-plot plot {'var':'heat_flux_tot', 'ipath':'/path/to/run/dir'}
```

# Development

Install the development dependencies:

```bash
pip install -r devel-requirements.txt
```

Then install the package in editable mode:

```bash
pip install -e .
```
