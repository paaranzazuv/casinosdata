"""Package installer"""

from setuptools import setup, find_packages

setup(
    name="proceso",
    version="0.1",
    package_dir={"": "proceso/src"},
    packages=find_packages(where="proceso/src"),
    install_requires=requirements.txt,
    entry_points={
        "console_scripts": [
            "proceso=__main__:main"
        ]
    },
)
