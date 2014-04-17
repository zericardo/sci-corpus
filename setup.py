# -*- coding: utf-8 -*-

"""
To install just execute

# python install.py install

Have fun :)

"""

from distutils.core import setup

print 'Installing Scientific Corpus ...'

setup(name='sci_corpus', 
      version='0.1', 
      description='Scientific Corpus Manager',
      
      author='Daniel Cosmo Pizetta, Jose Ricardo Furlan Ronqui, Tiago de Campos', 
      author_email='daniel.pizett@usp.br, xxx@usp.br, tiago.campos@usp.br',

      packages=['sci_corpus', 
                'sci_corpus.xxx'],

      package_data={'':['README.txt', 
                        'sci_corpus/ui/*.ui']}, 
      
      scripts=['sci_corpus/scripts/sci_corpus.py'], 
               
      download_url='')
