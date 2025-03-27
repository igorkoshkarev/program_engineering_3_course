import file
import sys
from main_window import MainWindow
from model import Model
import create_file_window
from PySide6.QtWidgets import QApplication


def get_files(filename: str) -> list[file.File]:
    files = []
    with open(filename, 'r') as f:
        for i in f:
            info = i.split()
            print(info)
            if info[0] == 'pdf':
                files.append(file.PDFFile(*info[1:]))
            elif info[0] == 'png':
                files.append(file.PNGFile(*info[1:]))
            else:
                raise TypeError
    return files


class MainController:

    CREATE_WINDOW_CLASS = {file.FILE_TYPE.PDF.name: create_file_window.CreatePDFFileWindow, 
                           file.FILE_TYPE.PNG.name: create_file_window.CreatePNGFileWindow}

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow()
        self.main_window.create_button.clicked.connect(self.view_create_window)
        self.main_window.remove_button.clicked.connect(self.remove_elements)
        self.db = Model()
    
    def view_create_window(self):
        self.file_type = self.main_window.get_create_file_type()
        self.create_window = self.CREATE_WINDOW_CLASS[self.file_type]()
        self.create_window.create_button.clicked.connect(self.create)
        self.create_window.show()
    
    def create(self):
        file_type = self.create_window.get_file_type()
        parameters = self.create_window.get_parameters()
        id = self.db.create(file_type, **parameters)
        self.main_window.add_row(id, file_type.value.name, parameters['name'], parameters['date'], parameters['size'])
        self.create_window.close()
        del self.create_window

    def remove_elements(self):
        selected_rows = self.main_window.selected_rows.copy()
        for id in selected_rows:
            self.remove_element(id)

    def remove_element(self, id):
        self.main_window.remove_row(id)
        self.db.remove(id)
    
    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec())




if __name__ == '__main__':
    m = MainController()
    m.run()