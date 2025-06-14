"""Package installer"""

from setuptools import setup, find_packages

setup(
    name="proceso",
    version="0.1",
    package_dir={"": "proceso/src"},
    packages=find_packages(where="proceso/src"),
    install_requires=[
        "pandas",
        "openpyxl",
        # Agrega aquí otras dependencias si quieres (como numpy, etc.)
    ],
    entry_points={
        "console_scripts": [
            "proceso=__main__:main"
        ]
    },
)
