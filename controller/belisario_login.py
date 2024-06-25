from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from controller.belisario_homepage import BelisarioHomepage

Form, Window = uic.loadUiType(r"ui/login.ui")
MainWindow = QMainWindow

class BelisarioLoginUser(Window):
    def __init__(self, user="", password="", fname="", lname="", age=""):
        super().__init__()
        self.ui = Form()
        self.ui.setupUi(self)   
        self.belisariouser = user
        self.belisariopassword = password
        self.belisariofname = fname
        self.belisariolname = lname
        self.belisarioage = age
        self.ui.btnlogin.clicked.connect(self.belisariologin)
        # self.ui.btnregister.clicked.connect(self.belisarioregister)
        self.setWindowTitle("Login") 
        
    def belisarioregister(self):
        from controller.belisario_register import BelisarioRegisterUser
        self.window = BelisarioRegisterUser()
        self.window.show()
        self.close()    
        
    def belisariologin(self):
        belisariologemail = self.ui.loguser.text()
        belisariologpass = self.ui.logpass.text()
        
        if belisariologemail == self.belisariouser and belisariologpass == self.belisariopassword:
            self.window = BelisarioHomepage(self.belisariofname, self.belisariolname, self.belisarioage, self.belisariouser, self.belisariopassword)
            self.window.show()
            self.window.belisariohp()
            self.close()   
        else:
            belisarioMsg = QMessageBox()
            belisarioMsg.setWindowTitle("Error")
            belisarioMsg.setText("Invalid Input")
            belisarioMsg.exec()
