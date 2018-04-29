""" Packaging settings """

from os.path import abspath, dirname
from setuptools import find_packages, setup

this_dir = abspath(dirname(__file__))

setup(
    name='badgeyay',
    include_package_data=True,
    version='1.0',
    description='A CLI tool for generation of the badges',
    author='yashLadha',
    python_requires='>=3',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # TODO: License to be added
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'click==6.7',
        'pypdf2==1.26.0',
        'defusedxml==0.5.0',
        'cairocffi==0.6.0',
        'cairosvg==2.0.3',
    ],
    keywords='cli badgeyay generator application',
    entry_points={
        'console_scripts': [
            'badgeyay=badgeyay:main',
        ],
    },
)
