import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)  # Загружаем дизайн
        self.clear()
        self.btn0.clicked.connect(self.add_digit)
        self.btn1.clicked.connect(self.add_digit)
        self.btn2.clicked.connect(self.add_digit)
        self.btn3.clicked.connect(self.add_digit)
        self.btn4.clicked.connect(self.add_digit)
        self.btn5.clicked.connect(self.add_digit)
        self.btn6.clicked.connect(self.add_digit)
        self.btn7.clicked.connect(self.add_digit)
        self.btn8.clicked.connect(self.add_digit)
        self.btn9.clicked.connect(self.add_digit)

        self.btn_clear.clicked.connect(self.clear)
        self.btn_div.clicked.connect(self.div)
        self.btn_dot.clicked.connect(self.dot)
        self.btn_eq.clicked.connect(self.eq)
        self.btn_fact.clicked.connect(self.fact)
        self.btn_minus.clicked.connect(self.minus)
        self.btn_mult.clicked.connect(self.mult)
        self.btn_plus.clicked.connect(self.plus)
        self.btn_pow.clicked.connect(self.pow)
        self.btn_sqrt.clicked.connect(self.sqrt)

    def add_digit(self):
        if self.floatPart == '':
           if self.intPart == '0' or self.intPart == '':
               self.intPart = self.sender().text()
           else:
               self.intPart += self.sender().text()
           self.table.display(self.intPart)
        else:
            self.floatPart += self.sender().text()
            self.table.display(f'{self.intPart}{self.floatPart}')

    def clear(self):
        self.intPart = ''
        self.floatPart = ''
        self.firstNumber = 0
        self.operation = False
        self.table.display("0")

    def div(self):
        if self.intPart != '':
            self.calculate()
        self.operation = '/'


    def dot(self):
        if self.floatPart == '':
            if self.intPart=='':
                self.intPart = '0'
            self.floatPart = '.'
            self.table.display(f'{self.intPart}{self.floatPart}')

    def eq(self):
        if not self.operation:
            return
        self.calculate()
        self.operation = False

    def calculate(self):
        secondNumber = float(self.intPart + self.floatPart)
        if self.operation == '/':
            if secondNumber == 0:
                self.table.display('ERR')
                return
            result = self.firstNumber / secondNumber
        if self.operation == '+':
            result = self.firstNumber + secondNumber
        if self.operation == '*':
            result = self.firstNumber * secondNumber
        if not self.operation:
            result = secondNumber


        self.table.display(result)
        self.firstNumber = result
        self.intPart = ''
        self.floatPart = ''



    def fact(self):
        pass

    def minus(self):
        pass

    def mult(self):
        if self.intPart != '':
            self.calculate()
        self.operation = '*'

    def plus(self):
        if self.intPart != '':
            self.calculate()
        self.operation = '+'

    def pow(self):
        pass

    def sqrt(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
