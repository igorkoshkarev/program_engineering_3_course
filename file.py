from abc import ABC, abstractmethod
from collections import namedtuple
import enum

class File(ABC):
    PARAMETERS = {'name': str, 'date': str, 'size': int}

    def __init__(self, name: str, date: str, size: int):
        self.type = None
        self.name = name
        self.date = date
        self.size = size
    
    def print_all(self):
        print('type: ', self.type)
        print('name: ', self.name)
        print('date: ', self.date)
        print('size: ', self.size)

    def get_parameters(self):
        return [self.type, self.name, self.date, self.size]
    
    def get_parameters_dict(self):
        return {'type': self.type, 'name': self.name, 'date': self.date, 'size': self.size}

class PDFFile(File):
    def __init__(self, name, date, size):
        super().__init__(name, date, size)
        self.type = "pdf"


class PNGFile(File):
    def __init__(self, name, date, size):
        super().__init__(name, date, size)
        self.type = 'png'


file_type = namedtuple('FileType', ['name', 'file_class'])

class FILE_TYPE(enum.Enum):
    PDF = file_type('pdf', PDFFile)
    PNG = file_type('png', PNGFile)

    @staticmethod
    def get_all_string_types() -> str:
        a = []
        for i in FILE_TYPE:
            a.append(i.value.name)
        return a

    @staticmethod
    def get_type_on_name(name: str) -> file_type:
        for i in FILE_TYPE._member_map_.values():
            if i.value.name == name:
                return i
        else:
            raise AssertionError('Такого типа файла не существует')
