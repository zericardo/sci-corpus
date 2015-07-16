Sci Corpus
==========

Scientific corpus manager.

See `Sci Corpus Wiki <https://github.com/zericardo/sci-corpus/wiki>`_ for information about simple use.

Dependencies:

* Python 2.7 >
* PySide 1.2 >
* sqlite3
* python - lxml

Installing
==========

To install, browse to your sci-corpus folder and run this following command:
::
      # python setup.py install

It will automatically install all dependencies.

For Windows users, you need to use CMD as administrator and run inside the sci-corpus the following commands:
::
      # c:\Python27\python.exe setup.py install

However, it eventually doesn't work because of its dependencies from Visual Studio for compiler .
So download the binaries from site.


* **Tip: qmake not found Error**

If during the installation of PySide you see an error stating that qmake was not found, this may be related to a long-standing change in nomenclature of qmake binary file in Fedora systems. Fortunately, there's a very simple solution.
In the near future, this should be incorporated automatically in the installation (using --qmake flag).

1. You'll first need to actually locate it:
::
      $ locate qmake | grep bin

2. One of the solutions you'll find is something very similar to
::
      /usr/bin/qmake-qt4

Use this path (or whatever you've found instead) in the next item.

3. Create a symbolic link (as root!):
::
      # ln -s /usr/bin/qmake-qt4 /usr/bin/qmake

Then, retry the installation process and everything should work properly!
