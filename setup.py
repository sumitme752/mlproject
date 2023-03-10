from setuptools import find_packages,setup
from typing import List

HYPN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPN_E_DOT in requirements:
            requirements.remove(HYPN_E_DOT)


    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author = 'sumit',
    author_email = 'sumitme752@gmail.com',
    packages = find_packages(),
    install_requires = get_reuirements('requirements.txt')
)