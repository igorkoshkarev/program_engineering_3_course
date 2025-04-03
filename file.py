from abc import ABC, abstractmethod
from collections import namedtuple
import enum

class File(ABC):
    PARAMETERS = {'name': str, 'date': str, 'size': int}
    UNIQUE_PARAMETERS = {}

    def __init__(self, name: str, date: str, size: int):
        self.name = name
        self.date = date
        self.size = size
    
    @abstractmethod
    def print_all(self):
        pass

    @abstractmethod
    def get_parameters(self):
        pass

class PDFFile(File):
    UNIQUE_PARAMETERS = {'pages': int}

    def __init__(self, name, date, size, pages):
        super().__init__(name, date, size)
        self.type = "pdf"
        self.pages = pages
    
    def print_all(self):
        print('type: ', self.type)
        print('name: ', self.name)
        print('date: ', self.date)
        print('size: ', self.size)
        print('pages: ', self.pages)
    
    def get_parameters(self):
        return [self.type, self.name, self.date, self.size, self.pages]


class PNGFile(File):
    UNIQUE_PARAMETERS = {'width': int, 'height': int}

    def __init__(self, name, date, size, width, height):
        super().__init__(name, date, size)
        self.type = 'png'
        self.width = width
        self.height = height
    
    def print_all(self):
        print('type: ', self.type)
        print('name: ', self.name)
        print('date: ', self.date)
        print('size: ', self.size)
        print('width: ', self.width)
        print('height: ', self.height)
    
    def get_parameters(self):
        return [self.type, self.name, self.date, self.size, self.width, self.height]
    


file_type = namedtuple('FileType', ['name', 'file_class'])

class FILE_TYPE(enum.Enum):
    PDF = file_type('pdf', PDFFile)
    PNG = file_type('png', PNGFile)

    @staticmethod
    def get_type_on_name(name: str) -> file_type:
        for i in FILE_TYPE._member_map_.values():
            if i.value.name == name:
                return i
        else:
            raise AssertionError('Такого типа файла не существует')
