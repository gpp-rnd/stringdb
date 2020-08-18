#!/usr/bin/env python

"""Tests for `stringdb` package."""

import pytest


import stringdb


@pytest.fixture()
def mapped_ddr_ids():
    """Example string ids"""
    string_ids = stringdb.get_string_ids(['TP53', 'BRCA1', 'FANCD1', 'FANCL'])
    return string_ids


def test_string_mapping(mapped_ddr_ids):
    assert (mapped_ddr_ids['preferredName'].isin(['TP53', 'BRCA1', 'BRCA2', 'FANCL'])
            .sum() / mapped_ddr_ids.shape[0] == 1)


def test_functional_annotation(mapped_ddr_ids):
    mapped_pathways = stringdb.get_functional_annotation(mapped_ddr_ids.stringId)
    assert (mapped_pathways.loc[mapped_pathways.term == 'GO:0006281', 'number_of_genes'].values[0] == 4)  # DNA repair


def test_network(mapped_ddr_ids):
    network = stringdb.get_network(mapped_ddr_ids.stringId)
    assert (network.shape[0] == 5)  # edges between everything except TP53 and FANCL


def test_ppi_enrichment(mapped_ddr_ids):
    enrichment_stats = stringdb.get_ppi_enrichment(mapped_ddr_ids.stringId)
    assert enrichment_stats['p_value'].values[0] < 0.05


def test_interaction_partners(mapped_ddr_ids):
    interaction_partners = stringdb.get_interaction_partners(mapped_ddr_ids.stringId)
    n_interactors = interaction_partners.preferredName_A.value_counts()
    assert n_interactors['TP53'] > n_interactors['FANCL']


def test_enrichment(mapped_ddr_ids):
    enrichment_df = stringdb.get_enrichment(mapped_ddr_ids.stringId)
    assert enrichment_df.sort_values('fdr')['term'].values[0] == 'PMID.22918243'
    background_enrichment = stringdb.get_enrichment(mapped_ddr_ids.stringId,
                                                    background_string_identifiers=mapped_ddr_ids.stringId)
    assert background_enrichment.shape[0] == 0
