from setuptools import setup,find_packages

setup(
    name="codeplateau",
    version="1.0.0",
    author="Jonathan Felicity",
    packages=find_packages(exclude=(
        "tests",
    )),
    install_requires=[
        'click',
    ],
    include_package_data=True,
    python_requires='>=3.7',
    py_modules=['main'],
    entry_points= """
        [console_scripts]
        codeplateau=main:start
    """

)