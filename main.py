from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from controller.belisario_register import BelisarioRegisterUser

if __name__ == "__main__":
    Belisarioapp = QApplication([])
    Belisariowindow = BelisarioRegisterUser()
    Belisariowindow.show()
    Belisarioapp.exec()
