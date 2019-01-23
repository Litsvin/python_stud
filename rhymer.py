import pronouncing

from util.reader import Reader


class Rhymer:

    @staticmethod
    def is_rhyme(word1, word2):
        rhyme = word1.rstrip() in pronouncing.rhymes(word2.rstrip())
        return rhyme

    @staticmethod
    def get_rhymes(word):
        """This method will provide you rhymes taken from pronouncing's resources"""
        return pronouncing.rhymes(word)

    @staticmethod
    def find_rhymes(file_path, word):
        """Method to find rhymes in file"""
        file = TxtReader.read(file_path)
        rhyme_list = []
        counter = 0
        for line in file:
            if Rhymer.is_rhyme(line, word):
                rhyme_list.append(line)
            if not line:
                print('End of file')
                break
            counter += 1
            if counter % 1000 == 0:
                print('Number of processed lines: ' + str(counter))
        if rhyme_list.__len__() == 0:
            raise Exception('Can\'t find a rhyme for "%s"' % word)
        print('List of rhymes to "%s": ' % word)
        for rhyme in rhyme_list:
            print(rhyme.rstrip())
        return rhyme_list


# print(Rhymer.get_rhymes('nod'))
# print(Rhymer.is_rhyme('i', 'cry'))
# Rhymer.find_rhymes("10k.txt", "cry")
