========
stringdb
========


.. image:: https://img.shields.io/pypi/v/stringdb.svg
        :target: https://pypi.python.org/pypi/stringdb

.. image:: https://api.travis-ci.com/gpp-rnd/stringdb.svg
        :target: https://travis-ci.com/gpp-rnd/stringdb

.. image:: https://readthedocs.org/projects/stringdb/badge/?version=latest
        :target: https://stringdb.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Python functions to access the STRINGdb API, a source of protein-protein association networks.
Documentation for the api can be found here: https://string-db.org/help/api/

* Free software: MIT license
* Documentation: https://stringdb.readthedocs.io.

Tutorial
--------
To install::

    $ pip install stringdb

Basic Usage
^^^^^^^^^^^
::

    import stringdb
    genes = ['TP53', 'BRCA1', 'FANCD1', 'FANCL']
    string_ids = stringdb.get_string_ids(genes)
    enrichment_df = stringdb.get_enrichment(string_ids.queryItem)

There are 5 functions for querying a list of stringIds, which follow
the pattern get\_\*

where \* can be 'enrichment', 'interaction\_partners', 'ppi\_enrichment',
'network', and 'functional\_annotation'


TODO
----

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
