from setuptools import setup, find_packages

# Leer los requerimientos
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="proceso",  # nombre del paquete
    version="0.1",
    package_dir={"": "proceso/src"},  # define el subdirectorio base
    packages=find_packages(where="proceso/src"),  # busca los paquetes dentro de src
    install_requires=requirements,  # requerimientos desde requirements.txt
    entry_points={
        "console_scripts": [
            "proceso=proceso.__main__:main"  # apunta a la función main en proceso/__main__.py
        ]
    },
)
