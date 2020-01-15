import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as readme:
    long_description = readme.read()

setuptools.setup(
    name="musictheorpy",
    version="1.3.0",
    author="Jeffrey Moorhead",
    author_email="jeff.moorhead1@gmail.com",
    description="A music theory library for Python",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/Jeff-Moorhead/musictheorpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
