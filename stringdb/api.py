"""api module. Functions to access the STRING API"""
import pandas as pd
import io
import requests


def build_request_url(method, output_format='tsv'):
    """Create url to query the string database

    Allows us to create stubs for querying the string api with various methods

    Parameters
    ----------
    method: str
        options - get_string_ids, network, interaction_partners, homology, homology_best,
            enrichment, functional_annotation, ppi_enrichment, version
    output_format: str, optional
        options - tsv, tsv-non-header, json, xml

    Returns
    -------
    str
        request URL
    """
    string_api_url = "https://string-db.org/api"
    request_url = "/".join([string_api_url, output_format, method])
    return request_url


def handle_results(results):
    """Handle results returned from string"""
    if results.ok:
        data = results.content.decode('utf8')
        # assumes tsv input
        df = pd.read_csv(io.StringIO(data), sep='\t')
        return df
    else:
        raise ValueError(results.reason)


def get_string_ids(identifiers, species=9606, limit=1, echo_query=1,
                   caller_identity='https://github.com/gpp-rnd/stringdb'):
    """Map gene symbols to string ids

    Parameters
    ----------
    identifiers: list
        gene symbols to map to string ids
    species: int, optional
        species identifier
    limit: int, optional
        limits the number of matches per query (best match comes first)
    echo_query: int, optional
        insert column with input identifiers. Takes values 0 or 1 (boolean)
    caller_identity: str, optional
        personal identifier for string

    Returns
    -------
    DataFrame
        mapping of string ids
    """
    request_url = build_request_url("get_string_ids")
    params = {
        "identifiers": "\r".join(identifiers),  # your protein list
        "species": species,  # species NCBI identifier
        "limit": limit,  # only one (best) identifier per input protein
        "echo_query": echo_query,  # see your input identifiers in the output
        "caller_identity": caller_identity
    }
    results = requests.post(request_url, data=params)
    df = handle_results(results)
    return df


def get_functional_annotation(identifiers, species=9606, caller_identity='https://github.com/gpp-rnd/stringdb',
                              allow_pubmed=0):
    """Get all pathways for a list of string ids

    Parameters
    ----------
    identifiers: list
        list of string ids
    species: int, optional
        species NCBI identifier
    caller_identity: str, optional
        personal identifier for string
    allow_pubmed: int, optional
        include pubmed articles, options - 1 or 0

    Returns
    -------
    DataFrame
        mapping between string ids and gene pathways
    """
    request_url = build_request_url("functional_annotation")
    pathway_list = []
    # limited to 2000 queries by string
    for i in range(0, len(identifiers), 2000):
        curr_ids = identifiers[i:(i + 2000)]
        params = {
            "identifiers": "\r".join(curr_ids),  # protein list
            "species": species,
            "caller_identity": caller_identity,
            "allow_pubmed": allow_pubmed
        }
        results = requests.post(request_url, data=params)
        df = handle_results(results)
        pathway_list.append(df)
    pathway_df = pd.concat(pathway_list)
    return pathway_df


def get_network(identifiers, species=9606, required_score=400,
                caller_identity='https://github.com/gpp-rnd/stringdb', add_nodes=0):
    """Get the ppi network for a list of string ids

    Parameters
    ----------
    identifiers: list
        list of string ids
    species: int, optional
        species NCBI identifier
    required_score: int, optional
        score cutoff for edges, corresponds to probability of belonging to same kegg pathway
    caller_identity: str, optional
        personal identifier for string
    add_nodes: int, optional
        number of nodes to add to the network based on confidence

    Returns
    -------
    DataFrame
        network edges
    """
    request_url = build_request_url("network")
    params = {
        "identifiers": "\r".join(identifiers),  # your protein list
        "species": species,  # species NCBI identifier
        "caller_identity": caller_identity,
        "required_score": required_score,
        "add_nodes": add_nodes
    }
    results = requests.post(request_url, data=params)
    df = handle_results(results)
    return df


def get_ppi_enrichment(identifiers, species=9606, required_score=400,
                       caller_identity='https://github.com/gpp-rnd/stringdb'):
    """Calculate ppi enrichment

    Parameters
    ----------
    identifiers: list
        list of string ids
    species: int, optional
        species NCBI identifier
    required_score: int, optional
        score cutoff for edges, corresponds to probability of belonging to same kegg pathway
    caller_identity: str, optional
        personal identifier for string

    Returns
    -------
    DataFrame
        one row DataFrame with ppi enrichment stats
    """
    request_url = build_request_url("ppi_enrichment")
    params = {
        "identifiers": "\r".join(identifiers),  # your protein list
        "species": species,  # species NCBI identifier
        "required_score": required_score,
        "caller_identity": caller_identity
    }
    results = requests.post(request_url, data=params)
    df = handle_results(results)
    return df


def get_interaction_partners(identifiers, species=9606, required_score=400,
                             limit=None, caller_identity='https://github.com/gpp-rnd/stringdb'):
    """Get interactions for identified proteins and all other string proteins

    Parameters
    ----------
    identifiers: list
        list of string ids
    species: int, optional
        species NCBI identifier
    required_score: int, optional
        score cutoff for edges, corresponds to probability of belonging to same kegg pathway
    limit: int, optional
        limit the number of interactors returned for each protein, ranked by score
    caller_identity: str, optional
        personal identifier for string

    Returns
    -------
    DataFrame
    """
    request_url = build_request_url("interaction_partners")
    params = {
        "identifiers": "\r".join(identifiers),  # your protein list
        "species": species,  # species NCBI identifier
        "required_score": required_score,
        "caller_identity": caller_identity,
    }
    if limit is not None:
        params['limit'] = limit
    results = requests.post(request_url, data=params)
    df = handle_results(results)
    return df


def get_enrichment(identifiers, background_string_identifiers=None, species=9606,
                   caller_identity='https://github.com/gpp-rnd/stringdb'):
    """Get functional enrichment for a list of proteins

    Parameters
    ----------
    identifiers: list
        list of string ids
    background_string_identifiers: list
        list of string ids to use as background
    species: int, optional
        species NCBI identifier
    caller_identity: str, optional
        personal identifier for string

    Returns
    -------
    DataFrame
        enriched pathways
    """
    request_url = build_request_url("enrichment")
    params = {
        "identifiers": "\r".join(identifiers),  # your protein list
        "species": species,  # species NCBI identifier
        "caller_identity": caller_identity,
    }
    if background_string_identifiers is not None:
        params['background_string_identifiers'] = "\r".join(background_string_identifiers)
    results = requests.post(request_url, data=params)
    df = handle_results(results)
    return df
