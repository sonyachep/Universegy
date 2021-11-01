import sqlite3

DATABASE = 'Universegy.db'


class Database:
    def __init__(self):
        self.connect = sqlite3.connect(DATABASE)
        self.cur = self.connect.cursor()

    def registration(self, name, surname, student_class, login, password, is_teacher):
        self.add_user(name, surname, student_class)
        self.connect.commit()
        user_id = self.cur.execute('''SELECT id FROM users WHERE name = ?''', (name,)).fetchall()[0][0]
        self.add_user_data(user_id, login, password, is_teacher)
        self.connect.commit()

    def log_in(self, login, password):
        all_users = self.cur.execute('''SELECT login, password FROM users_data''').fetchall()
        print(all_users)
        return (login, password) in all_users

    def add_user(self, name, surname, student_class):
        self.cur.execute('''INSERT INTO users (name, surname, class)
                        VALUES(?, ?, ?)''', (name, surname, student_class))

    def add_user_data(self, user_id, login, password, is_teacher):
        self.cur.execute('''INSERT INTO users_data (user_id, login, password, rights)
                                        VALUES(?, ?, ?, ?)''', (user_id, login, password, is_teacher))


class Users:
    def __init__(self):
        self.db = Database()

    def get_all(self):
        return self.db.cur.execute('''SELECT * FROM users''').fetchall()

    def get_user(self, id):
        return self.db.cur.execute('''SELECT * FROM users WHERE id = ?''', (id,)).fetchall()[0]


class Users_data:
    def __init__(self):
        self.db = Database()

    def get_all(self):
        data = self.db.cur.execute('''SELECT * FROM users_data''').fetchall()
        new_data = []
        for elem in data:
            id, login, password, rights = elem
            new_data.append((id, login, password, bool(rights)))
        return new_data

    def get_user_data(self, user_id):
        id, login, password, rights = self.db.cur.execute('''SELECT * FROM users_data 
        WHERE user_id = ?''', (user_id,)).fetchall()[0]
        return id, login, password, bool(rights)


class Tasks:
    def __init__(self):
        self.db = Database()

    def get_all(self):
        return self.db.cur.execute('''SELECT * FROM tasks''').fetchall()

    def get_task(self, task_id):
        id, task_text, answer, block = self.db.cur.execute('''SELECT * FROM tasks 
        WHERE task_id = ?''', (task_id,)).fetchall()[0]
        return id, task_text, answer, block

    def get_block(self, block):
        data = self.db.cur.execute('''SELECT * FROM tasks WHERE block = ?''', (block,)).fetchall()
        new_data = []
        for elem in data:
            id, task_text, answer, block = elem
            new_data.append((id, task_text, answer))
        return new_data


task = Tasks()
print(task.get_all())
print(task.get_task(2))
print(task.get_block(1))

# user_data = Users_data()
# print(user_data.get_all())
#
# print(user_data.get_user_data(1))
# print(user_data.get_user_data(2))
