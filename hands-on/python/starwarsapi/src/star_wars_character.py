from dataclasses import dataclass
from typing import List


@dataclass
class StarWarsCharacter:
    """Data class for Star Wars character from SWAPI"""
    name: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    homeworld: str
    films: List[str]
    species: List[str]
    vehicles: List[str]
    starships: List[str]
    created: str
    edited: str
    url: str

    @classmethod
    def from_dict(cls, data: dict) -> 'StarWarsCharacter':
        """Create a StarWarsCharacter from a dictionary"""
        return cls(
            name=data.get('name', ''),
            height=data.get('height', ''),
            mass=data.get('mass', ''),
            hair_color=data.get('hair_color', ''),
            skin_color=data.get('skin_color', ''),
            eye_color=data.get('eye_color', ''),
            birth_year=data.get('birth_year', ''),
            gender=data.get('gender', ''),
            homeworld=data.get('homeworld', ''),
            films=data.get('films', []),
            species=data.get('species', []),
            vehicles=data.get('vehicles', []),
            starships=data.get('starships', []),
            created=data.get('created', ''),
            edited=data.get('edited', ''),
            url=data.get('url', '')
        )
