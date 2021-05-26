
import random


class LotoCard:

    def __init__(self, player_type):
        def check_sort_item(item):
            if isinstance(item, int):
                return item
            else:
                return random.randint(1, self._MAX_NUMBER)

        self.player_type = player_type
        self._card = [
            [],
            [],
            []
        ]
        self._MAX_NUMBER = 90
        self._MAX_NUMBER_IN_CARD = 15
        self._numbers_stroked = 0
        NEED_SPACES = 4
        NEED_NUMBERS = 5
        self._numbers = random.sample(range(1, self._MAX_NUMBER + 1), self._MAX_NUMBER_IN_CARD)

        for line in self._card:
            for _ in range(NEED_SPACES):
                line.append(' ')
            for _ in range(NEED_NUMBERS):
                line.append(self._numbers.pop())
        # [' ', ' ',' ',' ', 80, 50, 60, 70, 5]
        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)

    def has_number(self, number):
        for line in self._card:
            if number in line:
                return True
        return False

    def try_stoke_number(self, number):
        for index, line in enumerate(self._card):
            for num_index, number_in_card in enumerate(line):
                if number == number_in_card:
                    self._card[index][num_index] = '-'
                    self._numbers_stroked += 1
                    if self._numbers_stroked >= self._MAX_NUMBER_IN_CARD:
                        raise Exception(f'{self.player_type} победил!')
                    return True
        return False

    def __str__(self):
        MAX_FIELD_LEN = 3
        header = f'\n{self.player_type}:\n'
        body = '\n'
        for line in self._card:
            for field in line:
                body += str(field).ljust(MAX_FIELD_LEN)
            body += '\n'
        return header + body


class LotaGame:
    def __init__(self, human_player, computer_player):
        self.human_player = human_player
        self.computer_player = computer_player

    def start(self):
        random_game_number = [i + 1 for i in range(90)]
        random.shuffle(random_game_number)
        for num in random_game_number:
            print(self.human_player)
            print(self.computer_player)
            print(f'Сейчас счет: {self.human_player._numbers_stroked} - {self.computer_player._numbers_stroked}')
            print(f'Новый бочонок: {num}, (осталось {90 - (random_game_number.index(num)+1)})')
            decide = input('Зачеркнуть цифру? Y/N ')
            while True:
                if decide == 'Y' or decide == 'y':
                    if not self.human_player.has_number(num):
                        raise Exception(f'{self.human_player} Вы пытаетесь зачеркнуть номер которого у Вас нет!')
                    self.human_player.try_stoke_number(num)
                    break
                elif decide == 'N' or decide == 'n':
                    if self.human_player.has_number(num):
                        raise Exception(f'{self.human_player} Вы проглядели номер в карточке!')
                    break
            self.computer_player.try_stoke_number(num)


human_player = LotoCard('Игрок')

computer_player = LotoCard('Компьютер')

game = LotaGame(human_player, computer_player)
game.start()

# Иван, спасибо за занятия, Вы пока лучший преподаватель которого я встречал на GB.