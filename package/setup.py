import setuptools
from setuptools import find_packages

setuptools.setup(
    name="package",
    version="0.0.1",
    author="Thomas Lips",
    author_email="thomas.lips@ugent.be",
    description="",
    install_requires=[
        "numpy",
    ],
    packages=find_packages(),
)
