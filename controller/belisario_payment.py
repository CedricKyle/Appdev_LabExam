from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

Form, Window = uic.loadUiType(r"ui/payment.ui")
MainWindow = QMainWindow

class Belisariopay(Window):
    def __init__(self, totalprice=""):
        super().__init__()
        self.ui = Form()
        self.ui.setupUi(self)   
        self.belisariototalprice = totalprice
        self.ui.pay_btn.clicked.connect(self.belisariobtnPay)
          

    def belisariopayment(self):
        self.belisariototal = str(self.belisariototalprice)
        self.ui.total.setText(self.belisariototal)
    
    def belisariobtnPay(self):
        try:
            cash_input = self.ui.payment.text()
            cash_amount = float(cash_input)
            total_amount = float(self.belisariototal)
            
            if cash_amount < total_amount:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Insufficient Funds")
                msg.exec()
            elif cash_amount >= total_amount:
                change = cash_amount - total_amount
                change_msg = QMessageBox()
                change_msg.setWindowTitle("Change")
                change_msg.setText(f"Your change is: {change}")
                change_msg.exec()
            else:
                invalid_input_msg = QMessageBox()
                invalid_input_msg.setWindowTitle("Error")
                invalid_input_msg.setText("Invalid Input")
                invalid_input_msg.exec()
        except ValueError:
            invalid_input_msg = QMessageBox()
            invalid_input_msg.setWindowTitle("Error")
            invalid_input_msg.setText("Invalid Input")
            invalid_input_msg.exec()
