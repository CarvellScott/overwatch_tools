from setuptools import setup, find_packages
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
readme_path = path.join(here, 'README.md')
long_description = ""
if path.exists(readme_path):
    with open(readme_path, encoding='utf-8') as f:
        long_description = f.read()


setup(
    name="overwatch_tools",
    version='0.0.1',
    description='Utilities designed to help players of the game Overwatch.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/CarvellScott/overwatch_tools',
    author='CarvellScott',
    author_email='carvell.scott@gmail.com',
    install_requires=[
        "PyAutoGUI==0.9.47"
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Users',
        'Topic :: Games :: Social Media Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='overwatch',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={
        "console_scripts": [
            "ow-highlight-trimmer=overwatch_tools.highlight_trimmer:main",
            "ow-game-loader=overwatch_tools.game_loader:main",
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/CarvellScott/overwatch_tools/issues',
        'Source': 'https://github.com/CarvellScott/overwatch_tools',
    },
)

