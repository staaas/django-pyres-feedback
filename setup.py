# -*- coding: utf-8 -*-
""" Setup file for easy installation """
from setuptools import setup, find_packages


version = __import__('feedback').__version__

LONG_DESCRIPTION = """
django-pyres-feedback is an application for
feedback submission via Pyres in Django. 
"""

setup(name='django-pyres-feedback',
      version=version,
      author='Stas Rudakou',
      author_email='dev@nott.cc',
      description='Feedback submission in Django via Pyres.',
      license='BSD',
      keywords='django, pyres, feedback, application',
      url='https://github.com/nott/django-pyres-feedback',
      packages=find_packages(),
      include_package_data=True,
      long_description=LONG_DESCRIPTION,
      install_requires=['django>=1.2.0',
                        'pyres>=1.0',],
      classifiers=['Framework :: Django',
                   'Development Status :: 4 - Beta',
                   'Topic :: Internet',
                   'License :: OSI Approved :: BSD License',
                   'Intended Audience :: Developers',
                   'Environment :: Web Environment',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7'])
