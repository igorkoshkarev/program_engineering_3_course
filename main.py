import file
import sys
from main_window import MainWindow
from model import Model
import create_file_window
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QFileDialog
import csv


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
        self.main_window.load_button.clicked.connect(self.load)
        self.main_window.save_button.clicked.connect(self.save)
        self.db = Model()
    
    def view_create_window(self):
        self.file_type = self.main_window.get_create_file_type()
        self.create_window = self.CREATE_WINDOW_CLASS[self.file_type]()
        self.create_window.create_button.clicked.connect(self.create)
        self.create_window.show()
    
    def create(self):
        file_type = self.create_window.get_file_type()
        parameters = self.create_window.get_parameters()
        self.add_element(file_type, *parameters.values())
        self.create_window.close()
        del self.create_window

    def remove_elements(self):
        selected_rows = self.main_window.selected_rows.copy()
        for id in selected_rows:
            self.remove_element(id)

    def remove_element(self, id):
        self.main_window.remove_row(id)
        self.db.remove(id)
    
    def load(self):
        path = QFileDialog.getOpenFileName(filter='*.csv')
        path = path[0]
        if path.endswith('.csv'):
            with open(path, 'r', newline='') as f:
                reader = csv.reader(f, delimiter=' ')
                for file_element in reader:
                    file_type_name, parameters = file_element[0], file_element[1:]
                    file_type = file.FILE_TYPE.get_type_on_name(file_type_name)
                    self.add_element(file_type, *parameters)

    def save(self):
        path = QFileDialog.getSaveFileName(filter='*.csv')
        path = path[0]
        if path.endswith('.csv'):
            with open(path, 'w', newline='') as f:
                writer = csv.writer(f, delimiter=' ')
                for i in self.db.select_all().values():
                    writer.writerow(i.get_parameters())

    def add_element(self, file_type, name, date, size, *parameters):
        id = self.db.create(file_type, name, date, size, *parameters)
        self.main_window.add_row(id, file_type.value.name, name, date, size)

    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec())




if __name__ == '__main__':
    m = MainController()
    m.run()