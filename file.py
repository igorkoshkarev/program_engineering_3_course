from abc import ABC, abstractmethod

class File(ABC):
    def __init__(self, name: str, date: str, size: int):
        self.name = name
        self.date = date
        self.size = size
    
    @abstractmethod
    def print_all(self):
        pass

class PDFFile(File):
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


class PNGFile(File):
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
        print('pages: ', self.width)
        print('pages: ', self.height)

