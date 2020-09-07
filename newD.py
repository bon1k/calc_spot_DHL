from FormDHL import *

def summa1(self):
    self.pushResult.clicked.connect(self.result1)


def result1(self):
    stand_tarif = self.lineEdit.text()
    stand_tarif = int(stand_tarif)
    discount = self.lineEdit_2.text()
    discount = int(discount)
    ves = self.lineEdit_3.text()
    ves = int(ves)
    rate_per = self.lineEdit_4.text()
    rate_per = int(rate_per)
    rez1 = stand_tarif - stand_tarif / 100 * discount
    rez1 = int(round(rez1, -1))
    rez2 = rez1 / ves
    rez2 = int(round(rez2 + 5, -1))
    if rez2 < rate_per:
        self.lineEdit_5.setText('Rate per превышен' + str(rate_per))
    else:
        rez3 = rez2 * ves
        self.lineEdit_5.setText('сумма для АДР  ' + str(rez3))


Ui_MainWindow.summa1 = summa1
Ui_MainWindow.result1 = result1


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.summa1()
    MainWindow.show()
    sys.exit(app.exec_())

