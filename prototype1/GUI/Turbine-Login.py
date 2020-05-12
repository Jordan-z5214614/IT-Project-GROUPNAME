import PyQt5
from PyQt5 import QtWidgets, uic
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import sqlite3
import sys



class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('TurbineLogin.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'loginButton')
        self.button.clicked.connect(self.loginProcess)

        self.button = self.findChild(QtWidgets.QPushButton, 'exitButton')
        self.button.clicked.connect(self.exitProcess)



        self.show()

    def loginProcess(self):
        username = str(self.username.toPlainText())
        password = str(self.password.toPlainText())

        # You can create a new database by changing the name within the quotes
        conn = sqlite3.connect('login.db')

        # The database will be saved in the location where your 'py' file is saved
        c = conn.cursor()
        
        hashP = hashlib.md5(password.encode('utf-8')).hexdigest()
        c.execute("SELECT * FROM LOGIN WHERE username='"+username+"' and password='"+hashP+"'")

        if c.fetchone():
            print("Found!")

        else:
            _init_(self)
        
        print(username)
        print(password)

    def exitProcess(self):
        self.destroy()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
