import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QScrollArea, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from PySide6.QtCore import Qt, Slot
from file import FILE_TYPE
import row_widget


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.rows_widgets = {}
        self.selected_rows = []

        self.setWindowTitle("Таблица файлов")
        self.menu_layout = QHBoxLayout()

        self.setMinimumSize(1100, 500)

        self.file_type_combo_box = QComboBox()
        self.file_type_combo_box.addItems(FILE_TYPE._member_names_)
        self.create_button = QPushButton()
        self.create_button.setText('Создать')
        self.remove_button = QPushButton()
        self.remove_button.setText('Удалить')
        self.load_button = QPushButton()
        self.load_button.setText('Загрузить')
        self.save_button = QPushButton()
        self.save_button.setText('Сохранить')

        self.menu_layout.addWidget(self.file_type_combo_box)
        self.menu_layout.addWidget(self.create_button)
        self.menu_layout.addWidget(self.remove_button)
        self.menu_layout.addWidget(self.load_button)
        self.menu_layout.addWidget(self.save_button)
        self.menu_widget = QWidget()
        self.menu_widget.setLayout(self.menu_layout)

        self.table_layout = QVBoxLayout()
        self.table_widget = QWidget()
        self.table_widget.setLayout(self.table_layout)
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.table_widget)


        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()
        self.central_layout.addWidget(self.menu_widget)
        self.central_layout.addWidget(self.scroll)
        self.central_widget.setLayout(self.central_layout)

        self.type_label = QLabel()
        self.type_label.setText("<b>Тип файла</b>")
        self.type_label.setFixedSize(200, 50)


        self.name_label = QLabel()
        self.name_label.setText("<b>Название файла</b>")
        self.name_label.setFixedSize(200, 50)


        self.date_label = QLabel()
        self.date_label.setText("<b>Дата изменения</b>")
        self.date_label.setFixedSize(200, 50)

        self.size_label = QLabel()
        self.size_label.setText("<b>Размер</b>")
        self.size_label.setFixedSize(200, 50)

        self.title_table_layout = QHBoxLayout()
        self.title_table_layout.setAlignment(Qt.AlignLeft)

        self.title_table_layout.addWidget(self.type_label)
        self.title_table_layout.addWidget(self.name_label)
        self.title_table_layout.addWidget(self.date_label)
        self.title_table_layout.addWidget(self.size_label)
        self.title_table_widget = QWidget()
        self.title_table_widget.setFixedSize(1000, 50)
        self.title_table_widget.setLayout(self.title_table_layout)
        self.table_layout.addWidget(self.title_table_widget)

        self.setCentralWidget(self.central_widget)
    
    def get_create_file_type(self):
        return self.file_type_combo_box.currentText()
    
    def add_row(self, id, file_type, name, date, size):
        new_row = row_widget.RowWidget(id, file_type, name, date, size)
        new_row.selected.connect(self.select_row)
        self.rows_widgets[id] = new_row
        self.table_layout.addWidget(self.rows_widgets[id])

    @Slot(bool, int)
    def select_row(self, state, id):
        if state:
            self.selected_rows.append(id)
        else:
            self.selected_rows.remove(id)
    
    def remove_row(self, id):
        row = self.rows_widgets[id]
        row.deleteLater()
        if id in self.selected_rows:
            self.selected_rows.remove(id)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MainWindow()
    m.show()
    m.add_row(1, 'sdf', 'sdf', 'sdsf', 'sdf')
    sys.exit(app.exec())
