import sys
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow, QSpinBox, QScrollArea, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from PySide6.QtCore import Qt
from file import FILE_TYPE

class CreateFileWindow(QMainWindow):

    TYPE: FILE_TYPE

    TYPE_WIDGET = {str: QLineEdit, int: QSpinBox}

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Создать файл")
        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()

        self.setMinimumSize(300, 300)

        self.parameters = {}

        for i, v in self.TYPE.value.file_class.PARAMETERS.items():
            l = QLabel()
            l.setText(i)
            w = self.TYPE_WIDGET[v]()
            self.parameters[i] = w

            self.central_layout.addWidget(l)
            self.central_layout.addWidget(w)

        for i, v in self.TYPE.value.file_class.UNIQUE_PARAMETERS.items():
            l = QLabel()
            l.setText(i)
            w = self.TYPE_WIDGET[v]()
            self.parameters[i] = w

            self.central_layout.addWidget(l)
            self.central_layout.addWidget(self.parameters[i])

        self.create_button = QPushButton()
        self.create_button.setText('Создать')

        self.central_layout.addWidget(self.create_button)
        self.central_widget.setLayout(self.central_layout)

        self.setCentralWidget(self.central_widget)
    
    def get_file_type(self):
        return self.TYPE
    
    def get_parameters(self):
        parameters = {}
        for i, v in self.parameters.items():
            if isinstance(v, self.TYPE_WIDGET[str]):
                parameters[i] = v.text()
            elif isinstance(v, self.TYPE_WIDGET[int]):
                parameters[i] = v.value()
        return parameters

class CreatePDFFileWindow(CreateFileWindow):

    TYPE = FILE_TYPE.PDF

class CreatePNGFileWindow(CreateFileWindow):

    TYPE = FILE_TYPE.PNG


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = CreatePNGFileWindow()
    m.show()
    sys.exit(app.exec())