import sys
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow, QSpinBox, QScrollArea, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from file import FILE_TYPE

class CreateFileWindow(QMainWindow):

    TYPE_WIDGET = {str: QLineEdit, int: QSpinBox}

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Создать файл")
        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()

        self.setMinimumSize(300, 300)

        self.file_type = QComboBox()
        self.file_type.addItems(FILE_TYPE.get_all_string_types())

        self.central_layout.addWidget(QLabel("Тип файла: "))
        self.central_layout.addWidget(self.file_type)

        self.parameters = {}

        for i, v in {'name': str, 'date': int, 'size': int}.items():
            l = QLabel()
            l.setText(i)
            w = self.TYPE_WIDGET[v]()
            self.parameters[i] = w

            self.central_layout.addWidget(l)
            self.central_layout.addWidget(w)

        self.create_button = QPushButton()
        self.create_button.setText('Создать')

        self.central_layout.addWidget(self.create_button)
        self.central_widget.setLayout(self.central_layout)

        self.setCentralWidget(self.central_widget)
    
    def get_file_type(self):
        return FILE_TYPE.get_type_on_name(self.file_type.currentText())
    
    def get_parameters_dict(self):
        parameters = {}
        for i, v in self.parameters.items():
            if isinstance(v, self.TYPE_WIDGET[str]):
                parameters[i] = v.text()
            elif isinstance(v, self.TYPE_WIDGET[int]):
                parameters[i] = v.value()
        return parameters
    
    def get_parameters_list(self):
        parameters = []
        for i, v in self.parameters.items():
            if isinstance(v, self.TYPE_WIDGET[str]):
                parameters.append(v.text())
            elif isinstance(v, self.TYPE_WIDGET[int]):
                parameters.append(v.value())
        return parameters
