This repository contains a simple demo package that makes use of a default extras to install recommended dependencies by default.

It is an example usage of the specification described in the PEP
draft at https://github.com/python/peps/pull/4198/.


The demo package comes in two flavors:
- Flavor A: Built exclusively with `pyproject.toml`
- Flavor B: Built mixing `pyproject.toml` and `setup.py`

Aside of that, both have the exact same logic, exact same behavior:

1. Install the PEP 771 Package:

```bash
# 1. Create a virtualenv 
# WARNING: Installing PEP 771 overwrites a bunch of standard python library.
# Do not install this in your main python environment.
virtualenv .venv
source .venv/bin/activate

# 2. Set the extra index to the Wheel-Next Static Wheel Server: MockHouse
pip config set --site global.extra-index-url https://wheel-next.github.io/mockhouse/pep-771/
>>> Writing to /path/to/venv/pip.conf

# 2. Install the PEP 771 Metapackage that will give you the modified libraries:
# - setuptools
# - pip
# - importlib_metadata
# - validate-pyproject
pip install pep-771

# 3. Let's verify everything is good:
pip --version
>>> pip 25.0.dev0+pep-771 from ...  # <=============== Check you can see `+pep-771`

pip freeze | grep setuptools
>>> setuptools @ git+https://github.com/wheel-next/setuptools.git@...
```

2. Install the demo package:

 ```bash
 # -------------------- Then choose one of the followings -------------------- #

# ~~~~~~~~ pep-771-demo-a ~~~~~~~~ #

# will install pep-771-demo-a AND the default `flask` extra
pip uninstall -y flask fastapi pep-771-demo-a pep-771-demo-b
pip install pep-771-demo-a

# will install pep-771-demo-a AND the explicit `flask` extra
pip uninstall -y flask fastapi pep-771-demo-a pep-771-demo-b
pip install pep-771-demo-a[flask]

# will install pep-771-demo-a AND the explicit `fastapi` extra - no default "flask"
pip uninstall -y flask fastapi pep-771-demo-a pep-771-demo-b
pip install pep-771-demo-a[fastapi]

# will install pep-771-demo-a AND the explicit `minimal` extra - no default "flask"
pip uninstall -y flask fastapi pep-771-demo-a pep-771-demo-b
pip install pep-771-demo-a[minimal]

# ~~~~~~~~ pep-771-demo-b ~~~~~~~~ #

# will install pep-771-demo-b AND the default `flask` extra
pip uninstall -y flask fastapi pep-771-demo-a pep-771-demo-b
pip install pep-771-demo-b

# will install pep-771-demo-b AND the explicit `flask` extra
pip uninstall -y flask fastapi pep-771-demo-a pep-771-demo-b
pip install pep-771-demo-b[flask]

# will install pep-771-demo-b AND the explicit `fastapi` extra - no default "flask"
pip uninstall -y flask fastapi pep-771-demo-a pep-771-demo-b
pip install pep-771-demo-b[fastapi]

# will install pep-771-demo-b AND the explicit `minimal` extra - no default "flask"
pip uninstall -y flask fastapi pep-771-demo-a pep-771-demo-b
pip install pep-771-demo-b[minimal]
```