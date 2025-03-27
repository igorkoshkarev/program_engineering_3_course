import file
from main_window import MainWindow
from model import Model

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

    def __init__(self):
        self.main_window = MainWindow()
        self.main_window.create_button.clicked.connect(self.view_create_window)
        self.main_window.remove_button.clicked.connect(self.remove)
        self.db = Model()
    
    def view_create_window(self):
        pass

    def remove(self):
        pass



if __name__ == '__main__':
    files = get_files('files.txt')
    for f in files:
        f.print_all()
        print()
