from asyncore import read
from gettext import install
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example of python packages',
    long_description=open('readme.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<OdukoyaD>/<package-name>',
    author='<Odukoya Adewale Daniel>',
    author_email='<danielOdukoyawale@gmail.com>'
    
)