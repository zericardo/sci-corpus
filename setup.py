#! python
# -*- coding: utf-8 -*-

"""
Script to install Sci Corpus.

# python setup.py install

Have fun :)

"""

from distutils.core import setup
import platform
import os
from sci_corpus import sci_corpus_main

print 'Installing Scientific Corpus ...'

base = None

if platform.system() == 'Windows':
    base = "Win32GUI"

setup(name=sci_corpus_main.__pname__,
      version=sci_corpus_main.__version__,
      description=sci_corpus_main.__ext_name__,
      
      author='Daniel Cosmo Pizetta, Jose Ricardo Furlan Ronqui, Tiago de Campos',
      author_email='daniel.pizetta@usp.br, jose.ronqui@usp.br, tiago.campos@usp.br',
      
      download_url='https://github.com/zericardo182/sci-corpus',
      
      packages=['sci_corpus',
                'sci_corpus.ui'],
      
      package_data={'/Sci Corpus':['examples',
                                   'docs']}
      
      scripts=['sci_corpus/scripts/sci_corpus.py'])
