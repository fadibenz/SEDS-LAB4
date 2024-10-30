import pytest
import SEDS_LAB4.SEDS_LAB4.modeling.model as model

def test_serve_beer_legal():
    adult = 25
    assert model.serve_beer(adult) == "Have beer"


def test_serve_beer_illegal():
    child = 10
    assert model.serve_beer(child) == "No beer"

def test_for_clean_row():
    string = "2,081\t314,942\n"
    assert model.row_to_list(string) == ["2,081","314,942"]

def test_for_missing_area():
    assert model.row_to_list("\t293,410") is None

def test_for_missing_tab():
    assert model.row_to_list("2,93,410\n") is None
