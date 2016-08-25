#!/usr/bin/env python

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup

import re
main_py = open('morfessjoint/__init__.py').read()
metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", main_py))

requires = [
    'morfessor',
    #    'progressbar',
]

setup(name='morfessorjoint',
      version=metadata['version'],
      author=metadata['author'],
      author_email='peter.smit@aalto.fi',
      url='http://www.cis.hut.fi/projects/morpho/',
      description='Morfessor Joint Graphemes/Phonemes',
      packages=['morfessjoint', 'morfessjoint.test'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering',
      ],
      license="BSD",
      scripts=['scripts/morfessjoint-train'],
      install_requires=requires,
      extras_require={
          'docs': [l.strip() for l in open('docs/build_requirements.txt')]
      }
      )
