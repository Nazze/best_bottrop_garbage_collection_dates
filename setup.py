from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="best_bottrop-NAZZE",
    version="0.0.3",
    author="Nazze",
    description="A small package that returns garbage collection dates in the city of bottrop for a given address",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nazze/best_bottrop_garbage_collection_dates",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)