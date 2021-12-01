import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Ui_calc import Ui_MainWindow


class MainWindow:
    def __init__(self):

        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.signals()
        
    def signals(self):
        # percent
        self.ui.clear_btn.clicked.connect(self.clear)
        # backspace
        self.ui.divide_btn.clicked.connect(lambda: self.button_clicked("/"))
        self.ui.seven_btn.clicked.connect(lambda: self.button_clicked("7"))
        self.ui.eight__btn.clicked.connect(lambda: self.button_clicked("8"))
        self.ui.nine_btn.clicked.connect(lambda: self.button_clicked("9"))
        self.ui.multiply_btn.clicked.connect(lambda: self.button_clicked("*"))
        self.ui.four_btn.clicked.connect(lambda: self.button_clicked("4"))
        self.ui.five_btn.clicked.connect(lambda: self.button_clicked("5"))
        self.ui.six_btn.clicked.connect(lambda: self.button_clicked("6"))
        self.ui.minus_btn.clicked.connect(lambda: self.button_clicked("-"))
        self.ui.one_btn.clicked.connect(lambda: self.button_clicked("1"))
        self.ui.two_btn.clicked.connect(lambda: self.button_clicked("2"))
        self.ui.three_btn.clicked.connect(lambda: self.button_clicked("3"))
        self.ui.plus_btn.clicked.connect(lambda: self.button_clicked("+"))
        # plus / minus
        self.ui.zero_btn.clicked.connect(lambda: self.button_clicked("0"))
        self.ui.decimal_btn.clicked.connect(lambda: self.button_clicked("."))
        # equals

    def show(self):
        self.main_win.show()

    # slots
        
    def button_clicked(self,val):
        curr_output = self.ui.output_lb.text()
        if curr_output == "0":
            curr_output = ""
        new_output = curr_output + val
        self.ui.output_lb.setText(new_output)
        
    def clear(self):
        self.ui.output_lb.setText("0")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())