from importlib_metadata import entry_points
from setuptools import setup,find_packages


setup(
    name="codeplateau",
    version="1.0.0",
    author="Jonathan Felicity",
    packages=find_packages(exclude=(
        "tests",
    )),
    include_package_data=True,
    entry_points="""
        [console_scripts]
        main=main:cli
    """

)