from setuptools import find_packages, setup
from typing import List

HYPEN = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """Return a list of requirements from requirements.txt"""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]

        if HYPEN in requirements:
            requirements.remove(HYPEN)

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Abhishek Jain",
    author_email="rj773897@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
