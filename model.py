from file import file_type
import file

class Model:

    def __init__(self):
        self.ID = 0
        self.files = {}

    def create(self, file_type: file_type, *params, **kparams):
        assert not(params and kparams), "Можно использовать только один способ передачи аргументов"
        if params:
            file = file_type.value.file_class(*params)
        else:
            file = file_type.value.file_class(**kparams)
        self.files[self.ID] = file
        self.ID += 1
        return self.ID-1
    
    def select_by_id(self, id: int) -> file.File:
        assert self.files.get(id, 0) != 0, "Записи с таким id не существует"
        return self.files[id]

    def remove(self, id: int):
        if id in self.files:
            self.files.pop(id)
    
    def select_all(self) -> dict[int, file.File]:
        return self.files
            