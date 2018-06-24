
import setuptools

from attributedict import __version__

setuptools.setup(
    name = 'attributedict',
    version = __version__,
    description = (
        'A dictionary object with attributes support.'
    ),
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    keywords = [
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
    author = 'Jonas Grimfelt',
    author_email = 'grimen@gmail.com',
    url = 'https://github.com/grimen/python-attributedict',
    project_urls = {
        'repository': 'https://github.com/grimen/python-attributedict',
        'bugs': 'https://github.com/grimen/python-attributedict/issues',
    },
    package_data = {
        '': [
            'MIT-LICENSE',
            'README.md',
        ],
    },
    py_modules = ['attributedict'],
    license = 'MIT',
    classifiers = [
        'Topic :: Software Development :: Libraries',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    zip_safe = True,
)
