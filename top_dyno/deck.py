from utils import read_json, write_json
import random

DYNO_NAMES = ("Mallorgassauro Rex", "Devceratops", "Pythondonte", "Galinha Caipira")

def generate_random_dynos_data() -> list[dict]:
    dyno_cards = []

    for dyno_name in DYNO_NAMES:
        dyno_dict  = {'name': dyno_name, 'strength': 10, 'agility': 8, 'heigth': 7}
        dyno_cards.append(dyno_dict)

    return dyno_cards