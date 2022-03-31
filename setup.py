from setuptools import setup,find_packages



with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="codeplateau",
    version="1.0.6",
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
        'click==8.0.4',
        'colorama==0.4.4',
        'requests==2.11.1',
        'requests-toolbelt==0.9.1',
        'six==1.16.0',
        'tqdm==4.63.0',
    ],
    include_package_data=True,
    python_requires='>=3.7',
    py_modules=['main'],
    
    entry_points= """
        [console_scripts]
        codeplateau=main:cli
    """

)