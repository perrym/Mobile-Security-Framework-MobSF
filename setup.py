#!/usr/bin/env python3
"""Setup for MobSF."""


from setuptools import (
    find_packages,
    setup,
)

from pathlib import Path


SETTINGS_LOC = 'mobsf/MobSF/settings.py'


def read(rel_path):
    init = Path(__file__).resolve().parent / rel_path
    return init.read_text('utf-8', 'ignore')


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('VERSION'):
            return line.split('\'')[1]
    raise RuntimeError('Unable to find version string.')


def settings_change(path, txt, new_text):
    settings = Path(path)
    old = settings.read_text()
    settings.write_text(old.replace(txt, new_text))


settings_change(SETTINGS_LOC, 'USE_HOME = False', 'USE_HOME = True')
description = (
    'Mobile Security Framework (MobSF) is an automated,'
    ' all-in-one mobile application (Android/iOS/Windows) pen-testing,'
    ' malware analysis and security assessment framework capable of '
    'performing static and dynamic analysis.')
setup(
    name='mobsf',
    version=get_version(SETTINGS_LOC),
    description=description,
    author='Ajin Abraham',
    author_email='ajin25@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
        'Programming Language :: Python :: 3.7',
        'Topic :: Security',
        'Topic :: Software Development :: Quality Assurance',
    ],
    packages=find_packages(include=[
        'mobsf', 'mobsf.*',
    ]),
    include_package_data=True,
    python_requires='>=3.7<3.9',
    entry_points={
        'console_scripts': [
            'mobsf = mobsf.__main__:main',
            'mobsfdb = mobsf.__main__:db',
        ],
    },
    url='https://github.com/MobSF/Mobile-Security-Framework-MobSF',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    install_requires=Path('requirements.txt').read_text().splitlines(),
)
settings_change(SETTINGS_LOC, 'USE_HOME = True', 'USE_HOME = False')
