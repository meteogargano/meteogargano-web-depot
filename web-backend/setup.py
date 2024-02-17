# coding: utf-8

# pylint: disable=missing-docstring
# pylint: disable=invalid-name

import os
import glob

from setuptools import setup, find_packages

import os
import glob

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, '__version__'), encoding='utf-8') as f:
    __version__ = f.read().strip()

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    __readme__ = f.read().strip()

__app_name__ = 'meteogargano-web-backend'


def main():
    setup(
        name=__app_name__,
        version=__version__,
        description='',
        long_description_content_type='text/x-rst',
        long_description=__readme__,
        url='',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python :: 3',
        ],
        packages=find_packages(where='src'),
        package_dir={'': 'src'},
        scripts=[
            'bin/meteogargano_backend',
        ],
        python_requires=">=3.9",
        install_requires=[
            'packaging',
            'fastapi',
            'uvicorn',
            'ninja2',
            'python-multipart',
            'sqlalchemy',
            'FastAPI'
        ],
        
        include_package_data=True, 
    )


if __name__ == '__main__':
    main()
