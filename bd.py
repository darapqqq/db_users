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

    def createtab(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER)
        ''')
        
        self.cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', 
               ('newuser', 'newuser@example.com', 28))
        self.cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', 
               ('user1', 'newuser1@example.com', 25))
        self.connection.commit()

    def read_users(self):
        self.cursor.execute('SELECT * FROM Users')
        self.usersdata = self.cursor.fetchall()
        self.ui.tableWidget.setRowCount(len(self.usersdata))
        self.ui.tableWidget.setColumnCount(len(self.usersdata[0]))

        for i, row in enumerate(self.usersdata):
            for j, value in enumerate(row):
                self.ui.tableWidget.setItem(i,j,QTableWidgetItem(str(value)))

    def dob(self):
        self.cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', 
               ('newuser', 'newuser@example.com', 28))
        self.read_users()


    def delll(self):
        row = self.ui.tableWidget.currentRow()
        self.cursor.execute('DELETE FROM Users WHERE id = ?', (row,))
        self.ui.tableWidget.clearSelection()
        self.ui.tableWidget.selectRow(self.ui.tableWidget.rowCount() - 1)
        if row == -1:
            row = self.ui.tableWidget.rowCount() - 1
        self.ui.tableWidget.removeRow(row)
        
        
    def izm(self):
        row = self.ui.tableWidget.currentRow()
        cursor.execute('UPDATE Users SET age = ? WHERE id = ?', (29, row))

    def close(self):
        self.cursor.close()
        self.connection.close()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_form = main_window()
    main_form.show()
    sys.exit(app.exec_())

