import pytest
import breweries


@pytest.mark.parametrize("key", ["my_addr", "api_key"])
def test_get_creds(key):
    rv = breweries.get_creds()
    assert key in rv


def test_generate_lat_long_length(test_addr):
    rv = breweries.generate_lat_long(test_addr)
    assert len(rv) == 6


def test_generate_lat_long_unique(test_addr):
    rv = breweries.generate_lat_long(test_addr)
    assert len(set(rv)) == 6


def test_clean_full_results_columns(sample_search_result):
    rv = breweries.clean_full_results(sample_search_result)
    assert len(rv.columns) == 8


def test_clean_full_results_length(sample_search_result):
    rv = breweries.clean_full_results(sample_search_result)
    assert len(rv) == 1
