from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import sqlite3
from mian import Ui_MainWindow as main_interface

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_interface()
        self.ui.setupUi(self)

        self.connection = sqlite3.connect('my_database.db')
        self.cursor = self.connection.cursor()
        
        self.createtab()
        self.read_users()
        
        self.ui.pushButton.clicked.connect(self.dob)
        self.ui.pushButton2.clicked.connect(self.delll)
        self.ui.pushButton3.clicked.connect(self.izm)

    def createtab(self): #создание
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER)
        ''')
        
        self.cursor.execute('SELECT COUNT(*) FROM Users')
        count = self.cursor.fetchone()[0]
        if count == 0:
            self.cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', 
                   ('newuser', 'newuser@example.com', 28))
            self.cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', 
                   ('user1', 'newuser1@example.com', 25))
            self.cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', 
                   ('newuser2', 'newuser@example.com', 27))
            self.cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', 
                   ('user3', 'newuser1@example.com', 26))
            self.connection.commit()

    def read_users(self): #вывод
        self.cursor.execute('SELECT * FROM Users')
        self.usersdata = self.cursor.fetchall()
        self.ui.tableWidget.setRowCount(len(self.usersdata))
        self.ui.tableWidget.setColumnCount(len(self.usersdata[0]))

        for i, row in enumerate(self.usersdata):
            for j, value in enumerate(row):
                self.ui.tableWidget.setItem(i,j,QTableWidgetItem(str(value)))

    def dob(self): #добавление
        self.cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', 
           ('', '', ''))
        self.connection.commit()
        self.read_users()

    def delll(self): #удалене
        current_row = self.ui.tableWidget.currentRow()
        if current_row >= 0:
            user_id = self.ui.tableWidget.item(current_row, 0).text()
            self.cursor.execute('DELETE FROM Users WHERE id = ?', (user_id,))
            self.connection.commit()
            self.read_users()
            
    def izm(self): #изменение
        current_row = self.ui.tableWidget.currentRow()
        if current_row >= 0:
            user_id = self.ui.tableWidget.item(current_row, 0).text()
            username = self.ui.tableWidget.item(current_row, 1).text()
            email = self.ui.tableWidget.item(current_row, 2).text()
            age = self.ui.tableWidget.item(current_row, 3).text()
            
            self.cursor.execute('UPDATE Users SET username=?, email=?, age=? WHERE id=?',
                           (username, email, age, user_id))
            self.connection.commit()
            self.read_users()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_form = main_window()
    main_form.show()
    sys.exit(app.exec_())

