import setuptools

setuptools.setup(
    extras_require={"fastapi": ["fastapi"], "flask": ["flask"], "minimal": []},
    default_extras_require=["flask"],
)
