from ast import main
from os import system
from collections import namedtuple
from random import shuffle

card = namedtuple('Карточка', ('name', 'color'))

class Game:

    def __init__(self) -> None:
        self.__cards = {
            'Житель': card('Житель', 'красный'),
            'Комиссар': card('Комиссар', 'красный'),
            'Доктор': card('Доктор', 'красный'),
            'Мафия': card('Мафия', 'чёрный'),
            'Маньяк': card('Маньяк', 'чёрный')
        }

    def very_small_game(self, u_c: int):
        deck = [self.__cards['Мафия'], self.__cards['Комиссар']]
        return deck + [self.__cards['Житель'] for i in range((u_c - len(deck)))]

    def small_game(self, u_c: int):
        maf = self.__cards['Мафия']
        deck = [maf, maf, self.__cards['Комиссар']]
        return deck + [self.__cards['Житель'] for i in range((u_c - len(deck)))]

    def medium_game(self, u_c: int):
        maf = self.__cards['Мафия']
        deck = [maf, maf, self.__cards['Комиссар'], self.__cards['Доктор']]
        return deck + [self.__cards['Житель'] for i in range((u_c - len(deck)))]

    def big_game(self, u_c: int):
        maf = self.__cards['Мафия']
        deck = [maf, maf, maf, self.__cards['Комиссар'],
                self.__cards['Доктор'], self.__cards['Маньяк']]
        return deck + [self.__cards['Житель'] for i in range((u_c - len(deck)))]

    def main(self):
        system('cls')

try:
    result = int(input('Укажите количество игроков: '))
except:
        raise TypeError('Введите число!')

new_game = Game()

if result in (6, 7):
    deck = new_game.very_small_game(result)
elif result in (8, 9, 10):
    deck = new_game.small_game(result)  #9
elif result in (11, 12):
    deck = new_game.medium_game(result)
elif result in (13, 14, 15):
    deck = new_game.big_game(result)
else:
    raise 'Игроков может быть от 6-ти до 15-ти!'

shuffle(deck)

for card_num in range(len(deck)):
    input('Нажмите enter, чтоб посмотреть карту:')
    current_card = deck[card_num]
    print(f'[{card_num + 1}] {current_card.name} | {current_card.color}')
    input('Нажмите enter, чтоб скрыть карту:')
    system('cls')
    print('Приятной игры!')

if __name__ == '__main__':
    main()
