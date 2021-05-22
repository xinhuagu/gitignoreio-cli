from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='gitignoreio-cli',  # Required
    version='0.0.2',  # Required
    description='command line to downlad .gitignore file from gitignore.io', 
    url='https://github.com/xinhuagu/gitignoreio-cli',  # Optional
    author='Xinhua Gu',
    author_email='xinhua.gu@gmail.com',
    keywords='git, gitignore, development', 
    packages=find_packages(),
    python_requires='>=3.6, <4',
    install_requires=['requests','argparse'], 

    entry_points={
        'console_scripts': [
           'gitignoreio-cli=src.bin:main',
        ],
    },

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/xinhuagu/gitignoreio-cli',
    },
)
