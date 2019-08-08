PE = pipenv
PER = $(PE) run

none:

init:
	$(PE) install --dev

publish:
	$(PER) python setup.py sdist bdist_wheel
	$(PER) twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	rm -fr build dist example2_pkg_blackcat.egg-info
