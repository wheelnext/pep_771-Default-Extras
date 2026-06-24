import setuptools

setuptools.setup(
    extras_require={"fastapi": ["fastapi"], "flask": ["flask"]},
    default_extras_require=["flask"],
)
