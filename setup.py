from setuptools import setup, find_packages

setup(
    name="pycolortools",
    version="0.1.0",
    description="A Python library for color conversions and colored terminal output",
    author="Quinten Teusink",
    author_email="teusinq879@gmail.com",
    url="https://github.com/jouwgebruikersnaam/pycolortools", 
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
