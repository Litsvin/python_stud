from interface.IReader import IReader


class TxtReader(IReader):

    @staticmethod
    def read(path_to_file):
        print('Will open ' + path_to_file)
        file = open(path_to_file, "r")
        str_list = []
        while True:
            line = file.readline()
            str_list.append(line)
            if not line:
                print('End of file')
                break
        return str_list


# print(TxtReader.read("../10k.txt"))
