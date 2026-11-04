import copy

class Luhn:
    def __init__(self, card_num: str):
        self.card_num: str = card_num
        self.clean_card_num: str = self.card_num.replace(' ', '')
        self.reversed_list: list = [int(char) for char in self.clean_card_num[::-1] if char.isnumeric()]

    def valid(self):
        
        if not self.clean_card_num.isnumeric():
            return False
        if len(self.clean_card_num) < 2:
            return False
        
        copy_list: list = copy.deepcopy(self.reversed_list)
        for index, number in enumerate(self.reversed_list[1::2]):
            if number * 2 > 9:
                copy_list[2 * index + 1] = (number * 2) - 9
            else:
                copy_list[2 * index + 1] = number * 2
        
        return sum(copy_list) % 10 == 0


print(Luhn('059').valid())