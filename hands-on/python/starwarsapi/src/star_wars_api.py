from abc import ABC, abstractmethod
from star_wars_character import StarWarsCharacter


class StarWarsAPI(ABC):
    """Interface for Star Wars API client"""
    
    @abstractmethod
    def get_luke_skywalker(self) -> StarWarsCharacter:
        """
        Get Luke Skywalker's information
        Returns:
            StarWarsCharacter: Luke Skywalker's data
        Raises:
            Exception: If an error occurs while fetching the data
        """
        pass

    @abstractmethod
    def get_darth_vader(self) -> StarWarsCharacter:
        """
        Get Darth Vader's information
        Returns:
            StarWarsCharacter: Darth Vader's data
        Raises:
            Exception: If an error occurs while fetching the data
        """
        pass