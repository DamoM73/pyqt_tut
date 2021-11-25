from calc2_ui import *

def signals(self):
    self.buttonCalc.clicked.connect(self.calc)
    
def calc(self):
    a = self.lineEdit1.text()
    b = self.lineEdit2.text()
    operator = self.comboBox.currentText()
    try:
        c = eval(a + operator + b)
        self.lineEdit3.setText(str(c))
    except:
        QtWidgets.QMessageBox.critical(MainWindow, "Error", "Invalid inputs!", QtWidgets.QMessageBox.Ok)
        
Ui_MainWindow.signals = signals
Ui_MainWindow.calc = calc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    MainWindow.show()
    sys.exit(app.exec())