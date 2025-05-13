import requests
from star_wars_api import StarWarsAPI
from star_wars_character import StarWarsCharacter


class StarWarsAPIImpl(StarWarsAPI):
    """Implementation of the Star Wars API client"""
    
    def __init__(self):
        self.base_url = "https://swapi.info/api"
    
    def get_luke_skywalker(self) -> StarWarsCharacter:
        """
        Get Luke Skywalker's information
        Returns:
            StarWarsCharacter: Luke Skywalker's data
        Raises:
            Exception: If an error occurs while fetching the data
        """
        url = f"{self.base_url}/people/1/"
        response = requests.get(url, allow_redirects=True)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        return StarWarsCharacter.from_dict(response.json())
    
    def get_darth_vader(self) -> StarWarsCharacter:
        """
        Get Darth Vader's information
        Returns:
            StarWarsCharacter: Darth Vader's data
        Raises:
            Exception: If an error occurs while fetching the data
        """
        return self._get_star_wars_character(4)
    
    def _get_star_wars_character(self, character_id: int) -> StarWarsCharacter:
        """
        Get a Star Wars character by ID
        Args:
            character_id: The ID of the character to fetch
        Returns:
            StarWarsCharacter: The character data
        Raises:
            Exception: If an error occurs while fetching the data
        """
        url = f"{self.base_url}/people/{character_id}/"
        response = requests.get(url, allow_redirects=True)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        return StarWarsCharacter.from_dict(response.json())
