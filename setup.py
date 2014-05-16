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
import os
import sys
from sci_corpus import sci_corpus_main

def dependancyChecks():
    """
    Perform some dependency checks.

	This verification was based on Eric Python IDE dependency check.
    """
    
    errors=[]

    print '\nChecking dependencies ...'

    print "Checking Python ..."
    if sys.version_info < (2, 7, 0):
        print 'Sorry, you must have Python 2.7.0 or higher.'
        print 'You can find here: <https://www.python.org/>'
        errors.append('Python')
    elif sys.version_info > (2, 9, 9):
        print 'Sorry, Sci Corpus requires Python 2.7 for running.'
        errors.append('Python')
    else:
    	print "Python Version: {}".format(*sys.version_info[:4])

    print "Checking PySide Library ..."
    try:
        import PySide
    except ImportError as msg:
        print 'Sorry, please install PySide 1.1.0 or higher.'
        print 'You can find here: <http://qt-project.org/wiki/PySide>'
        print 'Error: {0}'.format(msg)
        errors.append('PySide')
    else:
        print "PySide Version: {}".format(PySide.__version_info__[:3])
        print "Qt Version: {}".format(PySide.QtCore.__version_info__[:3])
        
        
    print "Checking LXML ..."
    try:
        import lxml
    except ImportError as msg:
        print 'Sorry, please install LXML 1.1.0 or higher.'
        print 'You can find here: <http://lxml.de/index.html#download>'
        print 'Error: {0}'.format(msg)
        errors.append('LXML')
    else:
        print "LXML Ok"
        
    print "Checking ReportLab ..."
    try:
        import reportlab
    except ImportError as msg:
        print 'Sorry, please install Report Lab.'
        print 'You can find here: <https://pypi.python.org/pypi/reportlab>'
        print 'Error: {0}'.format(msg)
        errors.append('LXML')
    else:
        print "ReportLab Ok"

	if errors != []:
		print "Please correct the errors shown and try again."
		exit(1)
	else:
		print "Dependancy checker was complete without errors."

print '\nPreparing to install Sci Corpus ...'

dependancyChecks()

print '\nInstalling Sci Corpus ...'

classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Window',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: MIT',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Topic :: Office/Business']
    
workspace = os.path.abspath(os.path.join(os.path.expanduser('~'),'Sci Corpus'))

#print 'Workspace: ', workspace

setup(name=sci_corpus_main.__name__,
      version=sci_corpus_main.__version__,
      description=sci_corpus_main.__ext_name__,
      author='Daniel Cosmo Pizetta, Jose Ricardo Furlan Ronqui, Tiago de Campos',
      author_email='daniel.pizetta@usp.br, jose.ronqui@usp.br, tiago.campos@usp.br',
      download_url='https://github.com/zericardo182/sci-corpus',
      classifiers=classifiers, 
      packages=['sci_corpus',
                'sci_corpus.ui'],
      #data_files=[(workspace,['README.rst'])], 
      scripts=['scicorpus'])
