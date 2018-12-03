import random
from util.TxtReader import TxtReader


class Generator:

    @staticmethod
    def generate_phrase(word1, word2):
        phrase_len = 8
        random_indexes = Generator.get_random_nums(phrase_len - 2, 10000)
        file = TxtReader.read("../10k.txt")


    @staticmethod
    def get_random_nums(amount, higher_limit):
        random_nums = []
        next_random = False
        for i in range(0, amount):
            if random_nums.__contains__(next_random):
                i -= i
                continue
            random_nums.append(random.randint(0, higher_limit))
        print(random_nums)
        return random_nums

# Generator.get_random_nums(6, 10000)
