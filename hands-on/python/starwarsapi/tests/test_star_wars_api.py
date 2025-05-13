import pytest
from src.star_wars_api_impl import StarWarsAPIImpl
from src.star_wars_character import StarWarsCharacter


def test_get_luke_skywalker():
    """Test that get_luke_skywalker returns Luke Skywalker's data"""
    star_wars_api = StarWarsAPIImpl()
    luke_skywalker = star_wars_api.get_luke_skywalker()
    
    assert luke_skywalker is not None
    assert luke_skywalker.name == "Luke Skywalker"
    assert luke_skywalker.height == "172"
    assert luke_skywalker.gender == "male"

def test_get_darth_vader():
    """Test that get_darth_vader returns Darth Vader's data"""
    star_wars_api = StarWarsAPIImpl()
    darth_vader = star_wars_api.get_darth_vader()
    
    assert darth_vader is not None
    assert darth_vader.name == "Darth Vader"
    assert darth_vader.height == "202"
    assert darth_vader.gender == "male"