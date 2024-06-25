from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from controller.belisario_payment import Belisariopay


Form, Window = uic.loadUiType(r"ui/homepage.ui")
MainWindow = QMainWindow

class BelisarioHomepage(Window):
    def __init__(self, fname="", lname="", age="", user="", password=""):
        super().__init__()
        self.ui = Form()
        self.ui.setupUi(self)
        self.belisariofname = fname
        self.belisariolname = lname
        self.belisarioage = age
        self.belisarioemail = user
        self.belisariopassword = password
        self.setWindowTitle("Homepage")
        self.belisariototalprice = 0
        self.ui.item1.clicked.connect(self.belisarioitem1)
        self.ui.item2.clicked.connect(self.belisarioitem2)
        self.ui.item3.clicked.connect(self.belisarioitem3)
        self.ui.item4.clicked.connect(self.belisarioitem4)
        self.ui.item5.clicked.connect(self.belisarioitem5)
        self.ui.item6.clicked.connect(self.belisarioitem6) 
        self.loadProducts()
        self.ui.remove.clicked.connect(self.belisarioremove) 
        self.ui.discount.clicked.connect(self.belisariodiscount)
        self.ui.paybtn.clicked.connect(self.belisariopay)
        self.ui.logout.clicked.connect(self.belisariologout)

    def belisariologout(self):
         from controller.belisario_login import BelisarioLoginUser
         self.window = BelisarioLoginUser(self.belisarioemail, self.belisariopassword, self.belisariofname, self.belisariolname, self.belisarioage)
         self.window.show()
         self.close()
        
    def belisariohp(self):
        self.ui.fname.setText(self.belisariofname)
        self.ui.lname.setText(self.belisariolname)
        belisarioage = str(self.belisarioage)
        self.ui.age.setText(belisarioage)
        print("Fname: ", self.belisariofname)
        print("Lname: ", self.belisariolname)
        print("Age: ", belisarioage)
           
        
    def belisarioitem1(self):
       belisarioname = "Burger" 
       belisarioprice = "120"
        
       if belisarioname and belisarioprice is not None:
            belisariorowCount = self.ui.itemtable.rowCount()
            self.ui.itemtable.insertRow(belisariorowCount)
            self.ui.itemtable.setItem(belisariorowCount, 0, QTableWidgetItem(belisarioname))
            self.ui.itemtable.setItem(belisariorowCount, 1, QTableWidgetItem(belisarioprice))
            self.belisariototalprice += 120
            
            self.ui.pay.setText(str(self.belisariototalprice))
    def belisarioitem2(self):
        belisarioname = "Iced Tea" 
        belisarioprice = "60"
        
        if belisarioname and belisarioprice is not None:
            belisariorowCount = self.ui.itemtable.rowCount()
            self.ui.itemtable.insertRow(belisariorowCount)
            self.ui.itemtable.setItem(belisariorowCount, 0, QTableWidgetItem(belisarioname))
            self.ui.itemtable.setItem(belisariorowCount, 1, QTableWidgetItem(belisarioprice)) 
            self.belisariototalprice += 60
            self.ui.pay.setText(str(self.belisariototalprice))
            
    def belisarioitem3(self):
        belisarioname = "Ice Cream" 
        belisarioprice = "100"
        
        if belisarioname and belisarioprice is not None:
            belisariorowCount = self.ui.itemtable.rowCount()
            self.ui.itemtable.insertRow(belisariorowCount)
            self.ui.itemtable.setItem(belisariorowCount, 0, QTableWidgetItem(belisarioname))
            self.ui.itemtable.setItem(belisariorowCount, 1, QTableWidgetItem(belisarioprice))
            self.belisariototalprice += 100
            self.ui.pay.setText(str(self.belisariototalprice))
            
    def belisarioitem4(self):
        belisarioname = "Fries" 
        belisarioprice = "70"
        
        if belisarioname and belisarioprice is not None:
            belisariorowCount = self.ui.itemtable.rowCount()
            self.ui.itemtable.insertRow(belisariorowCount)
            self.ui.itemtable.setItem(belisariorowCount, 0, QTableWidgetItem(belisarioname))
            self.ui.itemtable.setItem(belisariorowCount, 1, QTableWidgetItem(belisarioprice)) 
            self.belisariototalprice += 70
            self.ui.pay.setText(str(self.belisariototalprice))
            
    def belisarioitem5(self):
        belisarioname = "Spaghetti" 
        belisarioprice = "145"
        
        if belisarioname and belisarioprice is not None:
            belisariorowCount = self.ui.itemtable.rowCount()
            self.ui.itemtable.insertRow(belisariorowCount)
            self.ui.itemtable.setItem(belisariorowCount, 0, QTableWidgetItem(belisarioname))
            self.ui.itemtable.setItem(belisariorowCount, 1, QTableWidgetItem(belisarioprice)) 
            self.belisariototalprice += 145
            self.ui.pay.setText(str(self.belisariototalprice))
            
    def belisarioitem6(self):
        belisarioname = "Fried Chicken" 
        belisarioprice = "160"
        
        if belisarioname and belisarioprice is not None:
            belisariorowCount = self.ui.itemtable.rowCount()
            self.ui.itemtable.insertRow(belisariorowCount)
            self.ui.itemtable.setItem(belisariorowCount, 0, QTableWidgetItem(belisarioname))
            self.ui.itemtable.setItem(belisariorowCount, 1, QTableWidgetItem(belisarioprice)) 
            self.belisariototalprice += 160
            self.ui.pay.setText(str(self.belisariototalprice))
    
    

    def loadProducts(self):
        self.products = []
        
        self.ui.itemtable.setRowCount(len(self.products))
        self.ui.itemtable.setColumnCount(2)

        self.ui.itemtable.setHorizontalHeaderLabels(('Item', 'Price'))

        self.ui.itemtable.setColumnWidth(0, 100)
        self.ui.itemtable.setColumnWidth(1, 100)

        row_index = 0
        for product in self.products:
            self.ui.itemtable.setItem(row_index, 0, QTableWidgetItem(str(product['name'])))
            self.ui.itemtable.setItem(row_index, 1, QTableWidgetItem(str(product['price'])))
            row_index += 1
            
    def belisarioremove(self):
        for x in self.ui.itemtable.selectedItems():
            print(x.text())
            belisarioselected = self.ui.itemtable.currentRow()
            print(belisarioselected)
            self.belisariototalprice -= int(x.text())
            self.ui.itemtable.removeRow(belisarioselected)
            self.ui.pay.setText(str(self.belisariototalprice))
        
    def belisariodiscount(self):
        if int(self.belisarioage) >= 65:
            self.belisariodiscountprice = self.belisariototalprice * .80
            self.belisariototalprice = self.belisariodiscountprice
            self.ui.pay.setText(str(self.belisariototalprice))
        else:
            QMessageBox.information(self, "Discount", "Discount is only applicable for ages 65 and above.")
    
    def belisariopay(self):
        self.window = Belisariopay(self.belisariototalprice)
        self.window.show()
        self.window.belisariopayment()

