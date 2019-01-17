
# =========================================
#       IMPORTS
# --------------------------------------

import os
import setuptools

# DISABLED/BUG: this line fails when `pip install attributedict` but works `pip install .`
# from attributedict import __version__

# =========================================
#       FUNCTIONS
# --------------------------------------

def get_readme():
    root_path = os.path.abspath(os.path.dirname(__file__))
    readme_file_path = os.path.join(root_path, 'README.md')

    with open(readme_file_path) as file:
        readme = file.read()

    return readme

def get_requirements():
    root_path = os.path.abspath(os.path.dirname(__file__))
    requirements_file_path = os.path.join(root_path, 'requirements.txt')

    with open(requirements_file_path) as file:
        requirements = [requirement.strip() for requirement in file.readlines()]
        requirements = filter(lambda requirement: len(requirement), requirements)
        requirements = list(requirements)

    return requirements


# =========================================
#       MAIN
# --------------------------------------

readme = get_readme()
requirements = get_requirements()
packages = setuptools.find_packages()

config = {
    'name': 'attributedict',
    'version': '0.2.0',
    'description': (
        'A dictionary object with attributes support.'
    ),
    'keywords': [
        'object',
        'dict',
        'dictionary',
        'collection',
        'attributes',
        'attribute',
        'attr',
        'properties',
        'property',
        'props',
        'openstruct',
        'struct',
        'hashmap',
    ],
    'author': 'Jonas Grimfelt',
    'author_email': 'grimen@gmail.com',
    'url': 'https://github.com/grimen/python-attributedict',
    'download_url': 'https://github.com/grimen/python-attributedict',
    'project_urls': {
        'repository': 'https://github.com/grimen/python-attributedict',
        'bugs': 'https://github.com/grimen/python-attributedict/issues',
    },
    'license': 'MIT',

    'long_description': readme,
    'long_description_content_type': 'text/markdown',

    'classifiers': [
        'Topic :: Software Development :: Libraries',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    'packages': packages,
    'package_dir': {
        'attributedict': 'attributedict'
    },
    'package_data': {
        '': [
            'MIT-LICENSE',
            'README.md',
        ],
        'attributedict': [
            '*.*',
        ]
    },
    'include_package_data': True,
    'zip_safe': True,

    'install_requires': requirements,
    'setup_requires': ['setuptools_git >= 1.2'],
}

setuptools.setup(**config)
