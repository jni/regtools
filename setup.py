#!/usr/bin/env python

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'numpy',
    'scipy',
    'scikit-image'
]

test_requirements = [
    'pytest',
    'pytest-cov',
    'coverage'
]

setup(
    name='regtools',
    version='0.1.0',
    description="Misc tools for image registration in Python",
    long_description=readme + '\n\n' + history,
    author="Juan Nunez-Iglesias",
    author_email='juan.n@unimelb.edu.au',
    url='https://github.com/jni/regtools',
    packages=[
        'regtools',
    ],
    package_dir={'regtools':
                 'regtools'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='regtools',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
