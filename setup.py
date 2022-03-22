from setuptools import setup,find_packages



with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()



setup(
    name="codeplateau",
    version="1.0.2",
    author="Jonathan Felicity",
    author_email="jonathanfelicity@mail.com",
    description="CLI tool that makes coding easy and fun.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/jonathan-felicity/codepleateau.git",
    packages=find_packages(exclude=(
        "tests",
    )),
    install_requires=[
        requirements,
    ],
    include_package_data=True,
    python_requires='>=3.7',
    py_modules=['main'],
    
    entry_points= """
        [console_scripts]
        codeplateau=main:start
    """

)