from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'

#our function get_requirements will return a list
def get_requirements(file_path:str)->List[str]:
    """ this function will return a list of requiremets"""
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements






setup(
name="mlarchitect",
version='0.0.1',
author='Sharafunneesa',
author_email='sharafunneesa111.pp@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)
