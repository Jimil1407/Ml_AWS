from setuptools import find_packages, setup
from typing import List

ignr = '-e .'
def get_requirements(path:str)->List[str]:
    ''' this functions will return a list of requirements from the file'''
    requirements = []
    with open(path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n"," ")for req in requirements]

        if ignr in requirements:
            requirements.remove(ignr)

    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Jimil',
    author_email='jimil.devs@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)