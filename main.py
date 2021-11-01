import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from database import *


class Universegy(QMainWindow):
    def __init__(self):
        self.db = Database()
        super().__init__()
        uic.loadUi('universegy.ui', self)
        self.stackedWidget.setCurrentIndex(0)
        self.login.clicked.connect(self.RunToPage2)
        self.registration.clicked.connect(self.RunToPage3)
        self.enterance_btn.clicked.connect(self.log_in)
        self.set_user.clicked.connect(self.registrate)


    def RunToPage2(self):
        self.stackedWidget.setCurrentIndex(1)

    def RunToPage3(self):
        self.stackedWidget.setCurrentIndex(2)

    def log_in(self):
        pass

    def registrate(self):
        name = self.name_edit.text()
        surname = self.surname_edit.text()
        student_class = self.class_choice.currentText()
        login = self.login_edit.text()
        password = self.password_edit.text()
        is_teacher = int(self.is_teacher.isChecked())
        self.db.registration(name, surname, student_class, login, password, is_teacher)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Universegy()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
