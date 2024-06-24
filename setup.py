from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pph21_addons_13/__init__.py
from pph21_addons_13 import __version__ as version

setup(
	name="pph21_addons_13",
	version=version,
	description="PPH21 21 TER",
	author="DAS",
	author_email="das@das.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
