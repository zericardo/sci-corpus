# -*- coding: utf-8 -*-

"""
To install just execute.

# python setup.py install

Have fun :)

"""

#from distutils.core import setup
import sys
from cx_Freeze import setup, Executable

print 'Installing Scientific Corpus ...'

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name='sci-corpus',
      version='0.1',
      description='Scientific Corpus Manager',
      author='Daniel Cosmo Pizetta, Jose Ricardo Furlan Ronqui, Tiago de Campos',
      author_email='daniel.pizetta@usp.br, jose.ronqui@usp.br, tiago.campos@usp.br',
      #options = {'build_exe':build_exe_options}
      executables=[Executable("sci_corpus/sci_corpus_main.py", base=base)],
      download_url='https://github.com/zericardo182/sci-corpus')

"""
      packages=['sci_corpus',
                'sci_corpus.xxx'],

      package_data={'/Sci Corpus':['README.txt',
                        'sci_corpus/ui/*.ui']},
      
      scripts=['sci_corpus/scripts/sci_corpus.py'],
      
"""
