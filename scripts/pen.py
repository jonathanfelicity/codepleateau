import os 
import shutil


language = ['static', 'c', 'c++', 'java', 'python']
def write(name, type):
    """Generating boiler plate files"""
    if(type in language):
        repo = f'{os.path.dirname(__file__)}/repo/{type}'
        shutil.copytree(repo, name)
    else:
        print("False")
    