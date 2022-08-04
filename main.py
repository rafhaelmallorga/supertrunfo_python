import top_dyno

FILEPATH = 'top_dyno.json'

def main():
    # print(top_dyno.generate_random_dynos_data())
    top_dyno.create_random_dyno_deck(FILEPATH)

if __name__ == '__main__':
    main()