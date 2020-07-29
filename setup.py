# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in urp_console/__init__.py
from urp_console import __version__ as version

setup(
	name='urp_console',
	version=version,
	description='asdf',
	author='asdf',
	author_email='asdf',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
