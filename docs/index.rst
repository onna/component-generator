========
Contents
========

.. toctree::
   :maxdepth: 2

   installation
   usage
   reference/index
   contributing
   authors
   changelog

Generate backend components quickly

* Free software: BSD 2-Clause License

Installation
============

::

    pip install component-generator

You can also install the in-development version with::

    pip install https://github.com/onna/python-component-generator/archive/master.zip


Documentation
=============


https://python-component-generator.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
