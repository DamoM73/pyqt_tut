<<<<<<< HEAD
from interface import Ui_Dialog

ui = Ui_Dialog()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
=======
import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from calc_ui import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        
    def connectSignalsSlots(self):
        self.
>>>>>>> 77c5b6c67a149750289bfa7fbd9edaedf37335a3
