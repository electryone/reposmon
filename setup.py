# coding=utf-8
"""
appinstance
-
Active8 (04-03-15)
author: erik@a8.nl
license: GNU-GPL2
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from setuptools import setup
setup(name='reposmon',
      version='13',
      description='Monitor a git repository, execute a command when it changes. Basically a polling git-hook for pull.',
      url='https://github.com/erikdejonge/reposmon',
      author='Erik de Jonge',
      author_email='erik@a8.nl',
      license='GPL',
      scripts=['reposmon/reposmon'],
      packages=['reposmon'],
      zip_safe=True,
      install_requires=['consoleprinter', 'arguments', 'appinstance', 'schema', 'GitPython', 'pyyaml', 'docopt', 'psutil'],
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Development Status :: Beta",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
          "Operating System :: POSIX",
          "Topic :: Software Development :: Quality Assurance",
          "Topic :: System",
      ])
