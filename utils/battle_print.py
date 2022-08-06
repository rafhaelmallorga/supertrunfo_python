def print_card_vs_card(p1_card: dict, p2_card: dict, attr_to_compare) -> None:
    print('{} VS. {}'.format(p1_card['name'], p2_card['name']), end='\n\n')

    print('{}: {} X {} \n\nBattle Result:'.format(attr_to_compare.upper(), p1_card[attr_to_compare], p2_card[attr_to_compare]))

    if p1_card[attr_to_compare] > p2_card[attr_to_compare]:
        print(p1_card['name'], 'Wins ! ! !')
    elif p2_card[attr_to_compare] > p1_card[attr_to_compare]:
        print(p2_card['name'], 'Wins ! ! !')
    else:
        print('Draw . . .')

    