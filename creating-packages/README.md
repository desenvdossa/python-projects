Package creator

Install package
python -m pip install --upgrade pip

python -m pip install --user twine

python -m pip install --user setuptools


Create package

python setup.py sdist bdist_wheel


Send to testpypi

python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/* --verbose

