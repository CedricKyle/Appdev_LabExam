from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox 
from controller.belisario_login import BelisarioLoginUser

Form, Window = uic.loadUiType(r"ui/register_user.ui")

class BelisarioRegisterUser(Window):
    def __init__(self):
        super().__init__()
        self.ui = Form()
        self.ui.setupUi(self)
        self.ui.btnreg.clicked.connect(self.belisariocreateAcc)
        self.setWindowTitle("Register") 
        
    def belisariocreateAcc(self):
        try:
            self.belisarioemail = self.ui.reguser.text().strip()
            self.belisariopassword = self.ui.regpass.text().strip()
            self.belisariofname = self.ui.regfname.text().strip()
            self.belisariolname = self.ui.reglname.text().strip()
            ageTextbelisario = self.ui.regage.text().strip()
            
            if len(self.belisariopassword) < 8:
                raise ValueError("Length should be 8 characters long")
            
            if not self.belisarioemail or not self.belisariopassword or not self.belisariofname or not self.belisariolname or not ageTextbelisario: 
                raise ValueError("All fields are required")
            
            if not ageTextbelisario.isdigit():
                raise ValueError("Invalid age input")
            
            self.belisarioage = int(ageTextbelisario)
            if self.belisarioage < 18:
                raise ValueError("You need to be 18 to register")

            print("Account Created")
            print("First Name: ", self.belisariofname)
            print("Last Name: ", self.belisariolname)
            print("Age: ", self.belisarioage)
            print("Username: ", self.belisarioemail)
            print("Password: ", self.belisariopassword)
            self.window = BelisarioLoginUser(self.belisarioemail, self.belisariopassword, self.belisariofname, self.belisariolname, self.belisarioage)
            self.window.show()
            self.close()  
              
        except ValueError as ve:
            BelisarioMsg = QMessageBox()
            BelisarioMsg.setWindowTitle("Error")
            BelisarioMsg.setText(str(ve))
            BelisarioMsg.exec()
        
        except Exception as e:
            BelisarioMsg = QMessageBox()
            BelisarioMsg.setWindowTitle("Error")
            BelisarioMsg.setText(f"An unexpected error occurred: {str(e)}")
            BelisarioMsg.exec()
