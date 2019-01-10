from enum import Enum


class Runtime(object):
    def __init__(self, name, extention):
        self.name = name
        self.extention = extention


class Language(Enum):
    JAVA = Runtime('Java', 'java')
    PYTHON = Runtime('Python', 'py')

    @staticmethod
    def get_extension():
        return Runtime.extention

    @staticmethod
    def get_lang_name():
        return Runtime.name

    @staticmethod
    def values():
        return [r.value for r in Language]
