import random

from Rhymer import Rhymer
from enums.QuatrainType import QuatrainType
from util.TxtReader import TxtReader


class Generator:

    @staticmethod
    def generate_phrase(word1, word2):
        """For specified words phrase will be generated"""
        word_list = Generator.get_random_long_words(6)
        middle = int(word_list.__len__() / 2)
        first_line = ''
        second_line = ''
        for i in range(0, word_list.__len__()):
            if i < middle:
                first_line = first_line + " " + word_list[i]
            else:
                second_line = second_line + " " + word_list[i]
        # phrase = first_line + ' ' + word1 + "\n" + second_line + ' ' + word2
        phrase = '%s %s\n%s %s' % (first_line, word1, second_line, word2)
        print('Generated phrase:')
        print(phrase)
        return phrase

    @staticmethod
    def get_random_long_words(amount):
        """Method to return AMOUNT of words, tha are longer then 4 chars each"""
        random_indexes = Generator.get_random_nums(amount, 10000)
        word_list = TxtReader.read("../10k.txt")
        result = []
        for num in random_indexes:
            tmp = num
            while True:
                if word_list[tmp].__len__() > 4:
                    result.append(word_list[tmp].rstrip())
                    print('Will be used in phrase: ' + word_list[tmp])
                    break
                tmp += tmp
                if tmp >= 10000:
                    tmp = 0
        return result

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

    @staticmethod
    def generate_quatrain(q_type, word1, word2):
        line_length = 4

        rhyme1 = Rhymer.find_rhymes("../10k.txt", word1)[0]
        rhyme2 = Rhymer.find_rhymes("../10k.txt", word2)[0]

        line1 = ' '.join(Generator.get_random_long_words(line_length - 1))
        line2 = ' '.join(Generator.get_random_long_words(line_length - 1))
        line3 = ' '.join(Generator.get_random_long_words(line_length - 1))
        line4 = ' '.join(Generator.get_random_long_words(line_length - 1))

        if q_type == QuatrainType.ABAB:
            line1 = line1 + ' ' + word1
            line2 = line2 + ' ' + word2
            line3 = line3 + ' ' + rhyme1
            line4 = line4 + ' ' + rhyme2
            quatrain = [line1, line2, line3, line4]
        else:
            raise Exception('Unsupported quatrain type')
        print('=' * 6 + 'GENERATED QUATRAIN' + '=' * 6)
        for line in quatrain:
            print(line)
        print('=' * 30)
        return quatrain


# Generator.get_random_nums(6, 10000)
# Generator.generate_phrase('i', 'cry')
# Generator.get_random_long_words(6)
Generator.generate_quatrain(QuatrainType.ABAB, 'some', 'day')
