"""Ensure that the search function works correctly."""

from contactsearcher import search


def test_find_zero_matching_result():
    """Check to ensure that search for contacts works for one match."""
    contacts_database = """kylebarnes@hotmail.com,Records manager
joe70@yahoo.com,Network engineer
torresjames@white.info,Electrical engineer
shawkins@watson.com,Science writer"""
    contacts_list = search.search_for_email_given_job("nurse", contacts_database)
    assert len(contacts_list) == 0
    contacts_list = search.search_for_email_given_job(
        "physical therapit", contacts_database
    )
    assert len(contacts_list) == 0


def test_find_one_matching_result():
    """Check to ensure that search for contacts works for one match."""
    contacts_database = """kylebarnes@hotmail.com,Records manager
joe70@yahoo.com,Network engineer
torresjames@white.info,Electrical engineer
shawkins@watson.com,Science writer"""
    contacts_list = search.search_for_email_given_job("writer", contacts_database)
    assert len(contacts_list) == 1


def test_find_multiple_matching_result():
    """Check to ensure that search for contacts works for multiple matches."""
    contacts_database = """kylebarnes@hotmail.com,Records manager
joe70@yahoo.com,Network engineer
torresjames@white.info,Electrical engineer
shawkins@watson.com,Science writer"""
    contacts_list = search.search_for_email_given_job("engineer", contacts_database)
    assert len(contacts_list) == 2


def test_find_one_matching_result_partial():
    """Check to ensure that search for contacts works for one match with a partial string."""
    contacts_database = """kylebarnes@hotmail.com,Records manager
joe70@yahoo.com,Network engineer
torresjames@white.info,Electrical engineer
shawkins@watson.com,Science writer"""
    contacts_list = search.search_for_email_given_job("wri", contacts_database)
    assert len(contacts_list) == 1
    contacts_list = search.search_for_email_given_job("ter", contacts_database)
    assert len(contacts_list) == 1


def test_find_multiple_matching_result_partial():
    """Check to ensure that search for contacts works for multiple matches with a partial string."""
    contacts_database = """kylebarnes@hotmail.com,Records manager
joe70@yahoo.com,Network engineer
torresjames@white.info,Electrical engineer
shawkins@watson.com,Science writer"""
    contacts_list = search.search_for_email_given_job("engi", contacts_database)
    assert len(contacts_list) == 2
    contacts_list = search.search_for_email_given_job("neer", contacts_database)
    assert len(contacts_list) == 2
