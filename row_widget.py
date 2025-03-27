from PySide6.QtWidgets import QCheckBox, QLabel, QHBoxLayout, QWidget
from PySide6 import QtCore


class RowWidget(QWidget):

    selected = QtCore.Signal(bool, int)

    def __init__(self, id, file_type, name, date, size):

        super().__init__()

        self.setFixedSize(1000, 50)
        self.id = id

        self.type_label = QLabel()
        self.type_label.setFixedSize(200, 50)
        self.type_label.setText(file_type)

        self.name_label = QLabel()
        self.name_label.setFixedSize(200, 50)
        self.name_label.setText(name)

        self.date_label = QLabel()
        self.date_label.setFixedSize(200, 50)
        self.date_label.setText(date)

        self.size_label = QLabel()
        self.size_label.setFixedSize(200, 50)
        self.size_label.setText(str(size))

        self.check_box = QCheckBox()
        self.check_box.stateChanged.connect(self.select_row)

        self.central_widget = QWidget()
        self.central_layout = QHBoxLayout()
        self.central_layout.addWidget(self.type_label)
        self.central_layout.addWidget(self.name_label)
        self.central_layout.addWidget(self.date_label)
        self.central_layout.addWidget(self.size_label)
        self.central_layout.addWidget(self.check_box)
        self.setLayout(self.central_layout)
    
    def select_row(self, state):
        if state == 2:
            self.selected.emit(True, self.id)
        else:
            self.selected.emit(False, self.id)
