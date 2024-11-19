try:
    print(10 / 0)  #
except ZeroDivisionError:
    print("Помилка: спроба поділити на нуль!")


def lol(f):
    '''
    Демонстраційна функція, яка уникає поділу на нуль.
    '''
    try:
        return f / 0
    except ZeroDivisionError:
        print("Помилка: поділ на нуль!")
        return None


class InvalidToolTypeError(Exception):
    """Виняток для неправильного номіналу карти."""
    def __init__(self, tool_type: str):
        """
        Ініціалізує помилку з неправильним номіналом карти.
        :param tool_type: Неправильний номінал карти.
        """
        self.message = f"Неправильний номінал карти: {tool_type}. Допустимі значення: Ace, King, Queen, Jack."
        super().__init__(self.message)


class InvalidKitError(Exception):
    """Виняток для неправильної масті карти."""
    def __init__(self, kit: str):
        """
        Ініціалізує помилку з неправильною мастю карти.
        :param kit: Неправильна масть карти.
        """
        self.message = f"Неправильна масть карти: {kit}. Допустимі значення: spades, heart, club, diamond."
        super().__init__(self.message)


try:
    print(lol(101))
except ZeroDivisionError:
    print("Помилка при виконанні функції lol!")

from random import shuffle


class Card:
    '''Клас, який реалізує методи та властивості гральної стандартної карти'''

    def __init__(self, type: str, k: str):
        self.toolType = type
        self.kit = k
        self.__SetScore()

    @property
    def toolType(self) -> str:
        return self.__toolType

    @toolType.setter
    def toolType(self, t: str):
        if t and isinstance(t, str):
            if t in ("Ace", "King", "Queen", "Jack"):
                self.__toolType = t
            else:
                raise ValueError(f"Неправильний номінал карти: {t}")
        else:
            raise ValueError("Номінал карти повинен бути рядком!")

    @property
    def kit(self) -> str:
        return self.__kit

    @kit.setter
    def kit(self, k: str):
        if k and isinstance(k, str):
            if k in ('spades', 'heart', 'club', 'diamond'):
                self.__kit = k
            else:
                raise ValueError(f"Неправильна масть карти: {k}")
        else:
            raise ValueError("Масть карти повинна бути рядком!")

    def __SetScore(self):
        if self.__toolType == 'Ace':
            self.score = 11
        elif self.__toolType == 'King':
            self.score = 4
        elif self.__toolType == 'Queen':
            self.score = 3
        elif self.__toolType == 'Jack':
            self.score = 2
        else:
            self.score = 0

    def __str__(self) -> str:
        return f'{self.toolType} {self.kit}'

    def __eq__(self, other: 'Card') -> bool:
        return self.__toolType == other.__toolType and self.__kit == other.__kit

    __repr__ = __str__


class CardCollection:
    '''Клас для роботи з колодою чи іншими наборами карт'''

    __MAX_COUNT_CARDS = 16
    CURRENT_COUNT_CARDS = 0

    def __init__(self, n: str):
        self.setName(n)
        self.cards = []

    def getName(self) -> str:
        return self.__name.upper()

    def setName(self, n: str):
        if n:
            self.__name = n
        else:
            self.__name = None

    def addCard(self, card: 'Card'):
        if CardCollection.CURRENT_COUNT_CARDS + 1 > CardCollection.__MAX_COUNT_CARDS:
            raise CountCardsError(CardCollection.CURRENT_COUNT_CARDS + 1)
        if any(c == card for c in self.cards):
            raise DoubleCardsError(card)
        CardCollection.CURRENT_COUNT_CARDS += 1
        self.cards.append(card)

    def getNumberOfCards(self) -> int:
        return len(self.cards)

    def removeCard(self, another_seq: 'CardCollection', card_number: int):
        if 0 <= card_number < self.getNumberOfCards():
            card_to_move = self.cards.pop(card_number)
            another_seq.addCard(card_to_move)
        else:
            print('Карту перемістити не вдалося. Спробуйте ще раз.')

    def shuffling(self):
        shuffle(self.cards)

    def __str__(self) -> str:
        result = f'{self.getName()}:\n'
        for i in range(0, self.getNumberOfCards(), 6):
            result += f'\t\t'.join(str(card) for card in self.cards[i:i + 6]) + "\n"
        return result


class CountCardsError(Exception):
    def __init__(self, count_c: int):
        self.message = f'''Кількість карт не повинна перевищувати 16, але є {count_c} карт'''

    def __str__(self) -> str:
        return self.message


class DoubleCardsError(Exception):
    def __init__(self, card: 'Card'):
        self.message = f'''Карта {card} вже є в колоді.'''

    def __str__(self) -> str:
        return self.message


kit = ['heart', 'spades', 'diamond', 'club']
toolType = ['Ace', 'King', 'Queen', 'Jack']

deck = CardCollection('deck')

for tp in toolType:
    for kt in kit:
        deck.addCard(Card(tp, kt))

print(deck)

try:
    deck.addCard(Card('Ace', 'club'))
except CountCardsError:
    print('Спроба додати зайву карту! Гравця виключено.')
except DoubleCardsError as e:
    print(e)
else:
    print('Карта додана успішно.')

finally:
    deck.shuffling()
    print(deck)


def decoFun(function):
    def wrap():
        print('Код до функції')
        function()
        print('Код після функції')

    return wrap


@decoFun
def my_fun():
    print('Наш код')


print('-' * 100)
my_fun()

from datetime import datetime
from random import randint


def deco_timer(func):
    def timer():
        start_time = datetime.now()
        result = func()
        finish_time = datetime.now()
        print(f'Час виконання функції: {finish_time - start_time}')
        return result

    return timer


@deco_timer
def spanch_sort():
    lst = [randint(0, 10000) for _ in range(30000)]
    for i in range(len(lst)):
        swapped = False
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst


spanch_sort()
