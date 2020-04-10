# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
import os, sys, ast

here = os.path.abspath(os.path.dirname(__file__))
long_description = "See website for more info."

# Importing during setup causes dependency issues
with open('ohcrap/version.py') as f:
    exec(f.read())

setup(
    name='ohcrap',
    version=version,
    description='OhCrap(s) Simulator',
    long_description=long_description,
    url='https://github.com/bannsec/ohcrap',
    author='Michael Bann',
    author_email='self@bannsecurity.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Environment :: Console'
    ],
    keywords='Craps Simulation Strategy',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'dist']),
    install_requires=['prettytable'],
    entry_points={
        'console_scripts': [
            'ohcrap = ohcrap.ohcrap:run',
        ],
    },
)

