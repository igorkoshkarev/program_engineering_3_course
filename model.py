from file import FILE_TYPE

class Model:

    ID = 0

    def __init__(self):
        self.files = {}

    def create(self, file_type: FILE_TYPE, *params):
        file = file_type.value.file_class(*params)
        self.files[self.ID] = file
        self.ID += 1
        return self.ID-1

    def remove(self, id):
        self.files.pop(id)
    
    def select_all(self):
        return self.files
            