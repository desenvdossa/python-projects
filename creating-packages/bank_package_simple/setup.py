from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="bank_simple",
    version="0.0.1",
    author="Desenvdossa",
    author_email="desenvdossa@gmail.com",
    description="An OOP exercise in package",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/desenvdossa/python-projects/tree/main/creating-packages",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)