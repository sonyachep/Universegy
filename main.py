import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Universegy(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('universegy.ui', self)
        self.stackedWidget.setCurrentIndex(0)
        self.login.clicked.connect(self.RunToPage2)
        self.registration.clicked.connect(self.RunToPage3)
        self.enterance_btn.clicked.connect(self.log_in)


    def RunToPage2(self):
        self.stackedWidget.setCurrentIndex(1)

    def RunToPage3(self):
        self.stackedWidget.setCurrentIndex(2)

    def log_in(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Universegy()
    ex.show()
    sys.exit(app.exec_())