from setuptools import find_packages, setup
from typing import List

def get_requirements(filepath: str)->List[str]:
    """
    This function will return list of requirements
    """

    requirements = []

    with open(filepath) as f:
        requirements = f.readlines()
        [req.replace("\n", "") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements

setup(
    name="GenBrains",
    version="0.0.1",
    author="Satyam Mishra",
    author_email="apibrains@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)