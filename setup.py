import setuptools

with open('README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name="musictheorpy",
    version="0.0.1",
    author="Jeff Moorhead",
    author_email="jeff.moorhead1@gmail.com",
    description="a music theory library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jeff-Moorhead/musictheorpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: TBD :: TBD",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pymusic = musictheorpy.console.pymusic:main',
        ],
    }
)
