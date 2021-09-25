import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 150)
        self.setWindowTitle('Миникалькулятор - by morozov makar')

        self.label = QLabel(self)
        self.label.setText("Первое число(целое):")
        self.label.move(20, 20)

        self.label = QLabel(self)
        self.label.setText("Второе число(целое):")
        self.label.move(20, 80)

        self.btn = QPushButton('->', self)
        self.btn.move(190, 70)
        self.btn.clicked.connect(self.swith)

        self.first_input = QLineEdit(self)
        self.first_input.move(20, 40)

        self.second_input = QLineEdit(self)
        self.second_input.move(20, 100)

        self.summ_lbl = QLabel(self)
        self.summ_lbl.setText("Сумма")
        self.summ_lbl.move(300, 20)

        self.summ = QLCDNumber(self)
        self.summ.move(420, 20)

        self.ras_lbl = QLabel(self)
        self.ras_lbl.setText("Разность")
        self.ras_lbl.move(300, 50)

        self.raz = QLCDNumber(self)
        self.raz.move(420, 50)

        self.chas_lbl = QLabel(self)
        self.chas_lbl.setText("Частное")
        self.chas_lbl.move(300, 80)

        self.chast = QLCDNumber(self)
        self.chast.move(420, 80)

        self.prois_lbl = QLabel(self)
        self.prois_lbl.setText("Произведение")
        self.prois_lbl.move(300, 110)

        self.proiz = QLCDNumber(self)
        self.proiz.move(420, 110)

    def swith(self):
        x, y = list(map(int, [self.first_input.text(), self.second_input.text()]))
        self.summ.display(x + y)
        self.raz.display(x - y)
        self.proiz.display(x * y)
        if y != 0:
            self.chast.display(x / y)
        else:
            self.chast.display("Error")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
