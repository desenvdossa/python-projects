<h1>Package creator</h1>

<h2>Install package</h2>
python -m pip install --upgrade pip

python -m pip install --user twine

python -m pip install --user setuptools


<h2>Create package</h2>

python setup.py sdist bdist_wheel


<h2>Send to testpypi</h2>

python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/* --verbose

<h2>Install package</h2>

pip install -i https://test.pypi.org/simple/ bank-package-simple
