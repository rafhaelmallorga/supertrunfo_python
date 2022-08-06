import random
from utils import print_card_vs_card
from . import create_random_dyno_deck, generate_players_decks, generate_random_dynos_data

def get_random_attr(card: dict) -> str:
    card_keys = [key for key in card.keys() if key != 'name']
    
    return random.choice(card_keys)

def play(filepath: str) -> None:
    create_random_dyno_deck(filepath)
    p1_deck, p2_deck = generate_players_decks(filepath)

    for index, p1_card in enumerate(p1_deck):
        attr_to_compare = get_random_attr(p1_card)
        p2_card = p2_deck[index]

        print('-' * 100)
        print('ROUND {} \n'.format(index + 1))
        print_card_vs_card(p1_card, p2_card, attr_to_compare)
        print('-' * 100)