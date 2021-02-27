# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in repair/__init__.py
from repair import __version__ as version

setup(
	name='repair',
	version=version,
	description='Repair Management',
	author='AgilaSoft Inc.',
	author_email='info@agilasoft.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
