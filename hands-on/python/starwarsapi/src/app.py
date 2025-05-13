from star_wars_api_impl import StarWarsAPIImpl


def main():
    """Main function to demonstrate the Star Wars API client"""
    print("Star Wars API Client")
    print("--------------------")
    
    api = StarWarsAPIImpl()
    
    # Get Luke Skywalker
    luke = api.get_luke_skywalker()
    print(f"\nName: {luke.name}")
    print(f"Height: {luke.height} cm")
    print(f"Mass: {luke.mass} kg")
    print(f"Hair color: {luke.hair_color}")
    print(f"Appears in {len(luke.films)} films")
    
    # Get Darth Vader
    vader = api.get_darth_vader()
    print(f"\nName: {vader.name}")
    print(f"Height: {vader.height} cm")
    print(f"Mass: {vader.mass} kg")
    print(f"Hair color: {vader.hair_color}")
    print(f"Appears in {len(vader.films)} films")


if __name__ == "__main__":
    main()