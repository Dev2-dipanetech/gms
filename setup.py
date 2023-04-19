from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gms/__init__.py
from gms import __version__ as version

setup(
	name="gms",
	version=version,
	description="An app made for gym",
	author="Souradeep",
	author_email="souradeep.sengupta@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
