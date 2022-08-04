from utils import read_json, write_json
import random

DYNO_NAMES = ("Mallorgassauro Rex", "Devceratops", "Pythondonte", "Galinha Caipira")

def generate_random_dynos_data() -> list[dict]:
    return [
        {
            'name': dyno_name, 'strength': random.randint(1, 10), 'agility': round(random.uniform(0, 10), 1), 'heigth': round(random.uniform(0, 10), 2)
        } for dyno_name in DYNO_NAMES
    ] 

def create_random_dyno_deck(filepath: str) -> None:
    generated_dynos = generate_random_dynos_data()

    write_json(filepath, generated_dynos)
    