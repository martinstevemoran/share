from setuptools import setup, find_packages

setup(
    name='cisco_mce',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
         "requests >= 2.31.0"
    ],
     entry_points={
         'console_scripts': [
             'cisco_mce=ciscomcefiles:main',  # Adjust as needed
        ],
    },
)