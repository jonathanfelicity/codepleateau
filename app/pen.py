import os 
import shutil


def write(name, type):
    """Generating boiler plate files"""
    if(type):
        repo = f'{os.path.dirname(__file__)}/repo/{type}'
        shutil.copytree(repo, name)
    else:
        print("False")
    