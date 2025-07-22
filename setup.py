# tells how to install the package and dependencies 
#uses setuptools to create the package

from setuptools import setup, find_packages

#The setup() function is the main entry point for packaging your project.
  #It tells Python how to build, install, and distribute your project.
#find_packages() is a helper function that automatically detects all sub-packages and modules in your code. 

from typing import List

def get_requirements() -> List[str]:
    """
    This function returns a list of requirements for the package.
    It reads from a file named 'requirements.txt' and returns the list of dependencies.
    """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt','r') as f:
            lines = f.readlines()
            for line in lines :
                requirement = line.strip() 
                if requirement and requirement != '-e .': # ignores -e. in requirements.txt
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. No dependencies will be added.")                
    return requirement_lst


setup(
    name= "Network Security",
    version= "0.0.1",
    author= "Ayush",
    author_email= "ay881009@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements()
)