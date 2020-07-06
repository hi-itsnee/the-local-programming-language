#!/usr/bin/env python3

from distutils.core import setup

setup(name='local',
      version='2.0',
      description='The local programming language',
      packages=['local', 'local.functions', 'local.libs', 'local.statements'],
      )
