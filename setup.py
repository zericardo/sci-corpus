#! python
# -*- coding: utf-8 -*-
"""
Script to install Sci Corpus.

.. module:: setup
   :platform: Unix, Windows
   :synopsis: Script to install Sci Corpus.
   
.. moduleauthor:: Daniel Pizetta <daniel.pizetta@usp.br>

This script install sci corpus in your computer.


"""

from distutils.core import setup
import platform
import os
import sys
from sci_corpus import sci_corpus_main

def dependancyChecks():
    """
    Perform some dependency checks.

	This verification was based on Eric Python IDE dependency check.
    """
    
    errors=[]

    print('Checking dependencies ...')

    print("Checking Python ...")
    if sys.version_info < (2, 7, 0):
        print('Sorry, you must have Python 2.7.0 or higher.')
        print('You can find here: <https://www.python.org/>')
        errors.append('Python')
    elif sys.version_info > (2, 9, 9):
        print('Sorry, Sci Corpus requires Python 2.7 for running.')
        errors.append('Python')
    else:
    	print("Python Version: {0:d}.{1:d}.{2:d}".format(*sys.version_info[:3]))

    print("Checking PySide Library ...")
    try:
        import PySide
    except ImportError as msg:
        print('Sorry, please install PySide 1.1.0 or higher.')
        print('You can find here: <http://qt-project.org/wiki/PySide>')
        print('Error: {0}'.format(msg))
        errors.append('PySide')
    else:
        print("PySide Version: {0:d}.{1:d}.{2:d}".format(PySide.__version_info__[:3]))
        print("Qt Version: {0:d}.{1:d}.{2:d}".format(PySide.QtCore.__version_info__[:3]))

	if errors != []:
		print("Please correct the errors shown and try again.")
		exit(1)
	else:
		print("Dependancy checker was not found errors.")



print 'Preparing to install Sci Corpus ...'

dependancyChecks()

print('Installing Sci Corpus ...')

classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Window',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: MIT',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Topic :: Office/Business',
]

setup(name=sci_corpus_main.__pname__,
      version=sci_corpus_main.__version__,
      description=sci_corpus_main.__ext_name__,
      
      author='Daniel Cosmo Pizetta, Jose Ricardo Furlan Ronqui, Tiago de Campos',
      author_email='daniel.pizetta@usp.br, jose.ronqui@usp.br, tiago.campos@usp.br',
      
      download_url='https://github.com/zericardo182/sci-corpus',
      
      packages=['sci_corpus',
                'sci_corpus.ui'],
      
      package_data={'/Sci Corpus':['examples',
                                   'docs']}, 
      
      scripts=['sci_corpus/scripts/sci_corpus.py'])
