from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="demo_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
    ],
    author="Your Name",
    description="A package for one-hot encoding columns in CSV dataframes",
    long_description=long_description, 
    long_description_content_type="text/markdown",

    
)    