import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('scheduler.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        self.listWidget.setSortingEnabled(True)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        result_string = ""
        result_string += self.calendarWidget.selectedDate().toString('yyyy-MM-dd') + ' '
        result_string += self.timeEdit.time().toString('hh:mm:ss') + ' '
        result_string += self.lineEdit.text()
        self.lineEdit.setText('')
        self.listWidget.addItem(result_string)
        # Имя элемента совпадает с objectName в QTDesigner


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())