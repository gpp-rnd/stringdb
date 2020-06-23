========
stringdb
========


.. image:: https://img.shields.io/pypi/v/stringdb.svg
        :target: https://pypi.python.org/pypi/stringdb

.. image:: https://img.shields.io/travis/gpp-rnd/stringdb.svg
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

.. code:: ipython3

    import stringdb

.. code:: ipython3

    genes = ['TP53', 'BRCA1', 'FANCD1', 'FANCL']
    string_ids = stringdb.get_string_ids(genes)
    string_ids




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>queryItem</th>
          <th>queryIndex</th>
          <th>stringId</th>
          <th>ncbiTaxonId</th>
          <th>taxonName</th>
          <th>preferredName</th>
          <th>annotation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>TP53</td>
          <td>0</td>
          <td>9606.ENSP00000269305</td>
          <td>9606</td>
          <td>Homo sapiens</td>
          <td>TP53</td>
          <td>Cellular tumor antigen p53; Acts as a tumor su...</td>
        </tr>
        <tr>
          <th>1</th>
          <td>BRCA1</td>
          <td>1</td>
          <td>9606.ENSP00000418960</td>
          <td>9606</td>
          <td>Homo sapiens</td>
          <td>BRCA1</td>
          <td>Breast cancer type 1 susceptibility protein; E...</td>
        </tr>
        <tr>
          <th>2</th>
          <td>FANCD1</td>
          <td>2</td>
          <td>9606.ENSP00000369497</td>
          <td>9606</td>
          <td>Homo sapiens</td>
          <td>BRCA2</td>
          <td>Breast cancer type 2 susceptibility protein; I...</td>
        </tr>
        <tr>
          <th>3</th>
          <td>FANCL</td>
          <td>3</td>
          <td>9606.ENSP00000385021</td>
          <td>9606</td>
          <td>Homo sapiens</td>
          <td>FANCL</td>
          <td>E3 ubiquitin-protein ligase FANCL; Ubiquitin l...</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    enrichment_df = stringdb.get_enrichment(string_ids.queryItem)
    enrichment_df.sort_values('fdr')




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>category</th>
          <th>term</th>
          <th>number_of_genes</th>
          <th>number_of_genes_in_background</th>
          <th>ncbiTaxonId</th>
          <th>inputGenes</th>
          <th>preferredNames</th>
          <th>p_value</th>
          <th>fdr</th>
          <th>description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>64</th>
          <td>PMID</td>
          <td>PMID.22918243</td>
          <td>4</td>
          <td>8</td>
          <td>9606</td>
          <td>TP53,FANCD1,FANCL,BRCA1</td>
          <td>TP53,BRCA2,FANCL,BRCA1</td>
          <td>8.100000e-14</td>
          <td>1.160000e-08</td>
          <td>(2012) Switch of FANCL, a key FA-BRCA componen...</td>
        </tr>
        <tr>
          <th>106</th>
          <td>PMID</td>
          <td>PMID.26842001</td>
          <td>4</td>
          <td>12</td>
          <td>9606</td>
          <td>TP53,FANCD1,FANCL,BRCA1</td>
          <td>TP53,BRCA2,FANCL,BRCA1</td>
          <td>2.980000e-13</td>
          <td>2.140000e-08</td>
          <td>(2016) Fanconi anemia genes in lung adenocarci...</td>
        </tr>
        <tr>
          <th>127</th>
          <td>PMID</td>
          <td>PMID.28423363</td>
          <td>4</td>
          <td>22</td>
          <td>9606</td>
          <td>TP53,FANCD1,FANCL,BRCA1</td>
          <td>TP53,BRCA2,FANCL,BRCA1</td>
          <td>2.450000e-12</td>
          <td>2.390000e-08</td>
          <td>(2017) Multiple-gene panel analysis in a case ...</td>
        </tr>
        <tr>
          <th>126</th>
          <td>PMID</td>
          <td>PMID.28387924</td>
          <td>4</td>
          <td>15</td>
          <td>9606</td>
          <td>TP53,FANCD1,FANCL,BRCA1</td>
          <td>TP53,BRCA2,FANCL,BRCA1</td>
          <td>6.340000e-13</td>
          <td>2.390000e-08</td>
          <td>(2017) High number of kinome-mutations in non-...</td>
        </tr>
        <tr>
          <th>79</th>
          <td>PMID</td>
          <td>PMID.24439051</td>
          <td>4</td>
          <td>21</td>
          <td>9606</td>
          <td>TP53,FANCD1,FANCL,BRCA1</td>
          <td>TP53,BRCA2,FANCL,BRCA1</td>
          <td>2.070000e-12</td>
          <td>2.390000e-08</td>
          <td>(2014) Poly(ADP-ribose) polymerase inhibitor C...</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>12</th>
          <td>InterPro</td>
          <td>IPR013083</td>
          <td>2</td>
          <td>441</td>
          <td>9606</td>
          <td>FANCL,BRCA1</td>
          <td>FANCL,BRCA1</td>
          <td>3.000000e-03</td>
          <td>4.170000e-02</td>
          <td>Zinc finger, RING/FYVE/PHD-type</td>
        </tr>
        <tr>
          <th>150</th>
          <td>Process</td>
          <td>GO.0008285</td>
          <td>2</td>
          <td>669</td>
          <td>9606</td>
          <td>TP53,FANCD1</td>
          <td>TP53,BRCA2</td>
          <td>6.700000e-03</td>
          <td>4.210000e-02</td>
          <td>negative regulation of cell population prolife...</td>
        </tr>
        <tr>
          <th>149</th>
          <td>Process</td>
          <td>GO.0008283</td>
          <td>2</td>
          <td>676</td>
          <td>9606</td>
          <td>TP53,FANCD1</td>
          <td>TP53,BRCA2</td>
          <td>6.900000e-03</td>
          <td>4.260000e-02</td>
          <td>cell population proliferation</td>
        </tr>
        <tr>
          <th>141</th>
          <td>Process</td>
          <td>GO.0006325</td>
          <td>2</td>
          <td>683</td>
          <td>9606</td>
          <td>TP53,FANCD1</td>
          <td>TP53,BRCA2</td>
          <td>7.000000e-03</td>
          <td>4.310000e-02</td>
          <td>chromatin organization</td>
        </tr>
        <tr>
          <th>22</th>
          <td>Keyword</td>
          <td>KW-0007</td>
          <td>3</td>
          <td>3335</td>
          <td>9606</td>
          <td>TP53,FANCL,BRCA1</td>
          <td>TP53,FANCL,BRCA1</td>
          <td>1.730000e-02</td>
          <td>4.760000e-02</td>
          <td>Acetylation</td>
        </tr>
      </tbody>
    </table>
    <p>195 rows × 10 columns</p>
    </div>



We support 5 functions for querying a list of stringIds, which follow
the patter get\_\*

\* can be 'enrichment', 'interaction\_partners', 'ppi\_enrichment',
'network', and 'functional\_annotation'


TODO
----

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
