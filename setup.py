from setuptools import find_packages, setup

setup(
    name="vault",
    version="1.0.0",
    description="A tool to edit and preview markdown files in a local web environment.",
    author="Deivid Souza Santana",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "vault = main:main",  # Atrela o comando `vault` à função `main` em `main.py`
        ],
    },
)
