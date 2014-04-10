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
      
      author='Daniel Cosmo Pizetta, Jose Ricardo Furlan Ronqui, Tiago Campo', 
      author_email='daniel.pizett@usp.br, zericardo182@gmail.com, xx@usp.br',

      packages=['sci_corpus', 
                'sci_corpus.xxx'],

      package_data={'':['README.txt', 
                        'torm_translator/dummy/*.f', 
                        'torm_translator/dialogs/ui/*.ui']}, 
      
      scripts=['torm_translator/scripts/translate_f_json.py', 
               'torm_translator/scripts/translate_json_xml.py',  
               'torm_translator/scripts/translate_f_xml.py', 
               'torm_translator/scripts/translator_gui.py'], 
               
      download_url='')
