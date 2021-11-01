import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from database import *


class Universegy(QMainWindow):
    def __init__(self):
        self.db = Database()
        self.tasks = Tasks()

        super().__init__()
        uic.loadUi('universegy.ui', self)
        self.logged = False

        self.answers = {1:0,
                        2:0,
                        3:0,
                        4:0,
                        5:0,
                        6:0,
                        7:0,
                        8:0,
                        9:0,
                        10:0}
                        # 11:0,
                        # 12:0,
                        # 13:0,
                        # 14:0,
                        # 15:0,
                        # 16:0,
                        # 17:0,
                        # 18:0,
                        # 19:0,
                        # 20:0}
        self.task_number = 0

        self.run_to_page1()
        self.set_user.clicked.connect(self.run_to_page1)
        self.login.clicked.connect(self.run_to_page2)
        self.registration.clicked.connect(self.run_to_page3)
        self.integer_round.clicked.connect(self.run_to_page5)
        self.end_test.clicked.connect(self.run_to_page6)

        self.enterance.clicked.connect(self.log_in)
        self.enterance.clicked.connect(self.run_to_page4)

        self.set_user.clicked.connect(self.registrate)

        self.block1_task_choices.currentTextChanged.connect(self.show_block1_task)
        self.write_answer.clicked.connect(self.write_current_answer)
        self.end_test.clicked.connect(self.check_answer)

    def run_to_page1(self):
        self.stackedWidget.setCurrentIndex(0)

    def run_to_page2(self):
        self.stackedWidget.setCurrentIndex(1)

    def run_to_page3(self):
        self.stackedWidget.setCurrentIndex(2)

    def run_to_page4(self):
        if self.logged:
            self.stackedWidget.setCurrentIndex(3)

    def run_to_page5(self):
        self.stackedWidget.setCurrentIndex(4)

    def run_to_page6(self):
        self.stackedWidget.setCurrentIndex(5)

    def log_in(self):
        login = self.login_in_edit.text()
        password = self.password_in_edit.text()
        self.logged = self.db.log_in(login, password)

    def registrate(self):
        name = self.name_edit.text()
        surname = self.surname_edit.text()
        student_class = self.class_choice.currentText()
        login = self.login_edit.text()
        password = self.password_edit.text()
        is_teacher = int(self.is_teacher.isChecked())
        self.db.registration(name, surname, student_class, login, password, is_teacher)

    def show_block1_task(self):
        self.task_number = int(self.sender().currentText())
        tasks = self.tasks.get_block(1)
        for elem in tasks:
            id, text, answer = elem
            if id == self.task_number:
                self.task_view.setText(text)
                break

    def write_current_answer(self):
        answer = self.answer_edit.text()
        self.answers[self.task_number] = answer
        self.answer_edit.setText('')

    def check_answer(self):
        score = ''
        total = 0
        for id, student_answer in self.answers.items():
            id, task_text, right_answer, block = self.tasks.get_task(id)

            if student_answer == str(right_answer):
                if len(f'{id}: +') < 5:
                    score += f'{id}:  +\n'
                else:
                    score += f'{id}: +\n'
                total += 1
            else:
                if len(f'{id}: -') < 5:
                    score += f'{id}:   -\n'
                else:
                    score += f'{id}: -\n'

        result = f'результат: {total}/{len(self.answers.keys())}'
        self.result_view.setText(result)
        self.answer_view.setText(score)



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Universegy()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
