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

# 2. Install the PEP 771 Metapackage that will give you the modified libraries:
# - setuptools
# - pip
# - importlib_metadata
# - validate-pyproject
pip install --extra-index-url=https://wheel-next.github.io/static_pipserver/ pep-771

# 3. Let's verify everything is good:
pip --version
>>> pip 25.0.dev0+pep-771 from ...

pip freeze | grep setuptools
>>> setuptools @ git+https://github.com/wheel-next/setuptools.git@...

pip freeze | grep validate-pyproject
>>> validate-pyproject @ git+https://github.com/wheel-next/validate-pyproject.git@...

pip freeze | grep importlib_metadata
>>> importlib_metadata @ git+https://github.com/wheel-next/importlib_metadata.git@...
```

2. Install the demo package:

 ```bash
 # -------------------- Then choose one of the followings -------------------- #

# ~~~~~~~~ demo_pep_771_flavorA ~~~~~~~~ #

# will install demo_pep_771_flavorA AND the default `flask` extra
pip uninstall -y flask fastapi demo_pep_771_flavorA demo_pep_771_flavorB
pip install demo_pep_771_flavorA

# will install demo_pep_771_flavorA AND the explicit `flask` extra
pip uninstall -y flask fastapi demo_pep_771_flavorA demo_pep_771_flavorB
pip install demo_pep_771_flavorA[flask]

# will install demo_pep_771_flavorA AND the explicit `fastapi` extra - no default "flask"
pip uninstall -y flask fastapi demo_pep_771_flavorA demo_pep_771_flavorB
pip install demo_pep_771_flavorA[fastapi]

# will install demo_pep_771_flavorA AND the explicit `minimal` extra - no default "flask"
pip uninstall -y flask fastapi demo_pep_771_flavorA demo_pep_771_flavorB
pip install demo_pep_771_flavorA[minimal]

# ~~~~~~~~ demo_pep_771_flavorB ~~~~~~~~ #

# will install demo_pep_771_flavorB AND the default `flask` extra
pip uninstall -y flask fastapi demo_pep_771_flavorA demo_pep_771_flavorB
pip install demo_pep_771_flavorB

# will install demo_pep_771_flavorB AND the explicit `flask` extra
pip uninstall -y flask fastapi demo_pep_771_flavorA demo_pep_771_flavorB
pip install demo_pep_771_flavorB[flask]

# will install demo_pep_771_flavorB AND the explicit `fastapi` extra - no default "flask"
pip uninstall -y flask fastapi demo_pep_771_flavorA demo_pep_771_flavorB
pip install demo_pep_771_flavorB[fastapi]

# will install demo_pep_771_flavorB AND the explicit `minimal` extra - no default "flask"
pip uninstall -y flask fastapi demo_pep_771_flavorA demo_pep_771_flavorB
pip install demo_pep_771_flavorB[minimal]
```